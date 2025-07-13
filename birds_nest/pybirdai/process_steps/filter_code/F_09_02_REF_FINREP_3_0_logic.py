from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_09_02_REF_FINREP_3_0_UnionItem:
	base = None #F_09_02_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
	@lineage(dependencies={"base.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.base.INSTTTNL_SCTR()
	@lineage(dependencies={"base.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self) -> str:
		''' return string from MLTLTRL_DVLPMNT_BNK_INDCTR enumeration '''
		return self.base.MLTLTRL_DVLPMNT_BNK_INDCTR()
	@lineage(dependencies={"base.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self) -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		return self.base.PRTY_RL_TYP()
	@lineage(dependencies={"base.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self) -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		return self.base.MN_DBTR_INDCTR()
	@lineage(dependencies={"base.NMNL_AMNT"})
	def NMNL_AMNT(self) -> int:
		return self.base.NMNL_AMNT()

class F_09_02_REF_FINREP_3_0_Base:
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def MLTLTRL_DVLPMNT_BNK_INDCTR() -> str:
		''' return string from MLTLTRL_DVLPMNT_BNK_INDCTR enumeration '''
		pass
	def PRTY_RL_TYP() -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		pass
	def MN_DBTR_INDCTR() -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		pass
	def NMNL_AMNT() -> int:
		pass

class F_09_02_REF_FINREP_3_0_UnionTable :
	F_09_02_REF_FINREP_3_0_UnionItems = [] # F_09_02_REF_FINREP_3_0_UnionItem []
	F_09_02_REF_FINREP_3_0_Financial_guarantees_received_Table = None # Financial_guarantees_received
	def calc_F_09_02_REF_FINREP_3_0_UnionItems(self) -> list[F_09_02_REF_FINREP_3_0_UnionItem] :
		items = [] # F_09_02_REF_FINREP_3_0_UnionItem []
		for item in self.F_09_02_REF_FINREP_3_0_Financial_guarantees_received_Table.Financial_guarantees_receiveds:
			newItem = F_09_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_09_02_REF_FINREP_3_0_UnionItems = []
		self.F_09_02_REF_FINREP_3_0_UnionItems.extend(self.calc_F_09_02_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Financial_guarantees_received(F_09_02_REF_FINREP_3_0_Base):
	CRDT_FCLTY = None # CRDT_FCLTY
	@lineage(dependencies={"CRDT_FCLTY.NMNL_AMNT"})
	def NMNL_AMNT(self):
		return self.CRDT_FCLTY.NMNL_AMNT
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.NMNL_AMNT"})
	def NMNL_AMNT(self):
		return self.INSTRMNT.NMNL_AMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_ORGN"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT

class F_09_02_REF_FINREP_3_0_Financial_guarantees_received_Table:
	CRDT_FCLTY_Table = None # CRDT_FCLTY
	INSTRMNT_Table = None # INSTRMNT
	Financial_guarantees_receiveds = []# Financial_guarantees_received[]
	def calc_Financial_guarantees_receiveds(self) :
		items = [] # Financial_guarantees_received[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Financial_guarantees_receiveds = []
		self.Financial_guarantees_receiveds.extend(self.calc_Financial_guarantees_receiveds())
		CSVConverter.persist_object_as_csv(self,True)
		return None

