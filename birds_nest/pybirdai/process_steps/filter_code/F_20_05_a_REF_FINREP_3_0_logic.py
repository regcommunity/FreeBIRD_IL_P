from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_20_05_a_REF_FINREP_3_0_UnionItem:
	base = None #F_20_05_a_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.DFLT_STTS"})
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.DFLT_STTS()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
	@lineage(dependencies={"base.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.PRFRMNG_STTS()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()

class F_20_05_a_REF_FINREP_3_0_Base:
	def DFLT_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def PRFRMNG_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass

class F_20_05_a_REF_FINREP_3_0_UnionTable :
	F_20_05_a_REF_FINREP_3_0_UnionItems = [] # F_20_05_a_REF_FINREP_3_0_UnionItem []
	F_20_05_a_REF_FINREP_3_0_Financial_guarantees_given_Table = None # Financial_guarantees_given
	def calc_F_20_05_a_REF_FINREP_3_0_UnionItems(self) -> list[F_20_05_a_REF_FINREP_3_0_UnionItem] :
		items = [] # F_20_05_a_REF_FINREP_3_0_UnionItem []
		for item in self.F_20_05_a_REF_FINREP_3_0_Financial_guarantees_given_Table.Financial_guarantees_givens:
			newItem = F_20_05_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_20_05_a_REF_FINREP_3_0_UnionItems = []
		self.F_20_05_a_REF_FINREP_3_0_UnionItems.extend(self.calc_F_20_05_a_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Financial_guarantees_given(F_20_05_a_REF_FINREP_3_0_Base):
	CRDT_FCLTY = None # CRDT_FCLTY
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS"})
	def DFLT_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS_DRVD"})
	def DFLT_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS_DRVD
	@lineage(dependencies={"CRDT_FCLTY.IMPRMNT_STTS"})
	def DFLT_STTS(self):
		return self.CRDT_FCLTY.IMPRMNT_STTS
	@lineage(dependencies={"CRDT_FCLTY.PRFRMNG_STTS"})
	def DFLT_STTS(self):
		return self.CRDT_FCLTY.PRFRMNG_STTS
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS"})
	def PRFRMNG_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS_DRVD"})
	def PRFRMNG_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS_DRVD
	@lineage(dependencies={"CRDT_FCLTY.IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.CRDT_FCLTY.IMPRMNT_STTS
	@lineage(dependencies={"CRDT_FCLTY.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self):
		return self.CRDT_FCLTY.PRFRMNG_STTS

class F_20_05_a_REF_FINREP_3_0_Financial_guarantees_given_Table:
	CRDT_FCLTY_Table = None # CRDT_FCLTY
	Financial_guarantees_givens = []# Financial_guarantees_given[]
	def calc_Financial_guarantees_givens(self) :
		items = [] # Financial_guarantees_given[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Financial_guarantees_givens = []
		self.Financial_guarantees_givens.extend(self.calc_Financial_guarantees_givens())
		CSVConverter.persist_object_as_csv(self,True)
		return None

