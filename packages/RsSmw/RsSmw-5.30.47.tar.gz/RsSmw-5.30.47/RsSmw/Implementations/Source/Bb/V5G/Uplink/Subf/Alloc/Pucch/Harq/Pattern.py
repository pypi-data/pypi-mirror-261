from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PatternCls:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: List[str], subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:[SUBF<ST0>]:ALLoc<CH0>:PUCCh:HARQ:PATTern \n
		Snippet: driver.source.bb.v5G.uplink.subf.alloc.pucch.harq.pattern.set(pattern = ['rawAbc1', 'rawAbc2', 'rawAbc3'], subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		No command help available \n
			:param pattern: No help available
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.list_to_csv_str(pattern)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUCCh:HARQ:PATTern {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:[SUBF<ST0>]:ALLoc<CH0>:PUCCh:HARQ:PATTern \n
		Snippet: value: List[str] = driver.source.bb.v5G.uplink.subf.alloc.pucch.harq.pattern.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		No command help available \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: pattern: No help available"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUCCh:HARQ:PATTern?')
		return Conversions.str_to_str_list(response)
