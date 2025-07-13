from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_18_00_b_REF_FINREP_3_0_UnionItem:
	base = None #F_18_00_b_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.base.ACCMLTD_IMPRMNT()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.base.RPYMNT_RGHTS()
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
	@lineage(dependencies={"base.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.base.ENTRPRS_SZ()
	@lineage(dependencies={"base.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.base.PRPS()
	@lineage(dependencies={"base.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.base.SBJCT_IMPRMNT_INDCTR()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
	@lineage(dependencies={"base.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.PRFRMNG_STTS()
	@lineage(dependencies={"base.DFLT_STTS"})
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.DFLT_STTS()
	@lineage(dependencies={"base.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.IMPRMNT_STTS()
	@lineage(dependencies={"base.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()

class F_18_00_b_REF_FINREP_3_0_Base:
	def ACCMLTD_IMPRMNT() -> int:
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def RPYMNT_RGHTS() -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
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
	def ENTRPRS_SZ() -> str:
		''' return string from SZ enumeration '''
		pass
	def PRPS() -> str:
		''' return string from PRPS enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def PRFRMNG_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def DFLT_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def IMPRMNT_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def CRRYNG_AMNT() -> int:
		pass

class F_18_00_b_REF_FINREP_3_0_UnionTable :
	F_18_00_b_REF_FINREP_3_0_UnionItems = [] # F_18_00_b_REF_FINREP_3_0_UnionItem []
	F_18_00_b_REF_FINREP_3_0_Other_loans_Table = None # Other_loans
	F_18_00_b_REF_FINREP_3_0_Financial_guarantees_given_Table = None # Financial_guarantees_given
	F_18_00_b_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None # Non_Negotiable_bonds
	def calc_F_18_00_b_REF_FINREP_3_0_UnionItems(self) -> list[F_18_00_b_REF_FINREP_3_0_UnionItem] :
		items = [] # F_18_00_b_REF_FINREP_3_0_UnionItem []
		for item in self.F_18_00_b_REF_FINREP_3_0_Other_loans_Table.Other_loanss:
			newItem = F_18_00_b_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_18_00_b_REF_FINREP_3_0_Financial_guarantees_given_Table.Financial_guarantees_givens:
			newItem = F_18_00_b_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_18_00_b_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss:
			newItem = F_18_00_b_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_18_00_b_REF_FINREP_3_0_UnionItems = []
		self.F_18_00_b_REF_FINREP_3_0_UnionItems.extend(self.calc_F_18_00_b_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Other_loans(F_18_00_b_REF_FINREP_3_0_Base):
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self):
		return self.CLLTRL.ACCMLTD_IMPRMNT
	@lineage(dependencies={"CLLTRL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.CLLTRL.CRRYNG_AMNT
	CRDT_FCLTY = None # CRDT_FCLTY
	@lineage(dependencies={"CRDT_FCLTY.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.CRDT_FCLTY.ACCNTNG_CLSSFCTN
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
	def IMPRMNT_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS_DRVD"})
	def IMPRMNT_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS_DRVD
	@lineage(dependencies={"CRDT_FCLTY.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self):
		return self.CRDT_FCLTY.IMPRMNT_STTS
	@lineage(dependencies={"CRDT_FCLTY.PRFRMNG_STTS"})
	def IMPRMNT_STTS(self):
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
	ENTTY_RL = None # ENTTY_RL
	@lineage(dependencies={"ENTTY_RL.ENTTY_GRP_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.ENTTY_GRP_RL_TYP
	@lineage(dependencies={"ENTTY_RL.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.ENTTY_RL_TYP
	@lineage(dependencies={"ENTTY_RL.ENTTY_TRNSCTN_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.ENTTY_TRNSCTN_RL_TYP
	@lineage(dependencies={"ENTTY_RL.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.PRTY_RL_TYP
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self):
		return self.INSTRMNT.RPYMNT_RGHTS
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_ORGN"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
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
	@lineage(dependencies={"INSTRMNT_RL.DFLT_STTS"})
	def DFLT_STTS(self):
		return self.INSTRMNT_RL.DFLT_STTS
	@lineage(dependencies={"INSTRMNT_RL.DFLT_STTS_DRVD"})
	def DFLT_STTS(self):
		return self.INSTRMNT_RL.DFLT_STTS_DRVD
	@lineage(dependencies={"INSTRMNT_RL.IMPRMNT_STTS"})
	def DFLT_STTS(self):
		return self.INSTRMNT_RL.IMPRMNT_STTS
	@lineage(dependencies={"INSTRMNT_RL.INTL_IMPRMNT_STTS"})
	def DFLT_STTS(self):
		return self.INSTRMNT_RL.INTL_IMPRMNT_STTS
	@lineage(dependencies={"INSTRMNT_RL.PRFRMNG_STTS"})
	def DFLT_STTS(self):
		return self.INSTRMNT_RL.PRFRMNG_STTS
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.DFLT_STTS"})
	def IMPRMNT_STTS(self):
		return self.INSTRMNT_RL.DFLT_STTS
	@lineage(dependencies={"INSTRMNT_RL.DFLT_STTS_DRVD"})
	def IMPRMNT_STTS(self):
		return self.INSTRMNT_RL.DFLT_STTS_DRVD
	@lineage(dependencies={"INSTRMNT_RL.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self):
		return self.INSTRMNT_RL.IMPRMNT_STTS
	@lineage(dependencies={"INSTRMNT_RL.INTL_IMPRMNT_STTS"})
	def IMPRMNT_STTS(self):
		return self.INSTRMNT_RL.INTL_IMPRMNT_STTS
	@lineage(dependencies={"INSTRMNT_RL.PRFRMNG_STTS"})
	def IMPRMNT_STTS(self):
		return self.INSTRMNT_RL.PRFRMNG_STTS
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
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.DFLT_STTS"})
	def DFLT_STTS(self):
		return self.PRTY.DFLT_STTS
	@lineage(dependencies={"PRTY.PRFRMNG_STTS"})
	def DFLT_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	@lineage(dependencies={"PRTY.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self):
		return self.PRTY.ENTRPRS_SZ
	@lineage(dependencies={"PRTY.DFLT_STTS"})
	def IMPRMNT_STTS(self):
		return self.PRTY.DFLT_STTS
	@lineage(dependencies={"PRTY.PRFRMNG_STTS"})
	def IMPRMNT_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	@lineage(dependencies={"PRTY.INSTTNL_SCTR_EBA_ITS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTNL_SCTR_EBA_ITS
	@lineage(dependencies={"PRTY.INSTTNL_SCTR_SHS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTNL_SCTR_SHS
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
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

class Financial_guarantees_given(F_18_00_b_REF_FINREP_3_0_Base):
	CRDT_FCLTY = None # CRDT_FCLTY
	@lineage(dependencies={"CRDT_FCLTY.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.CRDT_FCLTY.ACCNTNG_CLSSFCTN
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
	def IMPRMNT_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS_DRVD"})
	def IMPRMNT_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS_DRVD
	@lineage(dependencies={"CRDT_FCLTY.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self):
		return self.CRDT_FCLTY.IMPRMNT_STTS
	@lineage(dependencies={"CRDT_FCLTY.PRFRMNG_STTS"})
	def IMPRMNT_STTS(self):
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

class Non_Negotiable_bonds(F_18_00_b_REF_FINREP_3_0_Base):
	ENTTY_RL = None # ENTTY_RL
	@lineage(dependencies={"ENTTY_RL.ENTTY_GRP_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.ENTTY_GRP_RL_TYP
	@lineage(dependencies={"ENTTY_RL.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.ENTTY_RL_TYP
	@lineage(dependencies={"ENTTY_RL.ENTTY_TRNSCTN_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.ENTTY_TRNSCTN_RL_TYP
	@lineage(dependencies={"ENTTY_RL.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.PRTY_RL_TYP
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.IMPRMNT_STTS"})
	def DFLT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.INVSTR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.INVSTR_PRTY_RL_TYP
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
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS"})
	def DFLT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS"})
	def DFLT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS"})
	def IMPRMNT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INVSTR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INVSTR_PRTY_RL_TYP
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.DFLT_STTS"})
	def DFLT_STTS(self):
		return self.PRTY.DFLT_STTS
	@lineage(dependencies={"PRTY.PRFRMNG_STTS"})
	def DFLT_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	@lineage(dependencies={"PRTY.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self):
		return self.PRTY.ENTRPRS_SZ
	@lineage(dependencies={"PRTY.DFLT_STTS"})
	def IMPRMNT_STTS(self):
		return self.PRTY.DFLT_STTS
	@lineage(dependencies={"PRTY.PRFRMNG_STTS"})
	def IMPRMNT_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	@lineage(dependencies={"PRTY.INSTTNL_SCTR_EBA_ITS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTNL_SCTR_EBA_ITS
	@lineage(dependencies={"PRTY.INSTTNL_SCTR_SHS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTNL_SCTR_SHS
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
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
	@lineage(dependencies={"SCRTY_PSTN.DFLT_STTS"})
	def DFLT_STTS(self):
		return self.SCRTY_PSTN.DFLT_STTS
	@lineage(dependencies={"SCRTY_PSTN.DFLT_STTS_DRVD"})
	def DFLT_STTS(self):
		return self.SCRTY_PSTN.DFLT_STTS_DRVD
	@lineage(dependencies={"SCRTY_PSTN.DFLT_STTS"})
	def IMPRMNT_STTS(self):
		return self.SCRTY_PSTN.DFLT_STTS
	@lineage(dependencies={"SCRTY_PSTN.DFLT_STTS_DRVD"})
	def IMPRMNT_STTS(self):
		return self.SCRTY_PSTN.DFLT_STTS_DRVD
	@lineage(dependencies={"SCRTY_PSTN.DFLT_STTS"})
	def PRFRMNG_STTS(self):
		return self.SCRTY_PSTN.DFLT_STTS
	@lineage(dependencies={"SCRTY_PSTN.DFLT_STTS_DRVD"})
	def PRFRMNG_STTS(self):
		return self.SCRTY_PSTN.DFLT_STTS_DRVD
	@lineage(dependencies={"SCRTY_PSTN.INVSTR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_PSTN.INVSTR_PRTY_RL_TYP

class F_18_00_b_REF_FINREP_3_0_Other_loans_Table:
	CLLTRL_Table = None # CLLTRL
	CRDT_FCLTY_Table = None # CRDT_FCLTY
	ENTTY_RL_Table = None # ENTTY_RL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
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


class F_18_00_b_REF_FINREP_3_0_Financial_guarantees_given_Table:
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


class F_18_00_b_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
	ENTTY_RL_Table = None # ENTTY_RL
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

