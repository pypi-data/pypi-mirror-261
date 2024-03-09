import binascii
import json
import os
import time
import uuid
from time import sleep
from typing import Optional, Callable, Any, List, Union, Literal

import requests
from pydantic import BaseModel
from websocket import create_connection

from e2b import Sandbox, EnvVars, ProcessMessage, OpenPort
from e2b.constants import TIMEOUT


class Error(BaseModel):
    name: str
    value: str
    traceback: List[str]


class Result(BaseModel):
    output: Optional[str] = None
    stdout: List[str] = []
    stderr: List[str] = []
    error: Optional[Error] = None
    # TODO: This will be changed in the future, it's just to enable the use of display_data
    display_data: List[dict] = []


class CodeInterpreterV2(Sandbox):
    template = "code-interpreter-stateful"

    def __init__(
        self,
        template: Optional[str] = None,
        api_key: Optional[str] = None,
        cwd: Optional[str] = None,
        env_vars: Optional[EnvVars] = None,
        timeout: Optional[float] = TIMEOUT,
        on_stdout: Optional[Callable[[ProcessMessage], Any]] = None,
        on_stderr: Optional[Callable[[ProcessMessage], Any]] = None,
        on_exit: Optional[Callable[[int], Any]] = None,
        **kwargs,
    ):
        super().__init__(
            template=template or self.template,
            api_key=api_key,
            cwd=cwd,
            env_vars=env_vars,
            timeout=timeout,
            on_stdout=on_stdout,
            on_stderr=on_stderr,
            on_exit=on_exit,
            **kwargs,
        )

        self._setup_jupyter()

    def _setup_jupyter(self) -> None:
        config = json.loads(self.filesystem.read("/root/.jupyter/config.json"))
        self._jupyter_server_token = config["token"]
        self._jupyter_kernel_id = config["kernel_id"]

    def _connect_kernel(self):
        header = {"Authorization": f"Token {self._jupyter_server_token}"}
        return create_connection(
            f"{self.get_protocol('ws')}://{self.get_hostname(8888)}/api/kernels/{self._jupyter_kernel_id}/channels",
            header=header,
        )

    @staticmethod
    def _send_execute_request(code: str) -> dict:
        msg_id = str(uuid.uuid4())
        session = str(uuid.uuid4())

        return {
            "header": {
                "msg_id": msg_id,
                "username": "e2b",
                "session": session,
                "msg_type": "execute_request",
                "version": "5.3",
            },
            "parent_header": {},
            "metadata": {},
            "content": {
                "code": code,
                "silent": False,
                "store_history": False,
                "user_expressions": {},
                "allow_stdin": False,
            },
        }

    @staticmethod
    def _wait_for_result(
        ws,
        on_stdout: Optional[Callable[[ProcessMessage], Any]],
        on_stderr: Optional[Callable[[ProcessMessage], Any]],
    ) -> Result:
        result = Result()
        input_accepted = False

        while True:
            response = json.loads(ws.recv())
            if response["msg_type"] == "error":
                result.error = Error(
                    name=response["content"]["ename"],
                    value=response["content"]["evalue"],
                    traceback=response["content"]["traceback"],
                )

            elif response["msg_type"] == "stream":
                if response["content"]["name"] == "stdout":
                    result.stdout.append(response["content"]["text"])
                    if on_stdout:
                        on_stdout(
                            ProcessMessage(
                                line=response["content"]["text"],
                                timestamp=time.time_ns(),
                            )
                        )

                elif response["content"]["name"] == "stderr":
                    result.stderr.append(response["content"]["text"])
                    if on_stderr:
                        on_stderr(
                            ProcessMessage(
                                line=response["content"]["text"],
                                error=True,
                                timestamp=time.time_ns(),
                            )
                        )

            elif response["msg_type"] == "display_data":
                result.display_data.append(response["content"]["data"])

            elif response["msg_type"] == "execute_result":
                result.output = response["content"]["data"]["text/plain"]

            elif response["msg_type"] == "status":
                if response["content"]["execution_state"] == "idle":
                    if input_accepted:
                        break
                elif response["content"]["execution_state"] == "error":
                    result.error = Error(
                        name=response["content"]["ename"],
                        value=response["content"]["evalue"],
                        traceback=response["content"]["traceback"],
                    )
                    break

            elif response["msg_type"] == "execute_reply":
                if response["content"]["status"] == "error":
                    result.error = Error(
                        name=response["content"]["ename"],
                        value=response["content"]["evalue"],
                        traceback=response["content"]["traceback"],
                    )
                elif response["content"]["status"] == "ok":
                    pass

            elif response["msg_type"] == "execute_input":
                input_accepted = True
            else:
                print("[UNHANDLED MESSAGE TYPE]:", response["msg_type"])
        return result

    def exec_python(
        self,
        code: str,
        on_stdout: Optional[Callable[[ProcessMessage], Any]] = None,
        on_stderr: Optional[Callable[[ProcessMessage], Any]] = None,
    ) -> Result:
        ws = self._connect_kernel()
        ws.send(json.dumps(self._send_execute_request(code)))
        result = self._wait_for_result(ws, on_stdout, on_stderr)

        ws.close()

        return result
