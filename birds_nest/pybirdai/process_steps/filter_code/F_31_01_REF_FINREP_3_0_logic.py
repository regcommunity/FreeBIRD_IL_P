from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_31_01_REF_FINREP_3_0_UnionItem:
	base = None #F_31_01_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.base.SBJCT_IMPRMNT_INDCTR()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.PRFRMNG_STTS()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
	@lineage(dependencies={"base.TYP_ACCNTNG_ITM"})
	def TYP_ACCNTNG_ITM(self) -> str:
		''' return string from TYP_ACCNTNG_ITM enumeration '''
		return self.base.TYP_ACCNTNG_ITM()
	@lineage(dependencies={"base.NMNL_AMNT"})
	def NMNL_AMNT(self) -> int:
		return self.base.NMNL_AMNT()
	@lineage(dependencies={"base.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.base.ACCMLTD_IMPRMNT()
	@lineage(dependencies={"base.NTNL_AMNT"})
	def NTNL_AMNT(self) -> int:
		return self.base.NTNL_AMNT()

class F_31_01_REF_FINREP_3_0_Base:
	def CRRYNG_AMNT() -> int:
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def PRFRMNG_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def TYP_ACCNTNG_ITM() -> str:
		''' return string from TYP_ACCNTNG_ITM enumeration '''
		pass
	def NMNL_AMNT() -> int:
		pass
	def ACCMLTD_IMPRMNT() -> int:
		pass
	def NTNL_AMNT() -> int:
		pass

class F_31_01_REF_FINREP_3_0_UnionTable :
	F_31_01_REF_FINREP_3_0_UnionItems = [] # F_31_01_REF_FINREP_3_0_UnionItem []
	F_31_01_REF_FINREP_3_0_Other_loans_Table = None # Other_loans
	F_31_01_REF_FINREP_3_0_Deposits_Table = None # Deposits
	F_31_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None # Non_Negotiable_bonds
	F_31_01_REF_FINREP_3_0_Provisions_Table = None # Provisions
	def calc_F_31_01_REF_FINREP_3_0_UnionItems(self) -> list[F_31_01_REF_FINREP_3_0_UnionItem] :
		items = [] # F_31_01_REF_FINREP_3_0_UnionItem []
		for item in self.F_31_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss:
			newItem = F_31_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_31_01_REF_FINREP_3_0_Deposits_Table.Depositss:
			newItem = F_31_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_31_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss:
			newItem = F_31_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_31_01_REF_FINREP_3_0_Provisions_Table.Provisionss:
			newItem = F_31_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_31_01_REF_FINREP_3_0_UnionItems = []
		self.F_31_01_REF_FINREP_3_0_UnionItems.extend(self.calc_F_31_01_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Other_loans(F_31_01_REF_FINREP_3_0_Base):
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self):
		return self.CLLTRL.ACCMLTD_IMPRMNT
	@lineage(dependencies={"CLLTRL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.CLLTRL.CRRYNG_AMNT
	@lineage(dependencies={"CLLTRL.NTNL_AMNT"})
	def NTNL_AMNT(self):
		return self.CLLTRL.NTNL_AMNT
	CRDT_FCLTY = None # CRDT_FCLTY
	@lineage(dependencies={"CRDT_FCLTY.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.CRDT_FCLTY.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"CRDT_FCLTY.NMNL_AMNT"})
	def NMNL_AMNT(self):
		return self.CRDT_FCLTY.NMNL_AMNT
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
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.NMNL_AMNT"})
	def NMNL_AMNT(self):
		return self.INSTRMNT.NMNL_AMNT
	@lineage(dependencies={"INSTRMNT.NTNL_AMNT"})
	def NTNL_AMNT(self):
		return self.INSTRMNT.NTNL_AMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_ORGN"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self):
		return self.INSTRMNT_RL.ACCMLTD_IMPRMNT
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.DFLT_STTS"})
	def PRFRMNG_STTS(self):
		return self.INSTRMNT_RL.DFLT_STTS
	@lineage(dependencies={"INSTRMNT_RL.DFLT_STTS_DRVD"})
	def PRFRMNG_STTS(self):
		return self.INSTRMNT_RL.DFLT_STTS_DRVD
	@lineage(dependencies={"INSTRMNT_RL.IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.INSTRMNT_RL.IMPRMNT_STTS
	@lineage(dependencies={"INSTRMNT_RL.INTL_IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.INSTRMNT_RL.INTL_IMPRMNT_STTS
	@lineage(dependencies={"INSTRMNT_RL.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self):
		return self.INSTRMNT_RL.PRFRMNG_STTS
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.DFLT_STTS"})
	def PRFRMNG_STTS(self):
		return self.PRTY.DFLT_STTS
	@lineage(dependencies={"PRTY.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR

class Deposits(F_31_01_REF_FINREP_3_0_Base):
	CRDT_FCLTY = None # CRDT_FCLTY
	@lineage(dependencies={"CRDT_FCLTY.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.CRDT_FCLTY.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"CRDT_FCLTY.NMNL_AMNT"})
	def NMNL_AMNT(self):
		return self.CRDT_FCLTY.NMNL_AMNT
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
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.NMNL_AMNT"})
	def NMNL_AMNT(self):
		return self.INSTRMNT.NMNL_AMNT
	@lineage(dependencies={"INSTRMNT.NTNL_AMNT"})
	def NTNL_AMNT(self):
		return self.INSTRMNT.NTNL_AMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_ORGN"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self):
		return self.INSTRMNT_RL.ACCMLTD_IMPRMNT
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.DFLT_STTS"})
	def PRFRMNG_STTS(self):
		return self.INSTRMNT_RL.DFLT_STTS
	@lineage(dependencies={"INSTRMNT_RL.DFLT_STTS_DRVD"})
	def PRFRMNG_STTS(self):
		return self.INSTRMNT_RL.DFLT_STTS_DRVD
	@lineage(dependencies={"INSTRMNT_RL.IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.INSTRMNT_RL.IMPRMNT_STTS
	@lineage(dependencies={"INSTRMNT_RL.INTL_IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.INSTRMNT_RL.INTL_IMPRMNT_STTS
	@lineage(dependencies={"INSTRMNT_RL.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self):
		return self.INSTRMNT_RL.PRFRMNG_STTS
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.DFLT_STTS"})
	def PRFRMNG_STTS(self):
		return self.PRTY.DFLT_STTS
	@lineage(dependencies={"PRTY.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self):
		return self.PRTY.PRFRMNG_STTS

class Non_Negotiable_bonds(F_31_01_REF_FINREP_3_0_Base):
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.NMNL_AMNT"})
	def NMNL_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.NMNL_AMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.IMPRMNT_STTS
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCMLTD_IMPRMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.NMNL_AMNT"})
	def NMNL_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.NMNL_AMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.DFLT_STTS"})
	def PRFRMNG_STTS(self):
		return self.PRTY.DFLT_STTS
	@lineage(dependencies={"PRTY.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	SCRTY_PSTN = None # SCRTY_PSTN
	@lineage(dependencies={"SCRTY_PSTN.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.SCRTY_PSTN.CRRYNG_AMNT
	@lineage(dependencies={"SCRTY_PSTN.NMNL_AMNT"})
	def NMNL_AMNT(self):
		return self.SCRTY_PSTN.NMNL_AMNT
	@lineage(dependencies={"SCRTY_PSTN.DFLT_STTS"})
	def PRFRMNG_STTS(self):
		return self.SCRTY_PSTN.DFLT_STTS
	@lineage(dependencies={"SCRTY_PSTN.DFLT_STTS_DRVD"})
	def PRFRMNG_STTS(self):
		return self.SCRTY_PSTN.DFLT_STTS_DRVD

class Provisions(F_31_01_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self):
		return self.NN_FNNCL_ASST.ACCMLTD_IMPRMNT
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT
	@lineage(dependencies={"NN_FNNCL_ASST.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.NN_FNNCL_ASST.HLD_SL_INDCTR
	@lineage(dependencies={"NN_FNNCL_ASST.TYP_NN_FNNCL_ASST"})
	def TYP_ACCNTNG_ITM(self):
		return self.NN_FNNCL_ASST.TYP_NN_FNNCL_ASST

class F_31_01_REF_FINREP_3_0_Other_loans_Table:
	CLLTRL_Table = None # CLLTRL
	CRDT_FCLTY_Table = None # CRDT_FCLTY
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Other_loanss = []# Other_loans[]
	def calc_Other_loanss(self) :
		items = [] # Other_loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Other_loanss = []
		self.Other_loanss.extend(self.calc_Other_loanss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_31_01_REF_FINREP_3_0_Deposits_Table:
	CRDT_FCLTY_Table = None # CRDT_FCLTY
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Depositss = []# Deposits[]
	def calc_Depositss(self) :
		items = [] # Deposits[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Depositss = []
		self.Depositss.extend(self.calc_Depositss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_31_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	SCRTY_PSTN_Table = None # SCRTY_PSTN
	Non_Negotiable_bondss = []# Non_Negotiable_bonds[]
	def calc_Non_Negotiable_bondss(self) :
		items = [] # Non_Negotiable_bonds[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Non_Negotiable_bondss = []
		self.Non_Negotiable_bondss.extend(self.calc_Non_Negotiable_bondss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_31_01_REF_FINREP_3_0_Provisions_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Provisionss = []# Provisions[]
	def calc_Provisionss(self) :
		items = [] # Provisions[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Provisionss = []
		self.Provisionss.extend(self.calc_Provisionss())
		CSVConverter.persist_object_as_csv(self,True)
		return None

