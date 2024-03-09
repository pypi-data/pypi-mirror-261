"""BTTC.

BT testing common utilities.
"""
import atexit

from mobly.controllers import android_device
from bttc import core
from bttc import utils_loader
from bttc.utils import device_factory
from ppadb import client
from typing import TypeAlias


__version__ = '0.0.69'
__author__ = 'John Lee/Yuan Long Luo/Denny Chai'
__credits__ = 'Google Pixel PQM'


GeneralDevice: TypeAlias = android_device.AndroidDevice


def get(
    serial_number: str,
    required_func_module_names: set[str] | None = None,
    init_mbs: bool = False,
    init_sl4a: bool = False,
    init_snippet_uiautomator: bool = False,
    init_tl4a: bool = False):
  """Gets device by its serial number."""
  required_func_module_names = required_func_module_names or {}
  func_module_info = utils_loader.get_func_modules()
  device = device_factory.get(
      serial_number, init_mbs=init_mbs, init_sl4a=init_sl4a,
      init_snippet_uiautomator=init_snippet_uiautomator,
      init_tl4a=init_tl4a)
  atexit.register(device.services.stop_all)
  for module_name, module_info in func_module_info.items():
    if module_name in required_func_module_names or module_info.auto_load:
      module_info.module.bind(device)

  return device


def get_all(
    required_func_module_names: set[str] | None = None,
    init_mbs: bool = False,
    init_sl4a: bool = False,
    init_snippet_uiautomator: bool = False,
    init_tl4a: bool = False):
  """Gets all connected device(s) from local."""
  device_info = {}
  adb_client = client.Client(host='localhost', port=5037)
  for device in adb_client.devices():
    device_info[device.serial] = get(
        device.serial,
        required_func_module_names=required_func_module_names,
        init_mbs=init_mbs,
        init_sl4a=init_sl4a,
        init_snippet_uiautomator=init_snippet_uiautomator,
        init_tl4a=init_tl4a)

  return device_info


def list_utils(dut: GeneralDevice) -> list[core.UtilBase]:
  """Gets loaded utilities from the given DUT.

  Args:
    dut: Device to search loaded utilities.

  Returns:
    List of loaded utilities.
  """
  loaded_utils = []
  for field_name, field_obj in dut.__dict__.items():
    if isinstance(field_obj, core.UtilBase):
      print(f'Loaded "{field_name}": {field_obj.DESCRIPTION}')
      loaded_utils.append(field_obj)

  return loaded_utils
