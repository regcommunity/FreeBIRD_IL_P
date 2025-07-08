from django.db import models
from pybirdai.annotations.decorators import lineage

class INSTRMNT_RL(models.Model):

    @property
    @lineage(dependencies={'INSTRMNT_RL.PRFRMNG_STTS', 'INSTRMNT_RL.ACCNTNG_CLSSFCTN', 'INSTRMNT_RL.ACCMLTD_IMPRMNT', 'INSTRMNT_RL.CRRYNG_AMNT', 'INSTRMNT_RL.IMPRMNT_STTS', 'INSTRMNT_RL.ACCMLTD_CHNGS_FV', 'INSTRMNT_RL.FV', 'INSTRMNT_RL.GNRL_ALLWNCS_BNK_RSK', 'INSTRMNT_RL.GNRL_ALLWNCS_CRDT_RSK', 'INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR'})
    def GRSS_CRRYNG_AMNT(self):
        accntng_clssfctn = None
        accmltd_imprmnt = 0
        accmltd_chngs_fv_cr = 0
        crryng_amnt  = 0 			
        fv = 0
        gnrl_allwncs_bnk_rsk = 0
        gnrl_allwncs_crdt_rsk = 0
        prfrmng_stts = self.PRFRMNG_STTS
        imprmnt_stts = self.IMPRMNT_STTS
        sbjct_imprmnt_idctr = self.SBJCT_IMPRMNT_INDCTR


		# "10":"Non_balance_sheet_recognised_financial_asset_instrument",
		# "34":"Balance_sheet_recognised_financial_asset_instrument_according_to_national_general_accepted_accounting_principles_nGAAP",
		# "35":"Balance_sheet_recognised_financial_asset_instrument_according_to_International_Financial_Reporting_Standard_IFRS",

        if (self.TYP_INSTRMNT_RL == '10') or \
            (self.TYP_INSTRMNT_RL == '34') or \
            (self.TYP_INSTRMNT_RL == '35'):
            accntng_clssfctn = self.ACCNTNG_CLSSFCTN
            accmltd_imprmnt = self.ACCMLTD_IMPRMNT
            crryng_amnt  = self.CRRYNG_AMNT
            imprmnt_stts = self.IMPRMNT_STTS
	 			
	 	# for some reason 	BLNC_SHT_RCGNSD_FNCL_ASST_INSTRMNT_FR_VL_TYP is a boolean, 
		# and we would expect it to be a domain with 2 members, need to investigate this.
		# 	
        if (self.BLNC_SHT_RCGNSD_FNCL_ASST_INSTRMNT_FR_VL_TYP):
            accmltd_chngs_fv_cr = self.ACCMLTD_CHNGS_FV
            fv = self.FV 

        if (self.TYP_INSTRMNT_RL == '34'):	 		
            gnrl_allwncs_bnk_rsk = self.GNRL_ALLWNCS_BNK_RSK
            gnrl_allwncs_crdt_rsk = self.GNRL_ALLWNCS_CRDT_RSK


        return_grss_crryng_amnt = 0
		# ACCNTNG_CLSSFCTN_INPT_domain = {		"0":"Not_applicable",
		# "14":"IFRS_Cash_balances_at_central_banks_and_other_demand_deposits_Cash_balances_at_central_banks_and_other_demand_deposits_in_accordance_with_IFRS",
		# "2":"IFRS_Financial_assets_held_for_trading_Financial_assets_held_for_trading_in_accordance_with_IFRS",
		# "21":"IFRS_Financial_liabilities_measured_at_amortised_cost_Financial_liabilities_measured_at_amortised_cost_in_accordance_with_IFRS",
		# "23":"IFRS_Financial_liabilities_held_for_trading_Financial_liabilities_held_for_trading_in_accordance_with_IFRS",
		# "25":"IFRS_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		# "3":"nGAAP_Trading_Financial_assets_Trading_financial_assets_in_accordance_with_national_GAAP",
		# "31":"nGAAP_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_accordance_with_national_GAAP_based_on_BAD",
		# "33":"nGAAP_Trading_financial_liabilities_Trading_financial_liabilities_in_accordance_with_national_GAAP_based_on_BAD",
		# "35":"nGAAP_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_nationa_GAAP_based_on_BAD",
		# "4":"IFRS_Financial_assets_designated_at_fair_value_through_profit_or_loss_Financial_assets_measured_at_fair_value_through_profit_and_loss_and_designated_as_such_upon_initial_recognition_or_subsequently_in_accordance_with_IFRS_except_those_classified_as_financial_assets_held_for_trading",
		# "41":"IFRS_Non_trading_financial_assets_mandatorily_at_fair_value_through_profit_or_loss_Non_trading_financial_assets_mandatorily_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		# "45":"nGAAP_Cash_balances_at_central_banks_and_other_demand_deposits_Cash_balances_at_central_banks_and_other_demand_deposits_in_accordance_with_national_GAAP",
		# "47":"nGAAP_Financial_assets_designated_at_fair_value_through_profit_or_loss_Financial_assets_designated_at_fair_value_through_profit_or_loss_in_accordance_with_national_GAAP",
		# "6":"IFRS_Financial_assets_at_amortised_cost_Financial_assets_measured_at_amortised_cost_in_accordance_with_IFRS",
		# "64":"nGAAP_financial_assets_at_fair_value_or_strict_LOCOM",
		# "7":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_fair_value_through_profit_or_loss_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_in_accordance_with_national_GAAP",
		# "711":"Accounting_portfolios_for_financial_assets_other_than_classified_as_held_for_sale_excluding_financial_assets_held_for_trading_trading_financial_assets_and_cash_and_cash_balances_at_central_banks_and_other_demand_deposits",
		# "73":"nGAAP_Other_non_trading_non_derivative_financial_assets_LOCOM_nGAAP_Other_non_trading_non_derivative_financial_assets_at_LOCOM",
		# "74":"nGAAP_Other_non_trading_non_derivative_financial_assets_Other_than_LOCOM",
		# "76":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_LOCOM_nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_at_LOCOM",
		# "77":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_Other_than_LOCOM",
		# "8":"IFRS_Financial_assets_at_fair_value_through_other_comprehensive_income_Financial_assets_measured_at_fair_value_through_other_comprehensive_income_due_to_business_model_and_cash_flows_characteristics_in_accordance_with_IFRS",
		# "83":"Investments_in_subsidiaries_joint_ventures_and_associates",
		# "85":"nGAAP_Accounting_portfolios_for_trading_financial_instruments_Cost_based_method_or_LOCOM",
		# "9":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_in_accordance_with_national_GAAP",
		# "90":"Under_IFRS_9_impairment_Off_balance_sheet_accounting_classification_under_IFRS_9_impairment",
		# "911":"Measured_under_IAS_37_Off_balance_sheet_accounting_classification_measured_under_IAS_37",
		# "912":"Measured_under_IFRS_4_Off_balance_sheet_accounting_classification_measured_under_IFRS_4",
		# "92":"Measured_at_fair_value_through_profit_or_loss_Off_balance_sheet_accounting_classification_IFRS_9_fair_valued_commitments_and_financial_guarantees",
		# "93":"Under_nGAAP_Off_balance_sheet_accounting_classification_measured_under_nGAAP_based_on_BAD",

        match accntng_clssfctn:
            case '4' | \
                    '41' | \
                    '47' | \
                    '7' :
				  
				# PRFRMNG_STTS_INPT_domain = {		"0":"Not_applicable",
				# "1":"Non_performing",
				# "11":"Performing",
				# }
                match prfrmng_stts:
                    case '11':
                        return_grss_crryng_amnt = fv
                    case '1':
                        return_grss_crryng_amnt = fv + accmltd_chngs_fv_cr
                    case _ : return_grss_crryng_amnt = 0

            case ('6' | '8' | '9'):
                return_grss_crryng_amnt = crryng_amnt - accmltd_imprmnt
            case ('77'):
				# IMPRMNT_STTS_domain = {		"211":"General_allowances_for_credit_risk_GAAP",
				# "212":"General_allowances_for_banking_risk_GAAP",
				# "23":"Stage_1_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_12_month_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
				# "24":"Stage_2_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
				# "25":"Stage_3_IFRS_To_be_used_if_the_instrument_is_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
				# "26":"Specific_allowances_GAAP_To_be_used_if_the_instrument_is_subject_to_impairment_in_accordance_with_an_applied_accounting_standard_other_than_IFRS_9_and_specific_loss_allowances_are_raised_irrespective_of_whether_these_allowances_are_individually_or_collectively_assessed_impaired",
				# "27":"Purchased_or_originated_credit_impaired_instruments_POCI_IFRS",
                match imprmnt_stts:
                    case '26' :
                        return_grss_crryng_amnt = crryng_amnt - accmltd_imprmnt
                    case '211':
                        return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_crdt_rsk
                    case '212':
                        return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_bnk_rsk
                    case _ : 
                        return_grss_crryng_amnt = 0
	 			
	 			
            case ('9'):
                match sbjct_imprmnt_idctr:
                    #	SBJCT_IMPRMNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
                    # "1":"Subject_to_impairment",
                    # "2":"Not_subject_to_impairment",
                    case '1':
                        match prfrmng_stts:
                            case '26':
                                return_grss_crryng_amnt = crryng_amnt - accmltd_imprmnt
                            case '211':
                                return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_crdt_rsk
                            case '212':
                                return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_bnk_rsk
                            case _ : 
                                return_grss_crryng_amnt = 0

                    case '2':
                        match prfrmng_stts:
                            case '11':
                                return_grss_crryng_amnt = fv
                            case '1':
                                return_grss_crryng_amnt = fv + accmltd_chngs_fv_cr
                            case _ : 
                                return_grss_crryng_amnt = 0
                    case _ : 
                        return_grss_crryng_amnt = 0
                        
                    
            case ('76' | '73'):	
                return_grss_crryng_amnt = crryng_amnt
            case '74':		
                return_grss_crryng_amnt = crryng_amnt + accmltd_imprmnt
            case ('2' | '3') :
                return_grss_crryng_amnt = fv
            case _ : 
                return_grss_crryng_amnt = 0		
                    
        return return_grss_crryng_amnt

    class Meta:
        pass