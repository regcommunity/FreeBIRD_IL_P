from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_05_01_REF_FINREP_3_0_UnionItem:
	base = None #F_05_01_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.base.GRSS_CRRYNG_AMNT()
	@lineage(dependencies={"base.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.base.PRPS()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.base.INSTTTNL_SCTR()
	@lineage(dependencies={"base.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self) -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		return self.base.PRTY_RL_TYP()
	@lineage(dependencies={"base.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self) -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		return self.base.MN_DBTR_INDCTR()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.base.RPYMNT_RGHTS()
	@lineage(dependencies={"base.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.base.PRJCT_FNNC_LN()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
	@lineage(dependencies={"base.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()
	@lineage(dependencies={"base.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self) -> str:
		''' return string from MLTLTRL_DVLPMNT_BNK_INDCTR enumeration '''
		return self.base.MLTLTRL_DVLPMNT_BNK_INDCTR()

class F_05_01_REF_FINREP_3_0_Base:
	def GRSS_CRRYNG_AMNT() -> int:
		pass
	def PRPS() -> str:
		''' return string from PRPS enumeration '''
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def PRTY_RL_TYP() -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		pass
	def MN_DBTR_INDCTR() -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def RPYMNT_RGHTS() -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		pass
	def PRJCT_FNNC_LN() -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def CRRYNG_AMNT() -> int:
		pass
	def MLTLTRL_DVLPMNT_BNK_INDCTR() -> str:
		''' return string from MLTLTRL_DVLPMNT_BNK_INDCTR enumeration '''
		pass

class F_05_01_REF_FINREP_3_0_UnionTable :
	F_05_01_REF_FINREP_3_0_UnionItems = [] # F_05_01_REF_FINREP_3_0_UnionItem []
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None # Trade_receivables
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None # Finance_leases
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None # Reverse_repurchase_agreements
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None # Other_loans
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None # Non_Negotiable_bonds
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None # Credit_card_debt
	def calc_F_05_01_REF_FINREP_3_0_UnionItems(self) -> list[F_05_01_REF_FINREP_3_0_UnionItem] :
		items = [] # F_05_01_REF_FINREP_3_0_UnionItem []
		for item in self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0_UnionItems = []
		self.F_05_01_REF_FINREP_3_0_UnionItems.extend(self.calc_F_05_01_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Trade_receivables(F_05_01_REF_FINREP_3_0_Base):
	pass
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	FNNCL_ASST_INSTRMNT_DRVD_DT = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR
	pass
	INTRNTNL_ORGNSTN = None # INTRNTNL_ORGNSTN
	@lineage(dependencies={"INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		if self.INTRNTNL_ORGNSTN is not None:
			return self.INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR
		else:
			return '2' #"Not_a_Multilateral_development_bank" 
	FNNCL_ASST_INSTRMNT = None # FNNCL_ASST_INSTRMNT
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRPS"})
	def PRPS(self):
		return self.FNNCL_ASST_INSTRMNT.PRPS
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self):
		return self.FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN
	pass
	pass
	pass
	pass
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT
	LN_EXCLDNG_RPRCHS_AGRMNT = None # LN_EXCLDNG_RPRCHS_AGRMNT
	@lineage(dependencies={"LN_EXCLDNG_RPRCHS_AGRMNT.LN_TYP"})
	def TYP_INSTRMNT(self):
		return self.LN_EXCLDNG_RPRCHS_AGRMNT.LN_TYP
	pass
	TRD_RCVBL_ASSGND_DBTR_ASSGNMNT = None # TRD_RCVBL_ASSGND_DBTR_ASSGNMNT
	@lineage(dependencies={"TRD_RCVBL_ASSGND_DBTR_ASSGNMNT.ASSNGND_DBTR_LGL_PRSN_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.TRD_RCVBL_ASSGND_DBTR_ASSGNMNT.ASSNGND_DBTR_LGL_PRSN_RL_TYP
	pass
	pass

class Finance_leases(F_05_01_REF_FINREP_3_0_Base):
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	FNNCL_ASST_INSTRMNT_DRVD_DT = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR
	INTRNTNL_ORGNSTN = None # INTRNTNL_ORGNSTN
	@lineage(dependencies={"INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		if self.INTRNTNL_ORGNSTN is not None:
			return self.INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR
		else:
			return '2' #"Not_a_Multilateral_development_bank" 
	FNNCL_ASST_INSTRMNT = None # FNNCL_ASST_INSTRMNT
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRPS"})
	def PRPS(self):
		return self.FNNCL_ASST_INSTRMNT.PRPS
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self):
		return self.FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN
	pass
	pass
	pass
	pass
	pass
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT
	LN_EXCLDNG_RPRCHS_AGRMNT = None # LN_EXCLDNG_RPRCHS_AGRMNT
	@lineage(dependencies={"LN_EXCLDNG_RPRCHS_AGRMNT.LN_TYP"})
	def TYP_INSTRMNT(self):
		return self.LN_EXCLDNG_RPRCHS_AGRMNT.LN_TYP
	pass
	FNNCL_LS_LSS_ASSGNMNT = None # FNNCL_LS_LSS_ASSGNMNT
	@lineage(dependencies={"FNNCL_LS_LSS_ASSGNMNT.LS_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.FNNCL_LS_LSS_ASSGNMNT.LS_PRTY_RL_TYP
	pass

class Reverse_repurchase_agreements(F_05_01_REF_FINREP_3_0_Base):
	pass
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR
	INTRNTNL_ORGNSTN = None # INTRNTNL_ORGNSTN
	@lineage(dependencies={"INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		if self.INTRNTNL_ORGNSTN is not None:
			return self.INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR
		else:
			return '2' #"Not_a_Multilateral_development_bank" 
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT
	FNNCL_ASST_INSTRMNT = None # FNNCL_ASST_INSTRMNT
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRPS"})
	def PRPS(self):
		return self.FNNCL_ASST_INSTRMNT.PRPS
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self):
		return self.FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN
	pass
	pass
	pass
	pass
	ENTTY_RL = None # ENTTY_RL
	@lineage(dependencies={"ENTTY_RL.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.ENTTY_RL.ENTTY_RL_TYP
	FNNCL_ASST_INSTRMNT_DRVD_DT = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	pass
	SFT = None # SFT
	@lineage(dependencies={"SFT.SFT_TYP"})
	def TYP_INSTRMNT(self):
		return self.SFT.SFT_TYP
	pass
	pass

class Other_loans(F_05_01_REF_FINREP_3_0_Base):
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	FNNCL_ASST_INSTRMNT_DRVD_DT = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT
	FNNCL_ASST_INSTRMNT = None # FNNCL_ASST_INSTRMNT
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRPS"})
	def PRPS(self):
		return self.FNNCL_ASST_INSTRMNT.PRPS
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self):
		return self.FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR
	OTHR_LN_DBTR_ASSGNMNT = None # OTHR_LN_DBTR_ASSGNMNT
	@lineage(dependencies={"OTHR_LN_DBTR_ASSGNMNT.LN_DBTR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.OTHR_LN_DBTR_ASSGNMNT.LN_DBTR_PRTY_RL_TYP
	@lineage(dependencies={"OTHR_LN_DBTR_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		return self.OTHR_LN_DBTR_ASSGNMNT.MN_DBTR_INDCTR
	INTRNTNL_ORGNSTN = None # INTRNTNL_ORGNSTN
	@lineage(dependencies={"INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		if self.INTRNTNL_ORGNSTN is not None:
			return self.INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR
		else:
			return '2' #"Not_a_Multilateral_development_bank" 
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'	
	LN_EXCLDNG_RPRCHS_AGRMNT = None # LN_EXCLDNG_RPRCHS_AGRMNT
	@lineage(dependencies={"LN_EXCLDNG_RPRCHS_AGRMNT.LN_TYP"})
	def TYP_INSTRMNT(self):
		return self.LN_EXCLDNG_RPRCHS_AGRMNT.LN_TYP
	pass

class Non_Negotiable_bonds(F_05_01_REF_FINREP_3_0_Base):
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	INTRNTNL_ORGNSTN = None # INTRNTNL_ORGNSTN
	@lineage(dependencies={"INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		if self.INTRNTNL_ORGNSTN is not None:
			return self.INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR
		else:
			return '2' #"Not_a_Multilateral_development_bank" 
	ISIN_SCRTY = None # ISIN_SCRTY
	@lineage(dependencies={"ISIN_SCRTY.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.ISIN_SCRTY.NGTBL_SCRTY_INDCTR
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT.GRSS_CRRYNG_AMNT
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'	
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	def TYP_INSTRMNT(self):
		return '1022'
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	pass
	SCRTY_ISSR_ASSGNMNT = None # SCRTY_ISSR_ASSGNMNT
	@lineage(dependencies={"SCRTY_ISSR_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ISSR_ASSGNMNT.PRTY_RL_TYP
	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return "2" #"Non_project_finance_loan"
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration we need to get this from the IFRS part'''
		return '2'
	def PRPS(self) -> str:
		''' return string from PRPS enumeration , other purpose'''
		return '19'

class Credit_card_debt(F_05_01_REF_FINREP_3_0_Base):
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	FNNCL_ASST_INSTRMNT_DRVD_DT = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR
	pass
	INTRNTNL_ORGNSTN = None # INTRNTNL_ORGNSTN
	@lineage(dependencies={"INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		if self.INTRNTNL_ORGNSTN is not None:
			return self.INTRNTNL_ORGNSTN.MLTLTRL_DVLPMNT_BNK_INDCTR
		else:
			return '2' #"Not_a_Multilateral_development_bank" 
	FNNCL_ASST_INSTRMNT = None # FNNCL_ASST_INSTRMNT
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRPS"})
	def PRPS(self):
		return self.FNNCL_ASST_INSTRMNT.PRPS
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self):
		return self.FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'	
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT
	LN_EXCLDNG_RPRCHS_AGRMNT = None # LN_EXCLDNG_RPRCHS_AGRMNT
	@lineage(dependencies={"LN_EXCLDNG_RPRCHS_AGRMNT.LN_TYP"})
	def TYP_INSTRMNT(self):
		return self.LN_EXCLDNG_RPRCHS_AGRMNT.LN_TYP
	pass
	CRDT_CRD_DBT_DBTR_ASSGNMNT = None # CRDT_CRD_DBT_DBTR_ASSGNMNT
	@lineage(dependencies={"CRDT_CRD_DBT_DBTR_ASSGNMNT.LN_DBTR_PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.CRDT_CRD_DBT_DBTR_ASSGNMNT.LN_DBTR_PRTY_RL_TYP

class F_05_01_REF_FINREP_3_0_Trade_receivables_Table:
	PRTY_Table = None # PRTY
	FNNCL_ASST_INSTRMNT_DRVD_DT_Table = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	INTRNTNL_ORGNSTN_Table = None # INTRNTNL_ORGNSTN
	FNNCL_ASST_INSTRMNT_Table = None # FNNCL_ASST_INSTRMNT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	LN_EXCLDNG_RPRCHS_AGRMNT_Table = None # LN_EXCLDNG_RPRCHS_AGRMNT
	TRD_RCVBL_ASSGND_DBTR_ASSGNMNT_Table = None # TRD_RCVBL_ASSGND_DBTR_ASSGNMNT
	Trade_receivabless = []# Trade_receivables[]
	def calc_Trade_receivabless(self) :
		items = [] # Trade_receivables[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Trade_receivabless = []
		self.Trade_receivabless.extend(self.calc_Trade_receivabless())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Finance_leases_Table:
	PRTY_Table = None # PRTY
	FNNCL_ASST_INSTRMNT_DRVD_DT_Table = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	INTRNTNL_ORGNSTN_Table = None # INTRNTNL_ORGNSTN
	FNNCL_ASST_INSTRMNT_Table = None # FNNCL_ASST_INSTRMNT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	LN_EXCLDNG_RPRCHS_AGRMNT_Table = None # LN_EXCLDNG_RPRCHS_AGRMNT
	FNNCL_LS_LSS_ASSGNMNT_Table = None # FNNCL_LS_LSS_ASSGNMNT
	Finance_leasess = []# Finance_leases[]
	def calc_Finance_leasess(self) :
		items = [] # Finance_leases[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Finance_leasess = []
		self.Finance_leasess.extend(self.calc_Finance_leasess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table:
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	INTRNTNL_ORGNSTN_Table = None # INTRNTNL_ORGNSTN
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	FNNCL_ASST_INSTRMNT_Table = None # FNNCL_ASST_INSTRMNT
	ENTTY_RL_Table = None # ENTTY_RL
	FNNCL_ASST_INSTRMNT_DRVD_DT_Table = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	PRTY_Table = None # PRTY
	SFT_Table = None # SFT
	Reverse_repurchase_agreementss = []# Reverse_repurchase_agreements[]
	def calc_Reverse_repurchase_agreementss(self) :
		items = [] # Reverse_repurchase_agreements[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Reverse_repurchase_agreementss = []
		self.Reverse_repurchase_agreementss.extend(self.calc_Reverse_repurchase_agreementss())
		CSVConverter.persist_object_as_csv(self,True)
		return None



	
class F_05_01_REF_FINREP_3_0_Other_loans_Table:
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	PRTY_Table = None # PRTY
	FNNCL_ASST_INSTRMNT_Table = None # FNNCL_ASST_INSTRMNT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	FNNCL_ASST_INSTRMNT_DRVD_DT_Table = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	LN_EXCLDNG_RPRCHS_AGRMNT_Table = None # LN_EXCLDNG_RPRCHS_AGRMNT
	OTHR_LN_Table = None # OTHR_LN
	OTHR_LN_DBTR_ASSGNMNT_Table = None # OTHR_LN_DBTR_ASSGNMNT
	INSTRMNT_Table = None
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	Other_loanss = []# Other_Loans[]

	@lineage(dependencies={"OTHR_LN_DBTR_ASSGNMNT.MN_DBTR_INDCTR",
		"OTHR_LN_DBTR_ASSGNMNT.Other_loan_has_Debtor_s_via_Other_loan_Loan_debtor_assignment",
		"OTHR_LN_DBTR_ASSGNMNT.Loan_debtor_is_obliged_to_pay_Other_loan_s_via_Other_loan_Debtor_assignment",
		"PRTY_RL.Party_acts_in_Party_role",
		"INSTRMNT.Instrument_type_by_product_delegate",
		"Instrument_type_by_product.Instrument_type_by_product_uniqueID",
		"OTHR_LN.Instrument_type_by_product_uniqueID",
		"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.Balance_sheet_recognised_financial_asset_instrument_type_delegate",
		"Balance_sheet_recognised_financial_asset_instrument_type.blnc_sht_rcgnsd_fnncl_asst_instrmnt_ifrs",
		"FNNCL_ASST_INSTRMNT.Financial_asset_instrument_has_Financial_asset_instrument_derived_data",
		"FNNCL_ASST_INSTRMNT.Financial_asset_instrument_type_delegate",
		"FNNCL_ASST_INSTRMNT.Instrument_acts_in_Instrument_role_s"})
	def calc_Other_loanss(self) :
		items = [] # Other_Loans[]
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations

		
		for loan in self.LN_EXCLDNG_RPRCHS_AGRMNT_Table:
			if loan.LN_TYP == '1022':
				other_loan = loan.Loan_type_delegate
				new_item = Other_loans() 
				new_item.LN_EXCLDNG_RPRCHS_AGRMNT = loan
				for debtor in  self.OTHR_LN_DBTR_ASSGNMNT_Table:
					if debtor.Other_loan_has_Debtor_s_via_Other_loan_Loan_debtor_assignment.Loan_type_uniqueID == other_loan.Loan_type_uniqueID:
						new_item.OTHR_LN_DBTR_ASSGNMNT = debtor	
						new_item.PRTY = debtor.Loan_debtor_is_obliged_to_pay_Other_loan_s_via_Other_loan_Loan_debtor_assignment.Party_acts_in_Party_role
						party_type = new_item.PRTY.Party_type_delegate
						if party_type and party_type.lgl_prsn:
							if party_type.lgl_prsn.orgnstn:
								if party_type.lgl_prsn.orgnstn.Organisation_type_delegate:
									if party_type.lgl_prsn.orgnstn.Organisation_type_delegate.intrntnl_orgnstn_gnrl_gvnmnt:
										if party_type.lgl_prsn.orgnstn.Organisation_type_delegate.intrntnl_orgnstn_gnrl_gvnmnt.intrntnl_orgnstn:
											new_item.INTRNTNL_ORGNSTN = party_type.lgl_prsn.orgnstn.Organisation_type_delegate.intrntnl_orgnstn_gnrl_gvnmnt.intrntnl_orgnstn
						
				the_instrument = None		
				for instrument in self.INSTRMNT_Table:
					if instrument.Instrument_type_by_product_delegate.Instrument_type_by_product_uniqueID == loan.Instrument_type_by_product_uniqueID:
						the_instrument = instrument
						break
				
				if the_instrument is not None:
					for instrument_rl in self.FNNCL_ASST_INSTRMNT_Table:
						if instrument_rl.Instrument_acts_in_Instrument_role_s == the_instrument:
							new_item.FNNCL_ASST_INSTRMNT = instrument_rl
							new_item.FNNCL_ASST_INSTRMNT_DRVD_DT = instrument_rl.Financial_asset_instrument_has_Financial_asset_instrument_derived_data
							Financial_asset_instrument_type_delegate = instrument_rl.Financial_asset_instrument_type_delegate
							
							if Financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt:
								new_item.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT = Financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt
								Balance_sheet_recognised_financial_asset_instrument_type_delegate = new_item.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.Balance_sheet_recognised_financial_asset_instrument_type_delegate
								if Balance_sheet_recognised_financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt_ifrs:
									new_item.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS = Balance_sheet_recognised_financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt_ifrs
							break

							
				items.append(new_item)
		return items
	
	def init(self):
		Orchestration().init(self)
		self.Other_loanss = []
		self.Other_loanss.extend(self.calc_Other_loanss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_IFRS_Table = None # LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_IFRS
	INTRNTNL_ORGNSTN_Table = None # INTRNTNL_ORGNSTN
	ISIN_SCRTY_Table = None # ISIN_SCRTY
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT
	PRTY_Table = None # PRTY
	SCRTY_ISSR_ASSGNMNT_Table = None # SCRTY_ISSR_ASSGNMNT
	Non_Negotiable_bondss = []# Non_Negotiable_bonds[]
	def calc_Non_Negotiable_bondss(self) :
		items = [] # Non_Negotiable_bonds[]
		for long_security in self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table:
			if long_security.lng_dbt_scrty_pstn_prdntl_prtfl_assgnmnt_accntng_clssfctn_fnncl_assts_assgnmnt:
				new_item = Non_Negotiable_bonds()	
				new_item.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = long_security
				new_item.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT = long_security.Long_security_position_Prudential_Portfolio_assignment_Accounting_classification_for_financial_assets_assignment_may_have_Long_security_position_Prudential_Portfolio_assignment_Accounting_classification_for_financial_assets_assignment_derived_data
				the_security_assignment = long_security.Long_security_position_Prudential_portfolio_assignment_is_assigned_to_Accounting_classification_s_for_financial_asset_via_Long_security_position_Prudential_Portfolio_assignment_Accounting_classification_for_financial_assets_assignment
				the_lng_scrty_pstn = the_security_assignment.Long_security_position_is_assigned_to_Prudential_portfolio_s_via_Long_security_position_Prudential_portfolio_assignment
				#go through scrty_postns until the Security_position_type_delegate is the long security_position
				the_scrty_pstn = None
				for scrty_postn in self.SCRTY_PSTN_Table:
					if scrty_postn.Security_position_type_delegate.Security_position_type_uniqueID  == the_lng_scrty_pstn.Security_position_type_uniqueID:
							the_scrty_pstn = scrty_postn

				the_scrty = None
				if the_scrty_pstn is not None:
					the_scrty = the_scrty_pstn.Security_is_involved_in_Security_position
				
				issuer_rl = the_scrty.Security_and_exchange_tradable_derivative_is_issued_by_Issuer_via_Security_Issuer_assignment
				new_item.SCRTY_ISSR_ASSGNMNT = issuer_rl
				issuer = issuer_rl.Issuer_issues_Security_or_Exchange_tradable_derivative_s_via_Security_Issuer_assignment
				issuer_prty = issuer.Party_acts_in_Party_role
				new_item.PRTY = issuer_prty
				items.append(new_item)
	
	
	
	
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	SCRTY_PSTN_Table = None # SCRTY_PSTN
	ENTTY_RL_Table = None # ENTTY_RL
	Non_Negotiable_bondss = []# Non_Negotiable_bonds[]
	def calc_Non_Negotiable_bondss(self) :
		items = [] # Non_Negotiable_bonds[
		for long_Security_accntng_classification in self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table:
			long_Security_assignment = long_Security_accntng_classification.theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
			scrty_position = long_Security_assignment.theSCRTY_PSTN
			scrty_exchng_trdbl_drvtv = scrty_position.theSCRTY_EXCHNG_TRDBL_DRVTV
			entty_rl = scrty_position.theENTTY_RL
			prty = entty_rl.thePRTY
			new_item = Non_Negotiable_bonds()
			new_item.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = long_Security_accntng_classification
			new_item.PRTY = prty
			new_item.SCRTY_EXCHNG_TRDBL_DRVTV = scrty_exchng_trdbl_drvtv
			negotiable = scrty_exchng_trdbl_drvtv.NGTBL_SCRTY_INDCTR
			# only add if not a negotiable security
			if negotiable == '2':
				items.append(new_item)
		return items
	def init(self):
		Orchestration().init(self)
		self.Non_Negotiable_bondss = []
		self.Non_Negotiable_bondss.extend(self.calc_Non_Negotiable_bondss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Credit_card_debt_Table:
	PRTY_Table = None # PRTY
	FNNCL_ASST_INSTRMNT_DRVD_DT_Table = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	INTRNTNL_ORGNSTN_Table = None # INTRNTNL_ORGNSTN
	FNNCL_ASST_INSTRMNT_Table = None # FNNCL_ASST_INSTRMNT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	LN_EXCLDNG_RPRCHS_AGRMNT_Table = None # LN_EXCLDNG_RPRCHS_AGRMNT
	CRDT_CRD_DBT_DBTR_ASSGNMNT_Table = None # CRDT_CRD_DBT_DBTR_ASSGNMNT
	CRDT_CRD_DBT_Table = None # CRDT_CRD_DBT
	Credit_card_debts = []# Credit_card_debt[]
	def calc_Credit_card_debts(self) :
		items = [] # Other_Loans[]
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations		
		for ln in self.LN_EXCLDNG_RPRCHS_AGRMNT_Table:
			if ln.LN_TYP == '51':
				credit_card_debt = ln.Loan_type_delegate
				new_item = Credit_card_debt() 
				new_item.LN_EXCLDNG_RPRCHS_AGRMNT = ln
				for debtor in  self.CRDT_CRD_DBT_DBTR_ASSGNMNT_Table:
					if debtor.Credit_card_debt_has_Debtor_via_Credit_card_debt_Loan_debtor_assignment.Loan_type_uniqueID == credit_card_debt.Loan_type_uniqueID:
						new_item.CRDT_CRD_DBT_DBTR_ASSGNMNT = debtor
						if debtor.Loan_debtor_is_obliged_to_pay_Credit_card_debt_Loan_debtor_assignment.Loan_debtor_is_obliged_to_pay_Other_loan_s_via_Other_loan_Loan_debtor_assignment:
							new_item.PRTY = debtor.Loan_debtor_is_obliged_to_pay_Credit_card_debt_Loan_debtor_assignment.Loan_debtor_is_obliged_to_pay_Other_loan_s_via_Other_loan_Loan_debtor_assignment.Party_acts_in_Party_role
							party_type = new_item.PRTY.Party_type_delegate
							if party_type and party_type.lgl_prsn:
								if party_type.lgl_prsn.orgnstn:
									if party_type.lgl_prsn.orgnstn.Organisation_type_delegate:
										if party_type.lgl_prsn.orgnstn.Organisation_type_delegate.intrntnl_orgnstn_gnrl_gvnmnt:
											if party_type.lgl_prsn.orgnstn.Organisation_type_delegate.intrntnl_orgnstn_gnrl_gvnmnt.intrntnl_orgnstn:
												new_item.INTRNTNL_ORGNSTN = party_type.lgl_prsn.orgnstn.Organisation_type_delegate.intrntnl_orgnstn_gnrl_gvnmnt.intrntnl_orgnstn
						
				the_instrument = None		
				for instrument in self.INSTRMNT_Table:
					if instrument.Instrument_type_by_product_delegate.Instrument_type_by_product_uniqueID == ln.Instrument_type_by_product_uniqueID:
						the_instrument = instrument
						break
				
				if the_instrument is not None:
					for instrument_rl in self.FNNCL_ASST_INSTRMNT_Table:
						if instrument_rl.Instrument_acts_in_Instrument_role_s == the_instrument:
							new_item.FNNCL_ASST_INSTRMNT = instrument_rl
							new_item.FNNCL_ASST_INSTRMNT_DRVD_DT = instrument_rl.Financial_asset_instrument_has_Financial_asset_instrument_derived_data
							Financial_asset_instrument_type_delegate = instrument_rl.Financial_asset_instrument_type_delegate
							
							if Financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt:
								new_item.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT = Financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt
								Balance_sheet_recognised_financial_asset_instrument_type_delegate = new_item.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.Balance_sheet_recognised_financial_asset_instrument_type_delegate
								if Balance_sheet_recognised_financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt_ifrs:
									new_item.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS = Balance_sheet_recognised_financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt_ifrs
							break
							
				items.append(new_item)
		return items
	def init(self):
		Orchestration().init(self)
		self.Credit_card_debts = []
		self.Credit_card_debts.extend(self.calc_Credit_card_debts())
		CSVConverter.persist_object_as_csv(self,True)
		return None

