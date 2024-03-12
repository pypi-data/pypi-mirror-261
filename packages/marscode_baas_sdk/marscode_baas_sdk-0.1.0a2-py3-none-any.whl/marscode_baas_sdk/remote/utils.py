import requests
import time

_SYSTEM_ERROR_CODE = "0200001"

def _parse_response(resp:requests.Response):
  try:
    ret = resp.json()
  except Exception:
    raise RemoteError(_SYSTEM_ERROR_CODE, resp.status_code, f"unexpected response, status code: {resp.status_code}, message: {resp.text}", None)
  if ("ResponseMetadata" not in ret) or (ret["ResponseMetadata"] == None) or ("Error" not in ret["ResponseMetadata"]):
    raise RemoteError(_SYSTEM_ERROR_CODE, resp.status_code, f"unexpected response without meta data field, status code: {resp.status_code}, message: {resp.text}", None)
  if (ret["ResponseMetadata"]["Error"] == None) or (ret["ResponseMetadata"]["Error"]["Code"]==""):
    if "Result" in ret:
      return ret["Result"]
    else:
      raise RemoteError(_SYSTEM_ERROR_CODE, resp.status_code, f"unexpected response without result field, status code: {resp.status_code}, message: {resp.text}", None)
  if ret["ResponseMetadata"]["Error"]["Code"]!="":
    err = ret["ResponseMetadata"]["Error"]
    raise RemoteError(err["Code"], resp.status_code, err["Message"], err["Data"])
  else:
    raise RemoteError(_SYSTEM_ERROR_CODE, resp.status_code, f"unexpected response, status code: {resp.status_code}, message: {resp.text}", None)

class RemoteError(Exception):
  """
  Error From Remote Server
  """
  code = None
  http_status = None
  message = None
  data = None
  def __init__(self, code:str, http_code:str, message:str, data:dict, *args, **kwargs):
    self.code = code
    self.http_code = http_code
    self.message = message
    self.data = data
    super().__init__(*args, **kwargs)
  def __str__(self) -> str:
    return f"remote error, http_status: {self.http_code}, code: {self.code}, message: {self.message}"

def retry(times:int, decay:float):
  def inner(f):
    def wraped(*args, **kwarg):
      for i in range(0, times+1):
        try:
          return f(*args, **kwarg)
        except Exception as e:
          if i == times:
            raise e
          time.sleep(decay)
    return wraped
  return inner  