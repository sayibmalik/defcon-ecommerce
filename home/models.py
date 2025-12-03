# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountAccount(models.Model):
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Account Currency')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountaccount_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    account_type = models.CharField(db_comment='Type')
    name = models.JSONField(db_comment='Account Name')
    code_store = models.JSONField(blank=True, null=True, db_comment='Code Store')
    note = models.TextField(blank=True, null=True, db_comment='Internal Notes')
    deprecated = models.BooleanField(blank=True, null=True, db_comment='Deprecated')
    reconcile = models.BooleanField(blank=True, null=True, db_comment='Allow Reconciliation')
    non_trade = models.BooleanField(blank=True, null=True, db_comment='Non Trade')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    cash_flow_type = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING, db_column='cash_flow_type', blank=True, null=True, db_comment='Cash Flow type')

    class Meta:
        managed = False
        db_table = 'account_account'
        db_table_comment = 'Account'


class AccountAccountAccountJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_account_id', 'account_journal_id')
    account_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_account_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_account AND account_journal'


class AccountAccountAccountMergeWizardRel(models.Model):
    pk = models.CompositePrimaryKey('account_merge_wizard_id', 'account_account_id')
    account_merge_wizard = models.ForeignKey('AccountMergeWizard', models.DO_NOTHING)
    account_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_account_merge_wizard_rel'
        db_table_comment = 'RELATION BETWEEN account_merge_wizard AND account_account'


class AccountAccountAccountTag(models.Model):
    pk = models.CompositePrimaryKey('account_account_id', 'account_account_tag_id')
    account_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    account_account_tag = models.ForeignKey('AccountAccountTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_account_tag'
        db_table_comment = 'RELATION BETWEEN account_account AND account_account_tag'


class AccountAccountFinancialReport(models.Model):
    pk = models.CompositePrimaryKey('report_line_id', 'account_id')
    report_line = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_financial_report'
        db_table_comment = 'RELATION BETWEEN account_financial_report AND account_account'


class AccountAccountResCompanyRel(models.Model):
    pk = models.CompositePrimaryKey('account_account_id', 'res_company_id')
    account_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    res_company = models.ForeignKey('ResCompany', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_res_company_rel'
        db_table_comment = 'RELATION BETWEEN account_account AND res_company'


class AccountAccountTag(models.Model):
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountaccounttag_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    applicability = models.CharField(db_comment='Applicability')
    name = models.JSONField(db_comment='Tag Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    tax_negate = models.BooleanField(blank=True, null=True, db_comment='Negate Tax Balance')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_account_tag'
        unique_together = (('name', 'applicability', 'country'),)
        db_table_comment = 'Account Tag'


class AccountAccountTagAccountMoveLineRel(models.Model):
    pk = models.CompositePrimaryKey('account_move_line_id', 'account_account_tag_id')
    account_move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_move_line_rel'
        db_table_comment = 'RELATION BETWEEN account_move_line AND account_account_tag'


class AccountAccountTagAccountTaxRepartitionLineRel(models.Model):
    pk = models.CompositePrimaryKey('account_tax_repartition_line_id', 'account_account_tag_id')
    account_tax_repartition_line = models.ForeignKey('AccountTaxRepartitionLine', models.DO_NOTHING)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_tax_repartition_line_rel'
        db_table_comment = 'RELATION BETWEEN account_tax_repartition_line AND account_account_tag'


class AccountAccountTagProductTemplateRel(models.Model):
    pk = models.CompositePrimaryKey('product_template_id', 'account_account_tag_id')
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_product_template_rel'
        db_table_comment = 'RELATION BETWEEN product_template AND account_account_tag'


class AccountAccountTaxDefaultRel(models.Model):
    pk = models.CompositePrimaryKey('account_id', 'tax_id')
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tax_default_rel'
        db_table_comment = 'RELATION BETWEEN account_account AND account_tax'


class AccountAccountType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountaccounttype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    type = models.CharField(db_comment='Type')
    name = models.JSONField(db_comment='Account Type')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_account_type'
        db_table_comment = 'account.account.type'


class AccountAccruedOrdersWizard(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, db_comment='Journal')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Company Currency')
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, db_comment='Accrual Account')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountaccruedorderswizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    date = models.DateField(db_comment='Date')
    reversal_date = models.DateField(db_comment='Reversal Date')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_accrued_orders_wizard'
        db_table_comment = 'Accrued Orders Wizard'


class AccountAgedTrailReportSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey('AccountReport', models.DO_NOTHING)
    sub_report = models.ForeignKey('AccountReport', models.DO_NOTHING, related_name='accountagedtrailreportsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_aged_trail_report_section_rel'
        db_table_comment = 'RELATION BETWEEN account_aged_trial_balance AND account_report'


class AccountAgedTrialBalance(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey('AccountReport', models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountagedtrialbalance_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    period_length = models.IntegerField(db_comment='Period Length (days)')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    result_selection = models.CharField(db_comment="Partner's")
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    name = models.JSONField(db_comment='Account Aged Trial balance Report')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance'
        db_table_comment = 'Account Aged Trial balance Report'


class AccountAgedTrialBalanceAccountJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_aged_trial_balance_id', 'account_journal_id')
    account_aged_trial_balance = models.ForeignKey(AccountAgedTrialBalance, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance_account_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_aged_trial_balance AND account_journal'


class AccountAnalyticAccount(models.Model):
    plan = models.ForeignKey('AccountAnalyticPlan', models.DO_NOTHING, db_comment='Plan')
    root_plan = models.ForeignKey('AccountAnalyticPlan', models.DO_NOTHING, related_name='accountanalyticaccount_root_plan_set', blank=True, null=True, db_comment='Root Plan')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Customer')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountanalyticaccount_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code = models.CharField(blank=True, null=True, db_comment='Reference')
    name = models.JSONField(db_comment='Analytic Account')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_analytic_account'
        db_table_comment = 'Analytic Account'


class AccountAnalyticAccountMrpBomRel(models.Model):
    pk = models.CompositePrimaryKey('account_analytic_account_id', 'mrp_bom_id')
    account_analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    mrp_bom = models.ForeignKey('MrpBom', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_account_mrp_bom_rel'
        db_table_comment = 'RELATION BETWEEN account_analytic_account AND mrp_bom'


class AccountAnalyticAccountMrpProductionRel(models.Model):
    pk = models.CompositePrimaryKey('account_analytic_account_id', 'mrp_production_id')
    account_analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    mrp_production = models.ForeignKey('MrpProduction', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_account_mrp_production_rel'
        db_table_comment = 'RELATION BETWEEN account_analytic_account AND mrp_production'


class AccountAnalyticAccountMrpWorkcenterRel(models.Model):
    pk = models.CompositePrimaryKey('account_analytic_account_id', 'mrp_workcenter_id')
    account_analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    mrp_workcenter = models.ForeignKey('MrpWorkcenter', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_account_mrp_workcenter_rel'
        db_table_comment = 'RELATION BETWEEN account_analytic_account AND mrp_workcenter'


class AccountAnalyticApplicability(models.Model):
    analytic_plan = models.ForeignKey('AccountAnalyticPlan', models.DO_NOTHING, blank=True, null=True, db_comment='Analytic Plan')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountanalyticapplicability_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    business_domain = models.CharField(db_comment='Domain')
    applicability = models.CharField(db_comment='Applicability')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    product_categ = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True, db_comment='Product Category')
    account_prefix = models.CharField(blank=True, null=True, db_comment='Financial Accounts Prefixes')

    class Meta:
        managed = False
        db_table = 'account_analytic_applicability'
        db_table_comment = "Analytic Plan's Applicabilities"


class AccountAnalyticDistributionModel(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    partner_category = models.ForeignKey('ResPartnerCategory', models.DO_NOTHING, blank=True, null=True, db_comment='Partner Category')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountanalyticdistributionmodel_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    analytic_distribution = models.JSONField(blank=True, null=True, db_comment='Analytic Distribution')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    product_categ = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True, db_comment='Product Category')
    account_prefix = models.CharField(blank=True, null=True, db_comment='Accounts Prefix')

    class Meta:
        managed = False
        db_table = 'account_analytic_distribution_model'
        db_table_comment = 'Analytic Distribution Model'


class AccountAnalyticLine(models.Model):
    account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Project Account')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True, db_comment='Unit of Measure')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='User')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='accountanalyticline_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountanalyticline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Description')
    category = models.CharField(blank=True, null=True, db_comment='Category')
    date = models.DateField(db_comment='Date')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Amount')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    unit_amount = models.FloatField(blank=True, null=True, db_comment='Quantity')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    general_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Financial Account')
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True, db_comment='Financial Journal')
    move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING, blank=True, null=True, db_comment='Journal Item')
    code = models.CharField(max_length=8, blank=True, null=True, db_comment='Code')
    ref = models.CharField(blank=True, null=True, db_comment='Ref.')
    so_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, db_column='so_line', blank=True, null=True, db_comment='Sales Order Item')

    class Meta:
        managed = False
        db_table = 'account_analytic_line'
        db_table_comment = 'Analytic Line'


class AccountAnalyticLineStockMoveRel(models.Model):
    pk = models.CompositePrimaryKey('stock_move_id', 'account_analytic_line_id')
    stock_move = models.ForeignKey('StockMove', models.DO_NOTHING)
    account_analytic_line = models.ForeignKey(AccountAnalyticLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_line_stock_move_rel'
        db_table_comment = 'RELATION BETWEEN stock_move AND account_analytic_line'


class AccountAnalyticPlan(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent')
    color = models.IntegerField(blank=True, null=True, db_comment='Color')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountanalyticplan_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    parent_path = models.CharField(blank=True, null=True, db_comment='Parent Path')
    complete_name = models.CharField(blank=True, null=True, db_comment='Complete Name')
    name = models.JSONField(db_comment='Name')
    default_applicability = models.JSONField(blank=True, null=True, db_comment='Default Applicability')
    description = models.TextField(blank=True, null=True, db_comment='Description')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_analytic_plan'
        db_table_comment = 'Analytic Plans'


class AccountAssetAsset(models.Model):
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, db_comment='Currency')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    category = models.ForeignKey('AccountAssetCategory', models.DO_NOTHING, db_comment='Category')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    method_number = models.IntegerField(blank=True, null=True, db_comment='Number of Depreciations')
    method_period = models.IntegerField(db_comment='Number of Months in a Period')
    invoice = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True, db_comment='Invoice')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountassetasset_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Asset Name')
    code = models.CharField(max_length=32, blank=True, null=True, db_comment='Reference')
    state = models.CharField(db_comment='Status')
    method = models.CharField(db_comment='Computation Method')
    method_time = models.CharField(db_comment='Time Method')
    date = models.DateField(db_comment='Date')
    method_end = models.DateField(blank=True, null=True, db_comment='Ending Date')
    note = models.TextField(blank=True, null=True, db_comment='Note')
    value = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Gross Value')
    salvage_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Salvage Value')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    prorata = models.BooleanField(blank=True, null=True, db_comment='Prorata Temporis')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    method_progress_factor = models.FloatField(blank=True, null=True, db_comment='Degressive Factor')

    class Meta:
        managed = False
        db_table = 'account_asset_asset'
        db_table_comment = 'Asset/Revenue Recognition'


class AccountAssetCategory(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Analytic Account')
    account_asset = models.ForeignKey(AccountAccount, models.DO_NOTHING, db_comment='Asset Account')
    account_depreciation = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='accountassetcategory_account_depreciation_set', db_comment='Depreciation Account')
    account_depreciation_expense = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='accountassetcategory_account_depreciation_expense_set', db_comment='Expense Account')
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, db_comment='Journal')
    method_number = models.IntegerField(blank=True, null=True, db_comment='Number of Depreciations')
    method_period = models.IntegerField(db_comment='Period Length')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountassetcategory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Asset Type')
    method = models.CharField(db_comment='Computation Method')
    method_time = models.CharField(db_comment='Time Method')
    type = models.CharField(db_comment='Type')
    method_end = models.DateField(blank=True, null=True, db_comment='Ending date')
    price = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Price')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    prorata = models.BooleanField(blank=True, null=True, db_comment='Prorata Temporis')
    open_asset = models.BooleanField(blank=True, null=True, db_comment='Auto-confirm Assets')
    group_entries = models.BooleanField(blank=True, null=True, db_comment='Group Journal Entries')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    method_progress_factor = models.FloatField(blank=True, null=True, db_comment='Degressive Factor')

    class Meta:
        managed = False
        db_table = 'account_asset_category'
        db_table_comment = 'Asset category'


class AccountAssetDepreciationLine(models.Model):
    sequence = models.IntegerField(db_comment='Sequence')
    asset = models.ForeignKey(AccountAssetAsset, models.DO_NOTHING, db_comment='Asset')
    move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True, db_comment='Depreciation Entry')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountassetdepreciationline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Depreciation Name')
    depreciation_date = models.DateField(blank=True, null=True, db_comment='Depreciation Date')
    move_check = models.BooleanField(blank=True, null=True, db_comment='Linked')
    move_posted_check = models.BooleanField(blank=True, null=True, db_comment='Posted')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    amount = models.FloatField(db_comment='Current Depreciation')
    remaining_value = models.FloatField(db_comment='Next Period Depreciation')
    depreciated_value = models.FloatField(db_comment='Cumulative Depreciation')

    class Meta:
        managed = False
        db_table = 'account_asset_depreciation_line'
        db_table_comment = 'Asset depreciation line'


class AccountAutomaticEntryWizard(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    destination_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='To')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountautomaticentrywizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    action = models.CharField(db_comment='Action')
    account_type = models.CharField(blank=True, null=True, db_comment='Account Type')
    date = models.DateField(db_comment='Date')
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total Amount')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    percentage = models.FloatField(blank=True, null=True, db_comment='Percentage')

    class Meta:
        managed = False
        db_table = 'account_automatic_entry_wizard'
        db_table_comment = 'Create Automatic Entries'


class AccountAutomaticEntryWizardAccountMoveLineRel(models.Model):
    pk = models.CompositePrimaryKey('account_automatic_entry_wizard_id', 'account_move_line_id')
    account_automatic_entry_wizard = models.ForeignKey(AccountAutomaticEntryWizard, models.DO_NOTHING)
    account_move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_automatic_entry_wizard_account_move_line_rel'
        db_table_comment = 'RELATION BETWEEN account_automatic_entry_wizard AND account_move_line'


class AccountAutopostBillsWizard(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    nb_unmodified_bills = models.IntegerField(blank=True, null=True, db_comment='Number of bills previously unmodified from this partner')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountautopostbillswizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_autopost_bills_wizard'
        db_table_comment = 'Autopost Bills Wizard'


class AccountBalanceReport(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey('AccountReport', models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountbalancereport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    display_account = models.CharField(db_comment='Display Accounts')
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    name = models.JSONField(db_comment='Trial Balance')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_balance_report'
        db_table_comment = 'Trial Balance Report'


class AccountBalanceReportJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_id', 'journal_id')
    account = models.ForeignKey(AccountBalanceReport, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_balance_report_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_balance_report AND account_journal'


class AccountBalanceReportSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey('AccountReport', models.DO_NOTHING)
    sub_report = models.ForeignKey('AccountReport', models.DO_NOTHING, related_name='accountbalancereportsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_balance_report_section_rel'
        db_table_comment = 'RELATION BETWEEN account_balance_report AND account_report'


class AccountBankBookReport(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountbankbookreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    target_move = models.CharField(db_comment='Target Moves')
    display_account = models.CharField(db_comment='Display Accounts')
    sortby = models.CharField(db_comment='Sort by')
    date_from = models.DateField(db_comment='Start Date')
    date_to = models.DateField(db_comment='End Date')
    initial_balance = models.BooleanField(blank=True, null=True, db_comment='Include Initial Balances')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_bank_book_report'
        db_table_comment = 'Account Bank Book Report'


class AccountBankStatement(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True, db_comment='Journal')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountbankstatement_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Reference')
    reference = models.CharField(blank=True, null=True, db_comment='External Reference')
    first_line_index = models.CharField(blank=True, null=True, db_comment='First Line Index')
    date = models.DateField(blank=True, null=True, db_comment='Date')
    balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Starting Balance')
    balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Computed Balance')
    balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Ending Balance')
    is_complete = models.BooleanField(blank=True, null=True, db_comment='Is Complete')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_bank_statement'
        db_table_comment = 'Bank Statement'


class AccountBankStatementIrAttachmentRel(models.Model):
    pk = models.CompositePrimaryKey('account_bank_statement_id', 'ir_attachment_id')
    account_bank_statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING)
    ir_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_ir_attachment_rel'
        db_table_comment = 'RELATION BETWEEN account_bank_statement AND ir_attachment'


class AccountBankStatementLine(models.Model):
    move = models.ForeignKey('AccountMove', models.DO_NOTHING, db_comment='Journal Entry')
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, db_comment='Journal')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True, db_comment='Statement')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Journal Currency')
    foreign_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name='accountbankstatementline_foreign_currency_set', blank=True, null=True, db_comment='Foreign Currency')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountbankstatementline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    account_number = models.CharField(blank=True, null=True, db_comment='Bank Account Number')
    partner_name = models.CharField(blank=True, null=True, db_comment='Partner Name')
    transaction_type = models.CharField(blank=True, null=True, db_comment='Transaction Type')
    payment_ref = models.CharField(blank=True, null=True, db_comment='Label')
    internal_index = models.CharField(blank=True, null=True, db_comment='Internal Reference')
    transaction_details = models.JSONField(blank=True, null=True, db_comment='Transaction Details')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount')
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount in Currency')
    is_reconciled = models.BooleanField(blank=True, null=True, db_comment='Is Reconciled')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    amount_residual = models.FloatField(blank=True, null=True, db_comment='Residual Amount')
    pos_session = models.ForeignKey('PosSession', models.DO_NOTHING, blank=True, null=True, db_comment='Session')
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Account')
    record_id = models.IntegerField(blank=True, null=True, db_comment='Record')
    lines_widget = models.CharField(blank=True, null=True, db_comment='Lines Widget')
    form_name = models.CharField(blank=True, null=True, db_comment='Form Name')
    bank_state = models.CharField(blank=True, null=True, db_comment='Bank State')
    reconcile_models_widget = models.CharField(blank=True, null=True, db_comment='Reconcile Models Widget')
    analytic_distribution = models.JSONField(blank=True, null=True, db_comment='Analytic Distribution')
    rowdata = models.JSONField(blank=True, null=True, db_comment='RowData')
    matchrowdata = models.JSONField(db_column='matchRowdata', blank=True, null=True, db_comment='MatchRowData')  # Field name made lowercase.
    lines_widget_json = models.JSONField(blank=True, null=True, db_comment='Lines Widget Json')
    form_balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Form Balance')
    employee = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True, db_comment='Employee')

    class Meta:
        managed = False
        db_table = 'account_bank_statement_line'
        db_table_comment = 'Bank Statement Line'


class AccountBankStatementLineAccountTaxRel(models.Model):
    pk = models.CompositePrimaryKey('account_bank_statement_line_id', 'account_tax_id')
    account_bank_statement_line = models.ForeignKey(AccountBankStatementLine, models.DO_NOTHING)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_line_account_tax_rel'
        db_table_comment = 'RELATION BETWEEN account_bank_statement_line AND account_tax'


class AccountBudgetPost(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountbudgetpost_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_budget_post'
        db_table_comment = 'Budgetary Position'


class AccountBudgetRel(models.Model):
    pk = models.CompositePrimaryKey('budget_id', 'account_id')
    budget = models.ForeignKey(AccountBudgetPost, models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_budget_rel'
        db_table_comment = 'RELATION BETWEEN account_budget_post AND account_account'


class AccountCashBookReport(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountcashbookreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    target_move = models.CharField(db_comment='Target Moves')
    display_account = models.CharField(db_comment='Display Accounts')
    sortby = models.CharField(db_comment='Sort by')
    date_from = models.DateField(db_comment='Start Date')
    date_to = models.DateField(db_comment='End Date')
    initial_balance = models.BooleanField(blank=True, null=True, db_comment='Include Initial Balances')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_cash_book_report'
        db_table_comment = 'Account Cash Book Report'


class AccountCashFlowReportSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey('AccountReport', models.DO_NOTHING)
    sub_report = models.ForeignKey('AccountReport', models.DO_NOTHING, related_name='accountcashflowreportsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_cash_flow_report_section_rel'
        db_table_comment = 'RELATION BETWEEN cash_flow_report AND account_report'


class AccountCashRounding(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountcashrounding_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    strategy = models.CharField(db_comment='Rounding Strategy')
    rounding_method = models.CharField(db_comment='Rounding Method')
    name = models.JSONField(db_comment='Name')
    profit_account_id = models.JSONField(blank=True, null=True, db_comment='Profit Account')
    loss_account_id = models.JSONField(blank=True, null=True, db_comment='Loss Account')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    rounding = models.FloatField(db_comment='Rounding Precision')

    class Meta:
        managed = False
        db_table = 'account_cash_rounding'
        db_table_comment = 'Account Cash Rounding'


class AccountCommonAccountReport(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey('AccountReport', models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountcommonaccountreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    display_account = models.CharField(db_comment='Display Accounts')
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    name = models.JSONField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_common_account_report'
        db_table_comment = 'Account Common Account Report'


class AccountCommonAccountReportAccountJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_common_account_report_id', 'account_journal_id')
    account_common_account_report = models.ForeignKey(AccountCommonAccountReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_account_report_account_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_common_account_report AND account_journal'


class AccountCommonJournalReport(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey('AccountReport', models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountcommonjournalreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    name = models.JSONField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    amount_currency = models.BooleanField(blank=True, null=True, db_comment='With Currency')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_common_journal_report'
        db_table_comment = 'Common Journal Report'


class AccountCommonJournalReportAccountJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_common_journal_report_id', 'account_journal_id')
    account_common_journal_report = models.ForeignKey(AccountCommonJournalReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report_account_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_common_journal_report AND account_journal'


class AccountCommonJournalReportSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey('AccountReport', models.DO_NOTHING)
    sub_report = models.ForeignKey('AccountReport', models.DO_NOTHING, related_name='accountcommonjournalreportsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_common_journal_report_section_rel'
        db_table_comment = 'RELATION BETWEEN account_common_journal_report AND account_report'


class AccountCommonParnterReportSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey('AccountReport', models.DO_NOTHING)
    sub_report = models.ForeignKey('AccountReport', models.DO_NOTHING, related_name='accountcommonparnterreportsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_common_parnter_report_section_rel'
        db_table_comment = 'RELATION BETWEEN account_common_partner_report AND account_report'


class AccountCommonPartnerReport(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey('AccountReport', models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountcommonpartnerreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    result_selection = models.CharField(db_comment="Partner's")
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    name = models.JSONField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_common_partner_report'
        db_table_comment = 'Account Common Partner Report'


class AccountCommonPartnerReportAccountJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_common_partner_report_id', 'account_journal_id')
    account_common_partner_report = models.ForeignKey(AccountCommonPartnerReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_partner_report_account_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_common_partner_report AND account_journal'


class AccountCommonPrintReportSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey('AccountReport', models.DO_NOTHING)
    sub_report = models.ForeignKey('AccountReport', models.DO_NOTHING, related_name='accountcommonprintreportsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_common_print_report_section_rel'
        db_table_comment = 'RELATION BETWEEN account_print_journal AND account_report'


class AccountCommonReportSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey('AccountReport', models.DO_NOTHING)
    sub_report = models.ForeignKey('AccountReport', models.DO_NOTHING, related_name='accountcommonreportsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_common_report_section_rel'
        db_table_comment = 'RELATION BETWEEN account_common_account_report AND account_report'


class AccountDayBookReport(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountdaybookreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    target_move = models.CharField(db_comment='Target Moves')
    date_from = models.DateField(db_comment='Start Date')
    date_to = models.DateField(db_comment='End Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_day_book_report'
        db_table_comment = 'Account Day Book Report'


class AccountDayBookReportAccountJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_day_book_report_id', 'account_journal_id')
    account_day_book_report = models.ForeignKey(AccountDayBookReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_day_book_report_account_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_day_book_report AND account_journal'


class AccountDebitNote(models.Model):
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True, db_comment='Use Specific Journal')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountdebitnote_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    reason = models.CharField(blank=True, null=True, db_comment='Reason')
    date = models.DateField(db_comment='Debit Note Date')
    copy_lines = models.BooleanField(blank=True, null=True, db_comment='Copy Lines')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_debit_note'
        db_table_comment = 'Add Debit Note wizard'


class AccountEdiDocument(models.Model):
    move = models.ForeignKey('AccountMove', models.DO_NOTHING, db_comment='Move')
    edi_format = models.ForeignKey('AccountEdiFormat', models.DO_NOTHING, db_comment='Edi Format')
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True, db_comment='Attachment')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountedidocument_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    state = models.CharField(blank=True, null=True, db_comment='State')
    blocking_level = models.CharField(blank=True, null=True, db_comment='Blocking Level')
    error = models.TextField(blank=True, null=True, db_comment='Error')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_edi_document'
        unique_together = (('edi_format', 'move'),)
        db_table_comment = 'Electronic Document for an account.move'


class AccountEdiFormat(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountediformat_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    code = models.CharField(unique=True, db_comment='Code')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_edi_format'
        db_table_comment = 'EDI format'


class AccountEdiFormatAccountJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_journal_id', 'account_edi_format_id')
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    account_edi_format = models.ForeignKey(AccountEdiFormat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_edi_format_account_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_journal AND account_edi_format'


class AccountFinancialReport(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    level = models.IntegerField(blank=True, null=True, db_comment='Level')
    account_report = models.ForeignKey('self', models.DO_NOTHING, related_name='accountfinancialreport_account_report_set', blank=True, null=True, db_comment='Report Value')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountfinancialreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    type = models.CharField(blank=True, null=True, db_comment='Type')
    account_type_ids = models.CharField(blank=True, null=True, db_comment='Type')
    sign = models.CharField(db_comment='Sign on Reports')
    display_detail = models.CharField(blank=True, null=True, db_comment='Display details')
    style_overwrite = models.CharField(blank=True, null=True, db_comment='Financial Report Style')
    name = models.JSONField(db_comment='Report Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_financial_report'
        db_table_comment = 'Account Report'


class AccountFinancialReportSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey('AccountReport', models.DO_NOTHING)
    sub_report = models.ForeignKey('AccountReport', models.DO_NOTHING, related_name='accountfinancialreportsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_financial_report_section_rel'
        db_table_comment = 'RELATION BETWEEN financial_report AND account_report'


class AccountFinancialYearOp(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountfinancialyearop_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_financial_year_op'
        db_table_comment = 'Opening Balance of Financial Year'


class AccountFiscalPosition(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True, db_comment='Country Group')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountfiscalposition_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    zip_from = models.CharField(blank=True, null=True, db_comment='Zip Range From')
    zip_to = models.CharField(blank=True, null=True, db_comment='Zip Range To')
    foreign_vat = models.CharField(blank=True, null=True, db_comment='Foreign Tax ID')
    name = models.JSONField(db_comment='Fiscal Position')
    note = models.JSONField(blank=True, null=True, db_comment='Notes')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    auto_apply = models.BooleanField(blank=True, null=True, db_comment='Detect Automatically')
    vat_required = models.BooleanField(blank=True, null=True, db_comment='VAT required')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_fiscal_position'
        db_table_comment = 'Fiscal Position'


class AccountFiscalPositionAccount(models.Model):
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, db_comment='Fiscal Position')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    account_src = models.ForeignKey(AccountAccount, models.DO_NOTHING, db_comment='Account on Product')
    account_dest = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='accountfiscalpositionaccount_account_dest_set', db_comment='Account to Use Instead')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountfiscalpositionaccount_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account'
        unique_together = (('position', 'account_src', 'account_dest'),)
        db_table_comment = 'Accounts Mapping of Fiscal Position'


class AccountFiscalPositionPosConfigRel(models.Model):
    pk = models.CompositePrimaryKey('pos_config_id', 'account_fiscal_position_id')
    pos_config = models.ForeignKey('PosConfig', models.DO_NOTHING)
    account_fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_pos_config_rel'
        db_table_comment = 'RELATION BETWEEN pos_config AND account_fiscal_position'


class AccountFiscalPositionResConfigSettingsRel(models.Model):
    pk = models.CompositePrimaryKey('res_config_settings_id', 'account_fiscal_position_id')
    res_config_settings = models.ForeignKey('ResConfigSettings', models.DO_NOTHING)
    account_fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_res_config_settings_rel'
        db_table_comment = 'RELATION BETWEEN res_config_settings AND account_fiscal_position'


class AccountFiscalPositionResCountryStateRel(models.Model):
    pk = models.CompositePrimaryKey('account_fiscal_position_id', 'res_country_state_id')
    account_fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_res_country_state_rel'
        db_table_comment = 'RELATION BETWEEN account_fiscal_position AND res_country_state'


class AccountFiscalPositionTax(models.Model):
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, db_comment='Fiscal Position')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    tax_src = models.ForeignKey('AccountTax', models.DO_NOTHING, db_comment='Tax on Product')
    tax_dest = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name='accountfiscalpositiontax_tax_dest_set', blank=True, null=True, db_comment='Tax to Apply')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountfiscalpositiontax_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax'
        unique_together = (('position', 'tax_src', 'tax_dest'),)
        db_table_comment = 'Tax Mapping of Fiscal Position'


class AccountFollowup(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountfollowup_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_followup'
        db_table_comment = 'Account Follow-up'


class AccountFullReconcile(models.Model):
    exchange_move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True, db_comment='Exchange Move')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountfullreconcile_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_full_reconcile'
        db_table_comment = 'Full Reconcile'


class AccountGroup(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountgroup_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code_prefix_start = models.CharField(blank=True, null=True, db_comment='Code Prefix Start')
    code_prefix_end = models.CharField(blank=True, null=True, db_comment='Code Prefix End')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_group'
        db_table_comment = 'Account Group'


class AccountIncoterms(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountincoterms_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code = models.CharField(max_length=3, db_comment='Code')
    name = models.JSONField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_incoterms'
        db_table_comment = 'Incoterms'


class AccountInvoiceTransactionRel(models.Model):
    pk = models.CompositePrimaryKey('invoice_id', 'transaction_id')
    invoice = models.ForeignKey('AccountMove', models.DO_NOTHING)
    transaction = models.ForeignKey('PaymentTransaction', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_transaction_rel'
        db_table_comment = 'RELATION BETWEEN account_move AND payment_transaction'


class AccountJournal(models.Model):
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING, blank=True, null=True, db_comment='Alias')
    default_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Default Account')
    suspense_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='accountjournal_suspense_account_set', blank=True, null=True, db_comment='Suspense Account')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    profit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='accountjournal_profit_account_set', blank=True, null=True, db_comment='Profit Account')
    loss_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='accountjournal_loss_account_set', blank=True, null=True, db_comment='Loss Account')
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True, db_comment='Bank Account')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountjournal_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    access_token = models.CharField(blank=True, null=True, db_comment='Security Token')
    code = models.CharField(max_length=5, db_comment='Short Code')
    type = models.CharField(db_comment='Type')
    invoice_reference_type = models.CharField(db_comment='Communication Type')
    invoice_reference_model = models.CharField(db_comment='Communication Standard')
    bank_statements_source = models.CharField(blank=True, null=True, db_comment='Bank Feeds')
    name = models.JSONField(db_comment='Journal Name')
    sequence_override_regex = models.TextField(blank=True, null=True, db_comment='Sequence Override Regex')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    autocheck_on_post = models.BooleanField(blank=True, null=True, db_comment='Auto-Check on Post')
    restrict_mode_hash_table = models.BooleanField(blank=True, null=True, db_comment='Secure Posted Entries with Hash')
    refund_sequence = models.BooleanField(blank=True, null=True, db_comment='Dedicated Credit Note Sequence')
    payment_sequence = models.BooleanField(blank=True, null=True, db_comment='Dedicated Payment Sequence')
    show_on_dashboard = models.BooleanField(blank=True, null=True, db_comment='Show journal on dashboard')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    debit_sequence = models.BooleanField(blank=True, null=True, db_comment='Dedicated Debit Note Sequence')
    check_sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, blank=True, null=True, db_comment='Check Sequence')
    bank_check_printing_layout = models.CharField(blank=True, null=True, db_comment='Check Layout')
    check_manual_sequencing = models.BooleanField(blank=True, null=True, db_comment='Manual Numbering')
    multiple_invoice_type = models.CharField(db_comment='Display Type')
    text_position = models.CharField(db_comment='Text Position')
    body_text_position = models.CharField(blank=True, null=True, db_comment='Body Text Position')
    text_align = models.CharField(blank=True, null=True, db_comment='Center Align Text Position')

    class Meta:
        managed = False
        db_table = 'account_journal'
        unique_together = (('company', 'code'),)
        db_table_comment = 'Journal'


class AccountJournalAccountJournalGroupRel(models.Model):
    pk = models.CompositePrimaryKey('account_journal_group_id', 'account_journal_id')
    account_journal_group = models.ForeignKey('AccountJournalGroup', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_journal_group_rel'
        db_table_comment = 'RELATION BETWEEN account_journal_group AND account_journal'


class AccountJournalAccountPrintJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_print_journal_id', 'account_journal_id')
    account_print_journal = models.ForeignKey('AccountPrintJournal', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_print_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_print_journal AND account_journal'


class AccountJournalAccountReconcileModelRel(models.Model):
    pk = models.CompositePrimaryKey('account_reconcile_model_id', 'account_journal_id')
    account_reconcile_model = models.ForeignKey('AccountReconcileModel', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_reconcile_model_rel'
        db_table_comment = 'RELATION BETWEEN account_reconcile_model AND account_journal'


class AccountJournalAccountReportPartnerLedgerRel(models.Model):
    pk = models.CompositePrimaryKey('account_report_partner_ledger_id', 'account_journal_id')
    account_report_partner_ledger = models.ForeignKey('AccountReportPartnerLedger', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_report_partner_ledger_rel'
        db_table_comment = 'RELATION BETWEEN account_report_partner_ledger AND account_journal'


class AccountJournalAccountReportRel(models.Model):
    pk = models.CompositePrimaryKey('account_report_id', 'account_journal_id')
    account_report = models.ForeignKey('AccountReport', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_report_rel'
        db_table_comment = 'RELATION BETWEEN account_report AND account_journal'


class AccountJournalCashFlowReportRel(models.Model):
    pk = models.CompositePrimaryKey('cash_flow_report_id', 'account_journal_id')
    cash_flow_report = models.ForeignKey('CashFlowReport', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_cash_flow_report_rel'
        db_table_comment = 'RELATION BETWEEN cash_flow_report AND account_journal'


class AccountJournalFinancialReportRel(models.Model):
    pk = models.CompositePrimaryKey('financial_report_id', 'account_journal_id')
    financial_report = models.ForeignKey('FinancialReport', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_financial_report_rel'
        db_table_comment = 'RELATION BETWEEN financial_report AND account_journal'


class AccountJournalGroup(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountjournalgroup_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Ledger group')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_journal_group'
        unique_together = (('company', 'name'),)
        db_table_comment = 'Account Journal Group'


class AccountJournalKitAccountTaxReportRel(models.Model):
    pk = models.CompositePrimaryKey('kit_account_tax_report_id', 'account_journal_id')
    kit_account_tax_report = models.ForeignKey('KitAccountTaxReport', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_kit_account_tax_report_rel'
        db_table_comment = 'RELATION BETWEEN kit_account_tax_report AND account_journal'


class AccountLockDate(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountlockdate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    sale_lock_date = models.DateField(blank=True, null=True, db_comment='Sales Lock Date')
    purchase_lock_date = models.DateField(blank=True, null=True, db_comment='Purchase Lock date')
    hard_lock_date = models.DateField(blank=True, null=True, db_comment='Lock Everyone')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_lock_date'
        db_table_comment = 'Lock date for accounting'


class AccountLockException(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='User')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='accountlockexception_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountlockexception_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    reason = models.CharField(blank=True, null=True, db_comment='Reason')
    lock_date_field = models.CharField(db_comment='Lock Date Field')
    lock_date = models.DateField(blank=True, null=True, db_comment='Changed Lock Date')
    company_lock_date = models.DateField(blank=True, null=True, db_comment='Original Lock Date')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    end_datetime = models.DateTimeField(blank=True, null=True, db_comment='End Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_lock_exception'
        db_table_comment = 'Account Lock Exception'


class AccountMergeWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountmergewizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    is_group_by_name = models.BooleanField(blank=True, null=True, db_comment='Group by name?')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_merge_wizard'
        db_table_comment = 'Account merge wizard'


class AccountMergeWizardLine(models.Model):
    wizard = models.ForeignKey(AccountMergeWizard, models.DO_NOTHING, db_comment='Wizard')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Account')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountmergewizardline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    grouping_key = models.CharField(blank=True, null=True, db_comment='Grouping Key')
    display_type = models.CharField(db_comment='Display Type')
    is_selected = models.BooleanField(blank=True, null=True, db_comment='Is Selected')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_merge_wizard_line'
        db_table_comment = 'Account merge wizard line'


class AccountMove(models.Model):
    sequence_number = models.IntegerField(blank=True, null=True, db_comment='Sequence Number')
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True, db_comment='Main Attachment')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, db_comment='Journal')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    origin_payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, blank=True, null=True, db_comment='Payment')
    statement_line = models.ForeignKey(AccountBankStatementLine, models.DO_NOTHING, blank=True, null=True, db_comment='Statement Line')
    tax_cash_basis_rec = models.ForeignKey('AccountPartialReconcile', models.DO_NOTHING, blank=True, null=True, db_comment='Tax Cash Basis Entry of')
    tax_cash_basis_origin_move = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Cash Basis Origin')
    auto_post_origin = models.ForeignKey('self', models.DO_NOTHING, related_name='accountmove_auto_post_origin_set', blank=True, null=True, db_comment='First recurring entry')
    secure_sequence_number = models.IntegerField(blank=True, null=True, db_comment='Inalterability No Gap Sequence #')
    invoice_payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, blank=True, null=True, db_comment='Payment Terms')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    commercial_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='accountmove_commercial_partner_set', blank=True, null=True, db_comment='Commercial Entity')
    partner_shipping = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='accountmove_partner_shipping_set', blank=True, null=True, db_comment='Delivery Address')
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True, db_comment='Recipient Bank')
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True, db_comment='Fiscal Position')
    preferred_payment_method_line = models.ForeignKey('AccountPaymentMethodLine', models.DO_NOTHING, blank=True, null=True, db_comment='Preferred Payment Method Line')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, db_comment='Currency')
    reversed_entry = models.ForeignKey('self', models.DO_NOTHING, related_name='accountmove_reversed_entry_set', blank=True, null=True, db_comment='Reversal of')
    invoice_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Salesperson')
    invoice_incoterm = models.ForeignKey(AccountIncoterms, models.DO_NOTHING, blank=True, null=True, db_comment='Incoterm')
    invoice_cash_rounding = models.ForeignKey(AccountCashRounding, models.DO_NOTHING, blank=True, null=True, db_comment='Cash Rounding Method')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='accountmove_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountmove_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    sequence_prefix = models.CharField(blank=True, null=True, db_comment='Sequence Prefix')
    access_token = models.CharField(blank=True, null=True, db_comment='Security Token')
    name = models.CharField(blank=True, null=True, db_comment='Number')
    ref = models.CharField(blank=True, null=True, db_comment='Reference')
    state = models.CharField(db_comment='Status')
    move_type = models.CharField(db_comment='Type')
    auto_post = models.CharField(db_comment='Auto-post')
    inalterable_hash = models.CharField(blank=True, null=True, db_comment='Inalterability Hash')
    payment_reference = models.CharField(blank=True, null=True, db_comment='Payment Reference')
    qr_code_method = models.CharField(blank=True, null=True, db_comment='Payment QR-code')
    payment_state = models.CharField(blank=True, null=True, db_comment='Payment Status')
    invoice_source_email = models.CharField(blank=True, null=True, db_comment='Source Email')
    invoice_partner_display_name = models.CharField(blank=True, null=True, db_comment='Invoice Partner Display Name')
    invoice_origin = models.CharField(blank=True, null=True, db_comment='Origin')
    incoterm_location = models.CharField(blank=True, null=True, db_comment='Incoterm Location')
    date = models.DateField(db_comment='Date')
    auto_post_until = models.DateField(blank=True, null=True, db_comment='Auto-post until')
    invoice_date = models.DateField(blank=True, null=True, db_comment='Invoice/Bill Date')
    invoice_date_due = models.DateField(blank=True, null=True, db_comment='Due Date')
    delivery_date = models.DateField(blank=True, null=True, db_comment='Delivery Date')
    sending_data = models.JSONField(blank=True, null=True, db_comment='Sending Data')
    narration = models.TextField(blank=True, null=True, db_comment='Terms and Conditions')
    invoice_currency_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Currency Rate')
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Untaxed Amount')
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Tax')
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total')
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount Due')
    amount_untaxed_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Untaxed Amount Signed')
    amount_untaxed_in_currency_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Untaxed Amount Signed Currency')
    amount_tax_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Tax Signed')
    amount_total_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total Signed')
    amount_total_in_currency_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total in Currency Signed')
    amount_residual_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount Due Signed')
    quick_edit_total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total (Tax inc.)')
    is_storno = models.BooleanField(blank=True, null=True, db_comment='Is Storno')
    always_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Always Tax Exigible')
    checked = models.BooleanField(blank=True, null=True, db_comment='Checked')
    posted_before = models.BooleanField(blank=True, null=True, db_comment='Posted Before')
    made_sequence_gap = models.BooleanField(blank=True, null=True, db_comment='Made Sequence Gap')
    is_manually_modified = models.BooleanField(blank=True, null=True, db_comment='Is Manually Modified')
    is_move_sent = models.BooleanField(blank=True, null=True, db_comment='Is Move Sent')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    debit_origin = models.ForeignKey('self', models.DO_NOTHING, related_name='accountmove_debit_origin_set', blank=True, null=True, db_comment='Original Invoice Debited')
    l10n_in_state = models.ForeignKey('ResCountryState', models.DO_NOTHING, blank=True, null=True, db_comment='Place of supply')
    l10n_in_shipping_port_code = models.ForeignKey('L10NInPortCode', models.DO_NOTHING, blank=True, null=True, db_comment='Port code')
    l10n_in_reseller_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='accountmove_l10n_in_reseller_partner_set', blank=True, null=True, db_comment='Reseller')
    l10n_in_gst_treatment = models.CharField(blank=True, null=True, db_comment='GST Treatment')
    l10n_in_gstin = models.CharField(blank=True, null=True, db_comment='GSTIN')
    l10n_in_shipping_bill_number = models.CharField(blank=True, null=True, db_comment='Shipping bill number')
    l10n_in_shipping_bill_date = models.DateField(blank=True, null=True, db_comment='Shipping bill date')
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True, db_comment='Campaign')
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True, db_comment='Source')
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True, db_comment='Medium')
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True, db_comment='Sales Team')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True)
    stock_move = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True, db_comment='Stock Move')
    reversed_pos_order = models.ForeignKey('PosOrder', models.DO_NOTHING, blank=True, null=True, db_comment='Reversed POS Order')
    recurring_ref = models.CharField(blank=True, null=True, db_comment='Recurring Ref')
    has_due = models.BooleanField(blank=True, null=True, db_comment='Has due')
    is_warning = models.BooleanField(blank=True, null=True, db_comment='Is warning')
    to_check = models.BooleanField(blank=True, null=True, db_comment='To Check')
    expense_sheet = models.ForeignKey('HrExpenseSheet', models.DO_NOTHING, blank=True, null=True, db_comment='Expense Sheet')
    edi_state = models.CharField(blank=True, null=True, db_comment='Electronic invoicing')
    l10n_in_edi_cancel_reason = models.CharField(blank=True, null=True, db_comment='Cancel reason')
    l10n_in_edi_cancel_remarks = models.CharField(blank=True, null=True, db_comment='Cancel remarks')

    class Meta:
        managed = False
        db_table = 'account_move'
        unique_together = (('name', 'journal'),)
        db_table_comment = 'Journal Entry'


class AccountMoveAccountPayment(models.Model):
    pk = models.CompositePrimaryKey('invoice_id', 'payment_id')
    invoice = models.ForeignKey(AccountMove, models.DO_NOTHING)
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move__account_payment'
        db_table_comment = 'RELATION BETWEEN account_move AND account_payment'


class AccountMoveAccountMoveSendBatchWizardRel(models.Model):
    pk = models.CompositePrimaryKey('account_move_send_batch_wizard_id', 'account_move_id')
    account_move_send_batch_wizard = models.ForeignKey('AccountMoveSendBatchWizard', models.DO_NOTHING)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_account_move_send_batch_wizard_rel'
        db_table_comment = 'RELATION BETWEEN account_move_send_batch_wizard AND account_move'


class AccountMoveAccountResequenceWizardRel(models.Model):
    pk = models.CompositePrimaryKey('account_resequence_wizard_id', 'account_move_id')
    account_resequence_wizard = models.ForeignKey('AccountResequenceWizard', models.DO_NOTHING)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_account_resequence_wizard_rel'
        db_table_comment = 'RELATION BETWEEN account_resequence_wizard AND account_move'


class AccountMoveDebitMove(models.Model):
    pk = models.CompositePrimaryKey('debit_id', 'move_id')
    debit = models.ForeignKey(AccountDebitNote, models.DO_NOTHING)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_debit_move'
        db_table_comment = 'RELATION BETWEEN account_debit_note AND account_move'


class AccountMoveLine(models.Model):
    move = models.ForeignKey(AccountMove, models.DO_NOTHING, db_comment='Journal Entry')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Journal')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    company_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Company Currency')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Account')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name='accountmoveline_currency_set', db_comment='Currency')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    reconcile_model = models.ForeignKey('AccountReconcileModel', models.DO_NOTHING, blank=True, null=True, db_comment='Reconciliation Model')
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, blank=True, null=True, db_comment='Originator Payment')
    statement_line = models.ForeignKey(AccountBankStatementLine, models.DO_NOTHING, blank=True, null=True, db_comment='Originator Statement Line')
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True, db_comment='Statement')
    group_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True, db_comment='Originator Group of Taxes')
    tax_line = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name='accountmoveline_tax_line_set', blank=True, null=True, db_comment='Originator Tax')
    tax_group = models.ForeignKey('AccountTaxGroup', models.DO_NOTHING, blank=True, null=True, db_comment='Originator tax group')
    tax_repartition_line = models.ForeignKey('AccountTaxRepartitionLine', models.DO_NOTHING, blank=True, null=True, db_comment='Originator Tax Distribution Line')
    full_reconcile = models.ForeignKey(AccountFullReconcile, models.DO_NOTHING, blank=True, null=True, db_comment='Matching')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True, db_comment='Unit of Measure')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountmoveline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    move_name = models.CharField(blank=True, null=True, db_comment='Number')
    parent_state = models.CharField(blank=True, null=True, db_comment='Status')
    ref = models.CharField(blank=True, null=True, db_comment='Reference')
    name = models.CharField(blank=True, null=True, db_comment='Label')
    matching_number = models.CharField(blank=True, null=True, db_comment='Matching #')
    display_type = models.CharField(db_comment='Display Type')
    date = models.DateField(blank=True, null=True, db_comment='Date')
    invoice_date = models.DateField(blank=True, null=True, db_comment='Invoice/Bill Date')
    date_maturity = models.DateField(blank=True, null=True, db_comment='Due Date')
    discount_date = models.DateField(blank=True, null=True, db_comment='Discount Date')
    analytic_distribution = models.JSONField(blank=True, null=True, db_comment='Analytic Distribution')
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Debit')
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Credit')
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Balance')
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount in Currency')
    tax_base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Base Amount')
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Residual Amount')
    amount_residual_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Residual Amount in Currency')
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Quantity')
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Unit Price')
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Subtotal')
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total')
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Discount (%)')
    discount_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Discount amount in Currency')
    discount_balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Discount Balance')
    is_imported = models.BooleanField(blank=True, null=True, db_comment='Is Imported')
    tax_tag_invert = models.BooleanField(blank=True, null=True, db_comment='Invert Tags')
    reconciled = models.BooleanField(blank=True, null=True, db_comment='Reconciled')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    l10n_in_hsn_code = models.CharField(blank=True, null=True, db_comment='HSN/SAC Code')
    is_downpayment = models.BooleanField(blank=True, null=True, db_comment='Is Downpayment')
    cogs_origin = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Cogs Origin')
    asset_category = models.ForeignKey(AccountAssetCategory, models.DO_NOTHING, blank=True, null=True, db_comment='Asset Category')
    asset_start_date = models.DateField(blank=True, null=True, db_comment='Asset Start Date')
    asset_end_date = models.DateField(blank=True, null=True, db_comment='Asset End Date')
    asset_mrr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Monthly Recurring Revenue')
    purchase_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING, blank=True, null=True, db_comment='Purchase Order Line')
    expense = models.ForeignKey('HrExpense', models.DO_NOTHING, blank=True, null=True, db_comment='Expense')

    class Meta:
        managed = False
        db_table = 'account_move_line'
        db_table_comment = 'Journal Item'


class AccountMoveLineAccountTaxRel(models.Model):
    pk = models.CompositePrimaryKey('account_move_line_id', 'account_tax_id')
    account_move_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_line_account_tax_rel'
        db_table_comment = 'RELATION BETWEEN account_move_line AND account_tax'


class AccountMoveMrpProductionRel(models.Model):
    pk = models.CompositePrimaryKey('account_move_id', 'mrp_production_id')
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING)
    mrp_production = models.ForeignKey('MrpProduction', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_mrp_production_rel'
        db_table_comment = 'RELATION BETWEEN account_move AND mrp_production'


class AccountMovePurchaseOrderRel(models.Model):
    pk = models.CompositePrimaryKey('purchase_order_id', 'account_move_id')
    purchase_order = models.ForeignKey('PurchaseOrder', models.DO_NOTHING)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_purchase_order_rel'
        db_table_comment = 'RELATION BETWEEN purchase_order AND account_move'


class AccountMoveReversal(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, db_comment='Journal')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountmovereversal_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    reason = models.CharField(blank=True, null=True, db_comment='Reason displayed on Credit Note')
    date = models.DateField(blank=True, null=True, db_comment='Reversal date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_move_reversal'
        db_table_comment = 'Account Move Reversal'


class AccountMoveReversalMove(models.Model):
    pk = models.CompositePrimaryKey('reversal_id', 'move_id')
    reversal = models.ForeignKey(AccountMoveReversal, models.DO_NOTHING)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_reversal_move'
        db_table_comment = 'RELATION BETWEEN account_move_reversal AND account_move'


class AccountMoveReversalNewMove(models.Model):
    pk = models.CompositePrimaryKey('reversal_id', 'new_move_id')
    reversal = models.ForeignKey(AccountMoveReversal, models.DO_NOTHING)
    new_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_reversal_new_move'
        db_table_comment = 'RELATION BETWEEN account_move_reversal AND account_move'


class AccountMoveSendBatchWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountmovesendbatchwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_move_send_batch_wizard'
        db_table_comment = 'Account Move Send Batch Wizard'


class AccountMoveSendWizard(models.Model):
    move = models.ForeignKey(AccountMove, models.DO_NOTHING, db_comment='Move')
    pdf_report = models.ForeignKey('IrActReportXml', models.DO_NOTHING, blank=True, null=True, db_comment='Invoice template')
    mail_template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='Email template')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountmovesendwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    mail_subject = models.CharField(blank=True, null=True, db_comment='Subject')
    sending_method_checkboxes = models.JSONField(blank=True, null=True, db_comment='Sending Method Checkboxes')
    extra_edi_checkboxes = models.JSONField(blank=True, null=True, db_comment='Extra Edi Checkboxes')
    mail_attachments_widget = models.JSONField(blank=True, null=True, db_comment='Mail Attachments Widget')
    mail_body = models.TextField(blank=True, null=True, db_comment='Contents')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_move_send_wizard'
        db_table_comment = 'Account Move Send Wizard'


class AccountMoveSendWizardResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('account_move_send_wizard_id', 'res_partner_id')
    account_move_send_wizard = models.ForeignKey(AccountMoveSendWizard, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_send_wizard_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN account_move_send_wizard AND res_partner'


class AccountMoveValidateAccountMoveRel(models.Model):
    pk = models.CompositePrimaryKey('validate_account_move_id', 'account_move_id')
    validate_account_move = models.ForeignKey('ValidateAccountMove', models.DO_NOTHING)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_validate_account_move_rel'
        db_table_comment = 'RELATION BETWEEN validate_account_move AND account_move'


class AccountPartialReconcile(models.Model):
    debit_move = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, db_comment='Debit Move')
    credit_move = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, related_name='accountpartialreconcile_credit_move_set', db_comment='Credit Move')
    full_reconcile = models.ForeignKey(AccountFullReconcile, models.DO_NOTHING, blank=True, null=True, db_comment='Full Reconcile')
    exchange_move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True, db_comment='Exchange Move')
    debit_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency of the debit journal item.')
    credit_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name='accountpartialreconcile_credit_currency_set', blank=True, null=True, db_comment='Currency of the credit journal item.')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountpartialreconcile_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    max_date = models.DateField(blank=True, null=True, db_comment='Max Date of Matched Lines')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount')
    debit_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Debit Amount Currency')
    credit_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Credit Amount Currency')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_partial_reconcile'
        db_table_comment = 'Partial Reconcile'


class AccountPayment(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True, db_comment='Main Attachment')
    move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True, db_comment='Journal Entry')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, db_comment='Journal')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True, db_comment='Recipient Bank Account')
    paired_internal_transfer_payment = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Paired Internal Transfer Payment')
    payment_method_line = models.ForeignKey('AccountPaymentMethodLine', models.DO_NOTHING, blank=True, null=True, db_comment='Payment Method')
    payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING, blank=True, null=True, db_comment='Method')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Customer/Vendor')
    outstanding_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Outstanding Account')
    destination_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='accountpayment_destination_account_set', blank=True, null=True, db_comment='Destination Account')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountpayment_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Number')
    state = models.CharField(db_comment='State')
    payment_type = models.CharField(db_comment='Payment Type')
    partner_type = models.CharField(db_comment='Partner Type')
    memo = models.CharField(blank=True, null=True, db_comment='Memo')
    payment_reference = models.CharField(blank=True, null=True, db_comment='Payment Reference')
    date = models.DateField(db_comment='Date')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount')
    amount_company_currency_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount Company Currency Signed')
    is_reconciled = models.BooleanField(blank=True, null=True, db_comment='Is Reconciled')
    is_matched = models.BooleanField(blank=True, null=True, db_comment='Is Matched With a Bank Statement')
    is_sent = models.BooleanField(blank=True, null=True, db_comment='Is Sent')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    payment_transaction = models.ForeignKey('PaymentTransaction', models.DO_NOTHING, blank=True, null=True, db_comment='Payment Transaction')
    payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True, db_comment='Saved Payment Token')
    source_payment = models.ForeignKey('self', models.DO_NOTHING, related_name='accountpayment_source_payment_set', blank=True, null=True, db_comment='Source Payment')
    pos_payment_method = models.ForeignKey('PosPaymentMethod', models.DO_NOTHING, blank=True, null=True, db_comment='POS Payment Method')
    force_outstanding_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='accountpayment_force_outstanding_account_set', blank=True, null=True, db_comment='Forced Outstanding Account')
    pos_session = models.ForeignKey('PosSession', models.DO_NOTHING, blank=True, null=True, db_comment='POS Session')
    pos_order = models.ForeignKey('PosOrder', models.DO_NOTHING, blank=True, null=True, db_comment='POS Order')
    check_number = models.CharField(blank=True, null=True)
    check_amount_in_words = models.CharField(blank=True, null=True, db_comment='Amount in Words')
    bank_reference = models.CharField(blank=True, null=True, db_comment='Bank Reference')
    cheque_reference = models.CharField(blank=True, null=True, db_comment='Cheque Reference')
    effective_date = models.DateField(blank=True, null=True, db_comment='Effective Date')

    class Meta:
        managed = False
        db_table = 'account_payment'
        db_table_comment = 'Payments'


class AccountPaymentAccountBankStatementLineRel(models.Model):
    pk = models.CompositePrimaryKey('account_bank_statement_line_id', 'account_payment_id')
    account_bank_statement_line = models.ForeignKey(AccountBankStatementLine, models.DO_NOTHING)
    account_payment = models.ForeignKey(AccountPayment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_payment_account_bank_statement_line_rel'
        db_table_comment = 'RELATION BETWEEN account_bank_statement_line AND account_payment'


class AccountPaymentMethod(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountpaymentmethod_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code = models.CharField(db_comment='Code')
    payment_type = models.CharField(db_comment='Payment Type')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_payment_method'
        unique_together = (('code', 'payment_type'),)
        db_table_comment = 'Payment Methods'


class AccountPaymentMethodLine(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    payment_method = models.ForeignKey(AccountPaymentMethod, models.DO_NOTHING, db_comment='Payment Method')
    payment_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Payment Account')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Journal')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountpaymentmethodline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    payment_provider = models.ForeignKey('PaymentProvider', models.DO_NOTHING, blank=True, null=True, db_comment='Payment Provider')

    class Meta:
        managed = False
        db_table = 'account_payment_method_line'
        db_table_comment = 'Payment Methods'


class AccountPaymentMethodLineResCompanyRel(models.Model):
    pk = models.CompositePrimaryKey('res_company_id', 'account_payment_method_line_id')
    res_company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    account_payment_method_line = models.ForeignKey(AccountPaymentMethodLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_payment_method_line_res_company_rel'
        db_table_comment = 'RELATION BETWEEN res_company AND account_payment_method_line'


class AccountPaymentRegister(models.Model):
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Journal')
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True, db_comment='Recipient Bank Account')
    custom_user_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name='accountpaymentregister_custom_user_currency_set', blank=True, null=True, db_comment='Custom User Currency')
    source_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name='accountpaymentregister_source_currency_set', blank=True, null=True, db_comment='Source Currency')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Customer/Vendor')
    payment_method_line = models.ForeignKey(AccountPaymentMethodLine, models.DO_NOTHING, blank=True, null=True, db_comment='Payment Method')
    writeoff_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Difference Account')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountpaymentregister_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    communication = models.CharField(blank=True, null=True, db_comment='Memo')
    installments_mode = models.CharField(blank=True, null=True, db_comment='Installments Mode')
    payment_type = models.CharField(blank=True, null=True, db_comment='Payment Type')
    partner_type = models.CharField(blank=True, null=True, db_comment='Partner Type')
    payment_difference_handling = models.CharField(blank=True, null=True, db_comment='Payment Difference Handling')
    writeoff_label = models.CharField(blank=True, null=True, db_comment='Journal Item Label')
    payment_date = models.DateField(db_comment='Payment Date')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount')
    custom_user_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Custom User Amount')
    source_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount to Pay (company currency)')
    source_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount to Pay (foreign currency)')
    group_payment = models.BooleanField(blank=True, null=True, db_comment='Group Payments')
    can_edit_wizard = models.BooleanField(blank=True, null=True, db_comment='Can Edit Wizard')
    can_group_payments = models.BooleanField(blank=True, null=True, db_comment='Can Group Payments')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True, db_comment='Saved payment token')
    bank_reference = models.CharField(blank=True, null=True, db_comment='Bank Reference')
    cheque_reference = models.CharField(blank=True, null=True, db_comment='Cheque Reference')
    effective_date = models.DateField(blank=True, null=True, db_comment='Effective Date')

    class Meta:
        managed = False
        db_table = 'account_payment_register'
        db_table_comment = 'Pay'


class AccountPaymentRegisterMoveLineRel(models.Model):
    pk = models.CompositePrimaryKey('wizard_id', 'line_id')
    wizard = models.ForeignKey(AccountPaymentRegister, models.DO_NOTHING)
    line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_payment_register_move_line_rel'
        db_table_comment = 'RELATION BETWEEN account_payment_register AND account_move_line'


class AccountPaymentTerm(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    sequence = models.IntegerField(db_comment='Sequence')
    discount_days = models.IntegerField(blank=True, null=True, db_comment='Discount Days')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountpaymentterm_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    early_pay_discount_computation = models.CharField(blank=True, null=True, db_comment='Cash Discount Tax Reduction')
    name = models.JSONField(db_comment='Payment Terms')
    note = models.JSONField(blank=True, null=True, db_comment='Description on the Invoice')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    display_on_invoice = models.BooleanField(blank=True, null=True, db_comment='Show installment dates')
    early_discount = models.BooleanField(blank=True, null=True, db_comment='Early Discount')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    discount_percentage = models.FloatField(blank=True, null=True, db_comment='Discount %')

    class Meta:
        managed = False
        db_table = 'account_payment_term'
        db_table_comment = 'Payment Terms'


class AccountPaymentTermLine(models.Model):
    nb_days = models.IntegerField(blank=True, null=True, db_comment='Days')
    payment = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING, db_comment='Payment Terms')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountpaymenttermline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    value = models.CharField(db_comment='Value')
    delay_type = models.CharField(db_comment='Delay Type')
    days_next_month = models.CharField(max_length=2, blank=True, null=True, db_comment='Days on the next month')
    value_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Due')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_payment_term_line'
        db_table_comment = 'Payment Terms Line'


class AccountPrintJournal(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey('AccountReport', models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountprintjournal_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    sort_selection = models.CharField(db_comment='Entries Sorted by')
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    name = models.JSONField(db_comment='Journal Audit')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    amount_currency = models.BooleanField(blank=True, null=True, db_comment='With Currency')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_print_journal'
        db_table_comment = 'Account Print Journal'


class AccountReconcileModel(models.Model):
    sequence = models.IntegerField(db_comment='Sequence')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    past_months_limit = models.IntegerField(blank=True, null=True, db_comment='Search Months Limit')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountreconcilemodel_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    rule_type = models.CharField(db_comment='Type')
    matching_order = models.CharField(db_comment='Matching Order')
    counterpart_type = models.CharField(blank=True, null=True, db_comment='Counterpart Type')
    match_nature = models.CharField(db_comment='Amount Type')
    match_amount = models.CharField(blank=True, null=True, db_comment='Amount Condition')
    match_label = models.CharField(blank=True, null=True, db_comment='Label')
    match_label_param = models.CharField(blank=True, null=True, db_comment='Label Parameter')
    match_note = models.CharField(blank=True, null=True, db_comment='Note')
    match_note_param = models.CharField(blank=True, null=True, db_comment='Note Parameter')
    match_transaction_type = models.CharField(blank=True, null=True, db_comment='Transaction Type')
    match_transaction_type_param = models.CharField(blank=True, null=True, db_comment='Transaction Type Parameter')
    payment_tolerance_type = models.CharField(db_comment='Payment Tolerance Type')
    decimal_separator = models.CharField(blank=True, null=True, db_comment='Decimal Separator')
    name = models.JSONField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    auto_reconcile = models.BooleanField(blank=True, null=True, db_comment='Auto-validate')
    to_check = models.BooleanField(blank=True, null=True, db_comment='To Check')
    match_text_location_label = models.BooleanField(blank=True, null=True, db_comment='Match Text Location Label')
    match_text_location_note = models.BooleanField(blank=True, null=True, db_comment='Match Text Location Note')
    match_text_location_reference = models.BooleanField(blank=True, null=True, db_comment='Match Text Location Reference')
    match_same_currency = models.BooleanField(blank=True, null=True, db_comment='Same Currency')
    allow_payment_tolerance = models.BooleanField(blank=True, null=True, db_comment='Payment Tolerance')
    match_partner = models.BooleanField(blank=True, null=True, db_comment='Partner is Set')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    match_amount_min = models.FloatField(blank=True, null=True, db_comment='Amount Min Parameter')
    match_amount_max = models.FloatField(blank=True, null=True, db_comment='Amount Max Parameter')
    payment_tolerance_param = models.FloatField(blank=True, null=True, db_comment='Gap')

    class Meta:
        managed = False
        db_table = 'account_reconcile_model'
        unique_together = (('name', 'company'),)
        db_table_comment = 'Preset to create journal entries during a invoices and payments matching'


class AccountReconcileModelLine(models.Model):
    model = models.ForeignKey(AccountReconcileModel, models.DO_NOTHING, blank=True, null=True, db_comment='Model')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    sequence = models.IntegerField(db_comment='Sequence')
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Account')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Journal')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountreconcilemodelline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    amount_type = models.CharField(db_comment='Amount Type')
    amount_string = models.CharField(db_comment='Amount')
    analytic_distribution = models.JSONField(blank=True, null=True, db_comment='Analytic Distribution')
    label = models.JSONField(blank=True, null=True, db_comment='Journal Item Label')
    force_tax_included = models.BooleanField(blank=True, null=True, db_comment='Tax Included in Price')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    amount = models.FloatField(blank=True, null=True, db_comment='Float Amount')

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line'
        db_table_comment = 'Rules for the reconciliation model'


class AccountReconcileModelLineAccountTaxRel(models.Model):
    pk = models.CompositePrimaryKey('account_reconcile_model_line_id', 'account_tax_id')
    account_reconcile_model_line = models.ForeignKey(AccountReconcileModelLine, models.DO_NOTHING)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line_account_tax_rel'
        db_table_comment = 'RELATION BETWEEN account_reconcile_model_line AND account_tax'


class AccountReconcileModelPartnerMapping(models.Model):
    model = models.ForeignKey(AccountReconcileModel, models.DO_NOTHING, db_comment='Model')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Partner')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountreconcilemodelpartnermapping_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    payment_ref_regex = models.CharField(blank=True, null=True, db_comment='Find Text in Label')
    narration_regex = models.CharField(blank=True, null=True, db_comment='Find Text in Notes')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_partner_mapping'
        db_table_comment = 'Partner mapping for reconciliation models'


class AccountReconcileModelResPartnerCategoryRel(models.Model):
    pk = models.CompositePrimaryKey('account_reconcile_model_id', 'res_partner_category_id')
    account_reconcile_model = models.ForeignKey(AccountReconcileModel, models.DO_NOTHING)
    res_partner_category = models.ForeignKey('ResPartnerCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_res_partner_category_rel'
        db_table_comment = 'RELATION BETWEEN account_reconcile_model AND res_partner_category'


class AccountReconcileModelResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('account_reconcile_model_id', 'res_partner_id')
    account_reconcile_model = models.ForeignKey(AccountReconcileModel, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN account_reconcile_model AND res_partner'


class AccountRecurringEntriesLine(models.Model):
    tmpl = models.ForeignKey('AccountRecurringPayments', models.DO_NOTHING, blank=True, null=True, db_comment='id')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountrecurringentriesline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    template_name = models.CharField(blank=True, null=True, db_comment='Name')
    date = models.DateField(blank=True, null=True, db_comment='Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    amount = models.FloatField(blank=True, null=True, db_comment='Amount')

    class Meta:
        managed = False
        db_table = 'account_recurring_entries_line'
        db_table_comment = 'Account Recurring Entries Line'


class AccountRecurringPayments(models.Model):
    debit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, db_column='debit_account', db_comment='Debit Account')
    credit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, db_column='credit_account', related_name='accountrecurringpayments_credit_account_set', db_comment='Credit Account')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, db_comment='Journal')
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Analytic Account')
    recurring_interval = models.IntegerField(blank=True, null=True, db_comment='Recurring Interval')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountrecurringpayments_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    recurring_period = models.CharField(db_comment='Recurring Period')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    journal_state = models.CharField(db_comment='Generate Journal As')
    pay_time = models.CharField(db_comment='Pay Time')
    date = models.DateField(db_comment='Starting Date')
    description = models.TextField(blank=True, null=True, db_comment='Description')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    amount = models.FloatField(blank=True, null=True, db_comment='Amount')

    class Meta:
        managed = False
        db_table = 'account_recurring_payments'
        db_table_comment = 'Accounting Recurring Payment'


class AccountReport(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    name = models.JSONField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    target_move = models.CharField(db_comment='Target Moves')
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')

    class Meta:
        managed = False
        db_table = 'account_report'
        db_table_comment = 'Accounting Report'


class AccountReportBankbookAccountRel(models.Model):
    pk = models.CompositePrimaryKey('report_id', 'account_id')
    report = models.ForeignKey(AccountBankBookReport, models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_report_bankbook_account_rel'
        db_table_comment = 'RELATION BETWEEN account_bank_book_report AND account_account'


class AccountReportBankbookJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_id', 'journal_id')
    account = models.ForeignKey(AccountBankBookReport, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_report_bankbook_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_bank_book_report AND account_journal'


class AccountReportCashbookAccountRel(models.Model):
    pk = models.CompositePrimaryKey('report_id', 'account_id')
    report = models.ForeignKey(AccountCashBookReport, models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_report_cashbook_account_rel'
        db_table_comment = 'RELATION BETWEEN account_cash_book_report AND account_account'


class AccountReportCashbookJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_id', 'journal_id')
    account = models.ForeignKey(AccountCashBookReport, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_report_cashbook_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_cash_book_report AND account_journal'


class AccountReportColumn(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    report = models.ForeignKey(AccountReport, models.DO_NOTHING, blank=True, null=True, db_comment='Report')
    custom_audit_action = models.ForeignKey('IrActWindow', models.DO_NOTHING, blank=True, null=True, db_comment='Custom Audit Action')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountreportcolumn_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    expression_label = models.CharField(db_comment='Expression Label')
    figure_type = models.CharField(db_comment='Figure Type')
    name = models.JSONField(db_comment='Name')
    sortable = models.BooleanField(blank=True, null=True, db_comment='Sortable')
    blank_if_zero = models.BooleanField(blank=True, null=True, db_comment='Blank if Zero')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_report_column'
        db_table_comment = 'Accounting Report Column'


class AccountReportDaybookAccountRel(models.Model):
    pk = models.CompositePrimaryKey('report_id', 'account_id')
    report = models.ForeignKey(AccountDayBookReport, models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_report_daybook_account_rel'
        db_table_comment = 'RELATION BETWEEN account_day_book_report AND account_account'


class AccountReportExpression(models.Model):
    report_line = models.ForeignKey('AccountReportLine', models.DO_NOTHING, db_comment='Report Line')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountreportexpression_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    label = models.CharField(db_comment='Label')
    engine = models.CharField(db_comment='Computation Engine')
    formula = models.CharField(db_comment='Formula')
    subformula = models.CharField(blank=True, null=True, db_comment='Subformula')
    date_scope = models.CharField(db_comment='Date Scope')
    figure_type = models.CharField(blank=True, null=True, db_comment='Figure Type')
    carryover_target = models.CharField(blank=True, null=True, db_comment='Carry Over To')
    green_on_positive = models.BooleanField(blank=True, null=True, db_comment='Is Growth Good when Positive')
    blank_if_zero = models.BooleanField(blank=True, null=True, db_comment='Blank if Zero')
    auditable = models.BooleanField(blank=True, null=True, db_comment='Auditable')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_report_expression'
        unique_together = (('report_line', 'label'),)
        db_table_comment = 'Accounting Report Expression'


class AccountReportExternalValue(models.Model):
    target_report_expression = models.ForeignKey(AccountReportExpression, models.DO_NOTHING, db_comment='Target Expression')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    foreign_vat_fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True, db_comment='Fiscal position')
    carryover_origin_report_line = models.ForeignKey('AccountReportLine', models.DO_NOTHING, blank=True, null=True, db_comment='Origin Line')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountreportexternalvalue_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    text_value = models.CharField(blank=True, null=True, db_comment='Text Value')
    carryover_origin_expression_label = models.CharField(blank=True, null=True, db_comment='Origin Expression Label')
    date = models.DateField(db_comment='Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    value = models.FloatField(blank=True, null=True, db_comment='Numeric Value')

    class Meta:
        managed = False
        db_table = 'account_report_external_value'
        db_table_comment = 'Accounting Report External Value'


class AccountReportGeneralLedger(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey(AccountReport, models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountreportgeneralledger_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    display_account = models.CharField(db_comment='Display Accounts')
    sortby = models.CharField(db_comment='Sort by')
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    name = models.JSONField(db_comment='General Ledger')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    initial_balance = models.BooleanField(blank=True, null=True, db_comment='Include Initial Balances')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger'
        db_table_comment = 'General Ledger Report'


class AccountReportGeneralLedgerJournalRel(models.Model):
    pk = models.CompositePrimaryKey('account_id', 'journal_id')
    account = models.ForeignKey(AccountReportGeneralLedger, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger_journal_rel'
        db_table_comment = 'RELATION BETWEEN account_report_general_ledger AND account_journal'


class AccountReportGeneralSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey(AccountReport, models.DO_NOTHING)
    sub_report = models.ForeignKey(AccountReport, models.DO_NOTHING, related_name='accountreportgeneralsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_report_general_section_rel'
        db_table_comment = 'RELATION BETWEEN account_report_general_ledger AND account_report'


class AccountReportLine(models.Model):
    report = models.ForeignKey(AccountReport, models.DO_NOTHING, db_comment='Parent Report')
    hierarchy_level = models.IntegerField(db_comment='Level')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Line')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    action_id = models.IntegerField(blank=True, null=True, db_comment='Action')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountreportline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    groupby = models.CharField(blank=True, null=True, db_comment='Group By')
    user_groupby = models.CharField(blank=True, null=True, db_comment='User Group By')
    code = models.CharField(blank=True, null=True, db_comment='Code')
    horizontal_split_side = models.CharField(blank=True, null=True, db_comment='Horizontal Split Side')
    name = models.JSONField(db_comment='Name')
    foldable = models.BooleanField(blank=True, null=True, db_comment='Foldable')
    print_on_new_page = models.BooleanField(blank=True, null=True, db_comment='Print On New Page')
    hide_if_zero = models.BooleanField(blank=True, null=True, db_comment='Hide if Zero')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_report_line'
        unique_together = (('report', 'code'),)
        db_table_comment = 'Accounting Report Line'


class AccountReportPartnerLedger(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey(AccountReport, models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountreportpartnerledger_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    result_selection = models.CharField(db_comment="Partner's")
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    name = models.JSONField(db_comment='Partner Ledger Report')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    amount_currency = models.BooleanField(blank=True, null=True, db_comment='With Currency')
    reconciled = models.BooleanField(blank=True, null=True, db_comment='Reconciled Entries')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_report_partner_ledger'
        db_table_comment = 'Account Partner Ledger'


class AccountReportPartnerSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey(AccountReport, models.DO_NOTHING)
    sub_report = models.ForeignKey(AccountReport, models.DO_NOTHING, related_name='accountreportpartnersectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_report_partner_section_rel'
        db_table_comment = 'RELATION BETWEEN account_report_partner_ledger AND account_report'


class AccountReportSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey(AccountReport, models.DO_NOTHING)
    sub_report = models.ForeignKey(AccountReport, models.DO_NOTHING, related_name='accountreportsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_report_section_rel'
        db_table_comment = 'RELATION BETWEEN account_report AND account_report'


class AccountResequenceWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountresequencewizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    first_name = models.CharField(db_comment='First New Sequence')
    ordering = models.CharField(db_comment='Ordering')
    first_date = models.DateField(blank=True, null=True, db_comment='First Date')
    end_date = models.DateField(blank=True, null=True, db_comment='End Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_resequence_wizard'
        db_table_comment = 'Remake the sequence of Journal Entries.'


class AccountSecureEntriesWizard(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountsecureentrieswizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    hash_date = models.DateField(db_comment='Hash All Entries')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_secure_entries_wizard'
        db_table_comment = 'Secure Journal Entries'


class AccountSetupBankManualConfig(models.Model):
    res_partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, db_comment='Res Partner Bank')
    num_journals_without_account = models.IntegerField(blank=True, null=True, db_comment='Num Journals Without Account')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accountsetupbankmanualconfig_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    new_journal_name = models.CharField(db_comment='New Journal Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_setup_bank_manual_config'
        db_table_comment = 'Bank setup manual config'


class AccountTax(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    sequence = models.IntegerField(db_comment='Sequence')
    tax_group = models.ForeignKey('AccountTaxGroup', models.DO_NOTHING, db_comment='Tax Group')
    cash_basis_transition_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Cash Basis Transition Account')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accounttax_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    type_tax_use = models.CharField(db_comment='Tax Type')
    tax_scope = models.CharField(blank=True, null=True, db_comment='Tax Scope')
    amount_type = models.CharField(db_comment='Tax Computation')
    price_include_override = models.CharField(blank=True, null=True, db_comment='Included in Price')
    tax_exigibility = models.CharField(blank=True, null=True, db_comment='Tax Exigibility')
    name = models.JSONField(db_comment='Tax Name')
    description = models.JSONField(blank=True, null=True, db_comment='Description')
    invoice_label = models.JSONField(blank=True, null=True, db_comment='Label on Invoices')
    invoice_legal_notes = models.TextField(blank=True, null=True, db_comment='Legal Notes')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Amount')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    include_base_amount = models.BooleanField(blank=True, null=True, db_comment='Affect Base of Subsequent Taxes')
    is_base_affected = models.BooleanField(blank=True, null=True, db_comment='Base Affected by Previous Taxes')
    analytic = models.BooleanField(blank=True, null=True, db_comment='Include in Analytic Cost')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    formula = models.TextField(blank=True, null=True, db_comment='Formula')
    l10n_in_reverse_charge = models.BooleanField(blank=True, null=True, db_comment='Reverse charge')

    class Meta:
        managed = False
        db_table = 'account_tax'
        db_table_comment = 'Tax'


class AccountTaxFiliationRel(models.Model):
    pk = models.CompositePrimaryKey('parent_tax', 'child_tax')
    parent_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, db_column='parent_tax')
    child_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, db_column='child_tax', related_name='accounttaxfiliationrel_child_tax_set')

    class Meta:
        managed = False
        db_table = 'account_tax_filiation_rel'
        db_table_comment = 'RELATION BETWEEN account_tax AND account_tax'


class AccountTaxGroup(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    tax_payable_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Tax Payable Account')
    tax_receivable_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='accounttaxgroup_tax_receivable_account_set', blank=True, null=True, db_comment='Tax Receivable Account')
    advance_tax_payment_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='accounttaxgroup_advance_tax_payment_account_set', blank=True, null=True, db_comment='Tax Advance Account')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accounttaxgroup_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    pos_receipt_label = models.CharField(blank=True, null=True, db_comment='PoS receipt label')
    name = models.JSONField(db_comment='Name')
    preceding_subtotal = models.JSONField(blank=True, null=True, db_comment='Preceding Subtotal')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'account_tax_group'
        db_table_comment = 'Tax Group'


class AccountTaxHrExpenseSplitRel(models.Model):
    pk = models.CompositePrimaryKey('hr_expense_split_id', 'account_tax_id')
    hr_expense_split = models.ForeignKey('HrExpenseSplit', models.DO_NOTHING)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_hr_expense_split_rel'
        db_table_comment = 'RELATION BETWEEN hr_expense_split AND account_tax'


class AccountTaxPosOrderLineRel(models.Model):
    pk = models.CompositePrimaryKey('pos_order_line_id', 'account_tax_id')
    pos_order_line = models.ForeignKey('PosOrderLine', models.DO_NOTHING)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_pos_order_line_rel'
        db_table_comment = 'RELATION BETWEEN pos_order_line AND account_tax'


class AccountTaxPurchaseOrderLineRel(models.Model):
    pk = models.CompositePrimaryKey('purchase_order_line_id', 'account_tax_id')
    purchase_order_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_purchase_order_line_rel'
        db_table_comment = 'RELATION BETWEEN purchase_order_line AND account_tax'


class AccountTaxRepartitionLine(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Account')
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True, db_comment='Tax')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='accounttaxrepartitionline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    repartition_type = models.CharField(db_comment='Based On')
    document_type = models.CharField(db_comment='Related to')
    use_in_tax_closing = models.BooleanField(blank=True, null=True, db_comment='Tax Closing Entry')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    factor_percent = models.FloatField(db_comment='%')

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_line'
        db_table_comment = 'Tax Repartition Line'


class AccountTaxReportSectionRel(models.Model):
    pk = models.CompositePrimaryKey('main_report_id', 'sub_report_id')
    main_report = models.ForeignKey(AccountReport, models.DO_NOTHING)
    sub_report = models.ForeignKey(AccountReport, models.DO_NOTHING, related_name='accounttaxreportsectionrel_sub_report_set')

    class Meta:
        managed = False
        db_table = 'account_tax_report_section_rel'
        db_table_comment = 'RELATION BETWEEN kit_account_tax_report AND account_report'


class AccountTaxSaleOrderDiscountRel(models.Model):
    pk = models.CompositePrimaryKey('sale_order_discount_id', 'account_tax_id')
    sale_order_discount = models.ForeignKey('SaleOrderDiscount', models.DO_NOTHING)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_sale_order_discount_rel'
        db_table_comment = 'RELATION BETWEEN sale_order_discount AND account_tax'


class AccountTaxSaleOrderLineRel(models.Model):
    pk = models.CompositePrimaryKey('sale_order_line_id', 'account_tax_id')
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_sale_order_line_rel'
        db_table_comment = 'RELATION BETWEEN sale_order_line AND account_tax'


class ActivityAttachmentRel(models.Model):
    pk = models.CompositePrimaryKey('activity_id', 'attachment_id')
    activity = models.ForeignKey('MailActivity', models.DO_NOTHING)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'activity_attachment_rel'
        db_table_comment = 'RELATION BETWEEN mail_activity AND ir_attachment'


class AssetDepreciationConfirmation(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='assetdepreciationconfirmation_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    date = models.DateField(db_comment='Account Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'asset_depreciation_confirmation'
        db_table_comment = 'Asset Depreciation Confirmation'


class AssetModify(models.Model):
    method_number = models.IntegerField(db_comment='Number of Depreciations')
    method_period = models.IntegerField(blank=True, null=True, db_comment='Period Length')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='assetmodify_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    method_end = models.DateField(blank=True, null=True, db_comment='Ending date')
    name = models.TextField(db_comment='Reason')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'asset_modify'
        db_table_comment = 'Modify Asset'


class AuthTotpDevice(models.Model):
    name = models.CharField()
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    scope = models.CharField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    index = models.CharField(max_length=8, blank=True, null=True)
    key = models.CharField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_totp_device'


class AuthTotpWizard(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, db_comment='User')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='authtotpwizard_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='authtotpwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    secret = models.CharField(db_comment='Secret')
    url = models.CharField(blank=True, null=True, db_comment='Url')
    code = models.CharField(max_length=7, blank=True, null=True, db_comment='Verification Code')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    qrcode = models.BinaryField(blank=True, null=True, db_comment='Qrcode')

    class Meta:
        managed = False
        db_table = 'auth_totp_wizard'
        db_table_comment = '2-Factor Setup Wizard'


class BarcodeNomenclature(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='barcodenomenclature_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Barcode Nomenclature')
    upc_ean_conv = models.CharField(db_comment='UPC/EAN Conversion')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    gs1_separator_fnc1 = models.CharField(blank=True, null=True, db_comment='FNC1 Separator')
    is_gs1_nomenclature = models.BooleanField(blank=True, null=True, db_comment='Is GS1 Nomenclature')

    class Meta:
        managed = False
        db_table = 'barcode_nomenclature'
        db_table_comment = 'Barcode Nomenclature'


class BarcodeRule(models.Model):
    barcode_nomenclature = models.ForeignKey(BarcodeNomenclature, models.DO_NOTHING, blank=True, null=True, db_comment='Barcode Nomenclature')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='barcoderule_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Rule Name')
    encoding = models.CharField(db_comment='Encoding')
    type = models.CharField(db_comment='Type')
    pattern = models.CharField(db_comment='Barcode Pattern')
    alias = models.CharField(db_comment='Alias')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    associated_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True, db_comment='Associated Uom')
    gs1_content_type = models.CharField(blank=True, null=True, db_comment='GS1 Content Type')
    gs1_decimal_usage = models.BooleanField(blank=True, null=True, db_comment='Decimal')

    class Meta:
        managed = False
        db_table = 'barcode_rule'
        db_table_comment = 'Barcode Rule'


class BaseDocumentLayout(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    report_layout = models.ForeignKey('ReportLayout', models.DO_NOTHING, blank=True, null=True, db_comment='Report Layout')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='basedocumentlayout_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    from_invoice = models.BooleanField(blank=True, null=True, db_comment='From Invoice')

    class Meta:
        managed = False
        db_table = 'base_document_layout'
        db_table_comment = 'Company Document Layout'


class BaseEnableProfilingWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='baseenableprofilingwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    duration = models.CharField(blank=True, null=True, db_comment='Enable profiling for')
    expiration = models.DateTimeField(blank=True, null=True, db_comment='Enable profiling until')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'base_enable_profiling_wizard'
        db_table_comment = 'Enable profiling for some time'


class BaseImportImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='baseimportimport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    res_model = models.CharField(blank=True, null=True, db_comment='Model')
    file_name = models.CharField(blank=True, null=True, db_comment='File Name')
    file_type = models.CharField(blank=True, null=True, db_comment='File Type')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    file = models.BinaryField(blank=True, null=True, db_comment='File')

    class Meta:
        managed = False
        db_table = 'base_import_import'
        db_table_comment = 'Base Import'


class BaseImportMapping(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='baseimportmapping_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    res_model = models.CharField(blank=True, null=True, db_comment='Res Model')
    column_name = models.CharField(blank=True, null=True, db_comment='Column Name')
    field_name = models.CharField(blank=True, null=True, db_comment='Field Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'base_import_mapping'
        db_table_comment = 'Base Import Mapping'


class BaseImportModule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='baseimportmodule_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    import_message = models.TextField(blank=True, null=True, db_comment='Import Message')
    modules_dependencies = models.TextField(blank=True, null=True, db_comment='Modules Dependencies')
    force = models.BooleanField(blank=True, null=True, db_comment='Force init')
    with_demo = models.BooleanField(blank=True, null=True, db_comment='Import demo data of module')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    module_file = models.BinaryField(db_comment='Module .ZIP file')

    class Meta:
        managed = False
        db_table = 'base_import_module'
        db_table_comment = 'Import Module'


class BaseLanguageExport(models.Model):
    model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True, db_comment='Model to Export')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='baselanguageexport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='File Name')
    lang = models.CharField(db_comment='Language')
    format = models.CharField(db_comment='File Format')
    export_type = models.CharField(db_comment='Export Type')
    domain = models.CharField(blank=True, null=True, db_comment='Model Domain')
    state = models.CharField(blank=True, null=True, db_comment='State')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    data = models.BinaryField(blank=True, null=True, db_comment='File')

    class Meta:
        managed = False
        db_table = 'base_language_export'
        db_table_comment = 'Language Export'


class BaseLanguageImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='baselanguageimport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Language Name')
    code = models.CharField(db_comment='ISO Code')
    filename = models.CharField(db_comment='File Name')
    overwrite = models.BooleanField(blank=True, null=True, db_comment='Overwrite Existing Terms')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    data = models.BinaryField(db_comment='File')

    class Meta:
        managed = False
        db_table = 'base_language_import'
        db_table_comment = 'Language Import'


class BaseLanguageInstall(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='baselanguageinstall_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    overwrite = models.BooleanField(blank=True, null=True, db_comment='Overwrite Existing Terms')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'base_language_install'
        db_table_comment = 'Install Language'


class BaseLanguageInstallWebsiteRel(models.Model):
    pk = models.CompositePrimaryKey('base_language_install_id', 'website_id')
    base_language_install = models.ForeignKey(BaseLanguageInstall, models.DO_NOTHING)
    website = models.ForeignKey('Website', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_language_install_website_rel'
        db_table_comment = 'RELATION BETWEEN base_language_install AND website'


class BaseModuleInstallRequest(models.Model):
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_comment='Module')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, db_comment='User')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='basemoduleinstallrequest_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='basemoduleinstallrequest_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    body_html = models.TextField(blank=True, null=True, db_comment='Body')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'base_module_install_request'
        db_table_comment = 'Module Activation Request'


class BaseModuleInstallReview(models.Model):
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_comment='Module')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='basemoduleinstallreview_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'base_module_install_review'
        db_table_comment = 'Module Activation Review'


class BaseModuleUninstall(models.Model):
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_comment='Module')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='basemoduleuninstall_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    show_all = models.BooleanField(blank=True, null=True, db_comment='Show All')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'base_module_uninstall'
        db_table_comment = 'Module Uninstall'


class BaseModuleUpdate(models.Model):
    updated = models.IntegerField(blank=True, null=True, db_comment='Number of modules updated')
    added = models.IntegerField(blank=True, null=True, db_comment='Number of modules added')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='basemoduleupdate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'base_module_update'
        db_table_comment = 'Update Module'


class BaseModuleUpgrade(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='basemoduleupgrade_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    module_info = models.TextField(blank=True, null=True, db_comment='Apps to Update')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'base_module_upgrade'
        db_table_comment = 'Upgrade Module'


class BasePartnerMergeAutomaticWizard(models.Model):
    number_group = models.IntegerField(blank=True, null=True, db_comment='Group of Contacts')
    current_line = models.ForeignKey('BasePartnerMergeLine', models.DO_NOTHING, blank=True, null=True, db_comment='Current Line')
    dst_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Destination Contact')
    maximum_group = models.IntegerField(blank=True, null=True, db_comment='Maximum of Group of Contacts')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='basepartnermergeautomaticwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    state = models.CharField(db_comment='State')
    group_by_email = models.BooleanField(blank=True, null=True, db_comment='Email')
    group_by_name = models.BooleanField(blank=True, null=True, db_comment='Name')
    group_by_is_company = models.BooleanField(blank=True, null=True, db_comment='Is Company')
    group_by_vat = models.BooleanField(blank=True, null=True, db_comment='VAT')
    group_by_parent_id = models.BooleanField(blank=True, null=True, db_comment='Parent Company')
    exclude_contact = models.BooleanField(blank=True, null=True, db_comment='A user associated to the contact')
    exclude_journal_item = models.BooleanField(blank=True, null=True, db_comment='Journal Items associated to the contact')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard'
        db_table_comment = 'Merge Partner Wizard'


class BasePartnerMergeAutomaticWizardResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('base_partner_merge_automatic_wizard_id', 'res_partner_id')
    base_partner_merge_automatic_wizard = models.ForeignKey(BasePartnerMergeAutomaticWizard, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN base_partner_merge_automatic_wizard AND res_partner'


class BasePartnerMergeLine(models.Model):
    wizard = models.ForeignKey(BasePartnerMergeAutomaticWizard, models.DO_NOTHING, blank=True, null=True, db_comment='Wizard')
    min_id = models.IntegerField(blank=True, null=True, db_comment='MinID')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='basepartnermergeline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    aggr_ids = models.CharField(db_comment='Ids')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'base_partner_merge_line'
        db_table_comment = 'Merge Partner Line'


class BillToPoWizard(models.Model):
    purchase_order = models.ForeignKey('PurchaseOrder', models.DO_NOTHING, blank=True, null=True, db_comment='Purchase Order')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='billtopowizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'bill_to_po_wizard'
        db_table_comment = 'Bill to Purchase Order'


class BlogBlog(models.Model):
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='blogblog_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    website_meta_og_img = models.CharField(blank=True, null=True, db_comment='Website opengraph image')
    website_meta_title = models.JSONField(blank=True, null=True, db_comment='Website meta title')
    website_meta_description = models.JSONField(blank=True, null=True, db_comment='Website meta description')
    website_meta_keywords = models.JSONField(blank=True, null=True, db_comment='Website meta keywords')
    seo_name = models.JSONField(blank=True, null=True, db_comment='Seo name')
    name = models.JSONField(db_comment='Blog Name')
    subtitle = models.JSONField(blank=True, null=True, db_comment='Blog Subtitle')
    content = models.JSONField(blank=True, null=True, db_comment='Content')
    cover_properties = models.TextField(blank=True, null=True, db_comment='Cover Properties')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'blog_blog'
        db_table_comment = 'Blog'


class BlogPost(models.Model):
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Author')
    blog = models.ForeignKey(BlogBlog, models.DO_NOTHING, db_comment='Blog')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='blogpost_write_uid_set', blank=True, null=True, db_comment='Last Contributor')
    visits = models.IntegerField(blank=True, null=True, db_comment='No of Views')
    website_meta_og_img = models.CharField(blank=True, null=True, db_comment='Website opengraph image')
    author_name = models.CharField(blank=True, null=True, db_comment='Author Name')
    website_meta_title = models.JSONField(blank=True, null=True, db_comment='Website meta title')
    website_meta_description = models.JSONField(blank=True, null=True, db_comment='Website meta description')
    website_meta_keywords = models.JSONField(blank=True, null=True, db_comment='Website meta keywords')
    seo_name = models.JSONField(blank=True, null=True, db_comment='Seo name')
    name = models.JSONField(db_comment='Title')
    subtitle = models.JSONField(blank=True, null=True, db_comment='Sub Title')
    content = models.JSONField(blank=True, null=True, db_comment='Content')
    teaser_manual = models.JSONField(blank=True, null=True, db_comment='Teaser Content')
    cover_properties = models.TextField(blank=True, null=True, db_comment='Cover Properties')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    published_date = models.DateTimeField(blank=True, null=True, db_comment='Published Date')
    post_date = models.DateTimeField(blank=True, null=True, db_comment='Publishing date')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'blog_post'
        db_table_comment = 'Blog Post'


class BlogPostBlogTagRel(models.Model):
    pk = models.CompositePrimaryKey('blog_tag_id', 'blog_post_id')
    blog_tag = models.ForeignKey('BlogTag', models.DO_NOTHING)
    blog_post = models.ForeignKey(BlogPost, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post_blog_tag_rel'
        db_table_comment = 'RELATION BETWEEN blog_tag AND blog_post'


class BlogTag(models.Model):
    category = models.ForeignKey('BlogTagCategory', models.DO_NOTHING, blank=True, null=True, db_comment='Category')
    color = models.IntegerField(blank=True, null=True, db_comment='Color')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='blogtag_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    website_meta_og_img = models.CharField(blank=True, null=True, db_comment='Website opengraph image')
    website_meta_title = models.JSONField(blank=True, null=True, db_comment='Website meta title')
    website_meta_description = models.JSONField(blank=True, null=True, db_comment='Website meta description')
    website_meta_keywords = models.JSONField(blank=True, null=True, db_comment='Website meta keywords')
    seo_name = models.JSONField(blank=True, null=True, db_comment='Seo name')
    name = models.JSONField(unique=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'blog_tag'
        db_table_comment = 'Blog Tag'


class BlogTagCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='blogtagcategory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(unique=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'blog_tag_category'
        db_table_comment = 'Blog Tag Category'


class BudgetBudget(models.Model):
    creating_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Responsible')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='budgetbudget_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='budgetbudget_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Budget Name')
    state = models.CharField(db_comment='Status')
    date_from = models.DateField(db_comment='Start Date')
    date_to = models.DateField(db_comment='End Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'budget_budget'
        db_table_comment = 'Budget'


class BudgetLines(models.Model):
    budget = models.ForeignKey(BudgetBudget, models.DO_NOTHING, db_comment='Budget')
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Analytic Account')
    general_budget = models.ForeignKey(AccountBudgetPost, models.DO_NOTHING, db_comment='Budgetary Position')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='budgetlines_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    date_from = models.DateField(db_comment='Start Date')
    date_to = models.DateField(db_comment='End Date')
    paid_date = models.DateField(blank=True, null=True, db_comment='Paid Date')
    planned_amount = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Planned Amount')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'budget_lines'
        db_table_comment = 'Budget Line'


class BusBus(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='busbus_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    channel = models.CharField(blank=True, null=True, db_comment='Channel')
    message = models.CharField(blank=True, null=True, db_comment='Message')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'bus_bus'
        db_table_comment = 'Communication Bus'


class BusPresence(models.Model):
    user = models.OneToOneField('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Users')
    status = models.CharField(blank=True, null=True, db_comment='IM Status')
    last_poll = models.DateTimeField(blank=True, null=True, db_comment='Last Poll')
    last_presence = models.DateTimeField(blank=True, null=True, db_comment='Last Presence')
    guest = models.OneToOneField('MailGuest', models.DO_NOTHING, blank=True, null=True, db_comment='Guest')

    class Meta:
        managed = False
        db_table = 'bus_presence'
        db_table_comment = 'User Presence'


class CashFlowReport(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey(AccountReport, models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='cashflowreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    account_report = models.ForeignKey(AccountFinancialReport, models.DO_NOTHING, db_comment='Account Reports')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    label_filter = models.CharField(blank=True, null=True, db_comment='Column Label')
    filter_cmp = models.CharField(db_comment='Filter by')
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    date_from_cmp = models.DateField(blank=True, null=True, db_comment='Date Start')
    date_to_cmp = models.DateField(blank=True, null=True, db_comment='Date End')
    name = models.JSONField(db_comment='Cash Flow Report')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    enable_filter = models.BooleanField(blank=True, null=True, db_comment='Enable Comparison')
    debit_credit = models.BooleanField(blank=True, null=True, db_comment='Display Debit/Credit Columns')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'cash_flow_report'
        db_table_comment = 'Cash Flow Report'


class ChangePasswordOwn(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='changepasswordown_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    new_password = models.CharField(blank=True, null=True, db_comment='New Password')
    confirm_password = models.CharField(blank=True, null=True, db_comment='New Password (Confirmation)')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'change_password_own'
        db_table_comment = 'User, change own password wizard'


class ChangePasswordUser(models.Model):
    wizard = models.ForeignKey('ChangePasswordWizard', models.DO_NOTHING, db_comment='Wizard')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, db_comment='User')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='changepassworduser_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='changepassworduser_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    user_login = models.CharField(blank=True, null=True, db_comment='User Login')
    new_passwd = models.CharField(blank=True, null=True, db_comment='New Password')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'change_password_user'
        db_table_comment = 'User, Change Password Wizard'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='changepasswordwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'change_password_wizard'
        db_table_comment = 'Change Password Wizard'


class ChangeProductionQty(models.Model):
    mo = models.ForeignKey('MrpProduction', models.DO_NOTHING, db_comment='Manufacturing Order')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='changeproductionqty_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity To Produce')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'change_production_qty'
        db_table_comment = 'Change Production Qty'


class ChatbotMessage(models.Model):
    mail_message = models.OneToOneField('MailMessage', models.DO_NOTHING, db_comment='Related Mail Message')
    discuss_channel = models.ForeignKey('DiscussChannel', models.DO_NOTHING, db_comment='Discussion Channel')
    script_step = models.ForeignKey('ChatbotScriptStep', models.DO_NOTHING, db_comment='Chatbot Step')
    user_script_answer = models.ForeignKey('ChatbotScriptAnswer', models.DO_NOTHING, blank=True, null=True, db_comment="User's answer")
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='chatbotmessage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    user_raw_answer = models.TextField(blank=True, null=True, db_comment="User's raw answer")
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'chatbot_message'
        db_table_comment = 'Chatbot Message'


class ChatbotScript(models.Model):
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, db_comment='Source')
    operator_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Bot Operator')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='chatbotscript_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    title = models.JSONField(db_comment='Title')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'chatbot_script'
        db_table_comment = 'Chatbot Script'


class ChatbotScriptAnswer(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    script_step = models.ForeignKey('ChatbotScriptStep', models.DO_NOTHING, db_comment='Script Step')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='chatbotscriptanswer_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    redirect_link = models.CharField(blank=True, null=True, db_comment='Redirect Link')
    name = models.JSONField(db_comment='Answer')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'chatbot_script_answer'
        db_table_comment = 'Chatbot Script Answer'


class ChatbotScriptAnswerChatbotScriptStepRel(models.Model):
    pk = models.CompositePrimaryKey('chatbot_script_step_id', 'chatbot_script_answer_id')
    chatbot_script_step = models.ForeignKey('ChatbotScriptStep', models.DO_NOTHING)
    chatbot_script_answer = models.ForeignKey(ChatbotScriptAnswer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chatbot_script_answer_chatbot_script_step_rel'
        db_table_comment = 'RELATION BETWEEN chatbot_script_step AND chatbot_script_answer'


class ChatbotScriptStep(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    chatbot_script = models.ForeignKey(ChatbotScript, models.DO_NOTHING, db_comment='Chatbot')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='chatbotscriptstep_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    step_type = models.CharField(db_comment='Step Type')
    message = models.JSONField(blank=True, null=True, db_comment='Message')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'chatbot_script_step'
        db_table_comment = 'Chatbot Script Step'


class ChooseDeliveryCarrier(models.Model):
    order = models.ForeignKey('SaleOrder', models.DO_NOTHING, db_comment='Order')
    carrier = models.ForeignKey('DeliveryCarrier', models.DO_NOTHING, db_comment='Shipping Method')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='choosedeliverycarrier_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    weight_uom_name = models.CharField(blank=True, null=True, db_comment='Weight Uom Name')
    delivery_message = models.TextField(blank=True, null=True, db_comment='Delivery Message')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    delivery_price = models.FloatField(blank=True, null=True, db_comment='Delivery Price')
    display_price = models.FloatField(blank=True, null=True, db_comment='Cost')

    class Meta:
        managed = False
        db_table = 'choose_delivery_carrier'
        db_table_comment = 'Delivery Carrier Selection Wizard'


class ChooseDeliveryPackage(models.Model):
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True, db_comment='Picking')
    delivery_package_type = models.ForeignKey('StockPackageType', models.DO_NOTHING, blank=True, null=True, db_comment='Delivery Package Type')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='choosedeliverypackage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    shipping_weight = models.FloatField(blank=True, null=True, db_comment='Shipping Weight')

    class Meta:
        managed = False
        db_table = 'choose_delivery_package'
        db_table_comment = 'Delivery Package Selection Wizard'


class ConfirmStockSms(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='confirmstocksms_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'confirm_stock_sms'
        db_table_comment = 'Confirm Stock SMS'


class CrmTag(models.Model):
    color = models.IntegerField(blank=True, null=True, db_comment='Color')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='crmtag_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(unique=True, db_comment='Tag Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'crm_tag'
        db_table_comment = 'CRM Tag'


class CrmTeam(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Team Leader')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='crmteam_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='crmteam_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Sales Team')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    invoiced_target = models.FloatField(blank=True, null=True, db_comment='Invoicing Target')

    class Meta:
        managed = False
        db_table = 'crm_team'
        db_table_comment = 'Sales Team'


class CrmTeamMember(models.Model):
    crm_team = models.ForeignKey(CrmTeam, models.DO_NOTHING, db_comment='Sales Team')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, db_comment='Salesperson')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='crmteammember_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='crmteammember_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'crm_team_member'
        db_table_comment = 'Sales Team Member'


class DecimalPrecision(models.Model):
    digits = models.IntegerField(db_comment='Digits')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='decimalprecision_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(unique=True, db_comment='Usage')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'decimal_precision'
        db_table_comment = 'Decimal Precision'


class DeliveryCarrier(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Delivery Product')
    shipping_insurance = models.IntegerField(blank=True, null=True, db_comment='Insurance Percentage')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='deliverycarrier_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    delivery_type = models.CharField(db_comment='Provider')
    integration_level = models.CharField(blank=True, null=True, db_comment='Integration Level')
    tracking_url = models.CharField(blank=True, null=True, db_comment='Tracking Link')
    invoice_policy = models.CharField(db_comment='Invoicing Policy')
    name = models.JSONField(db_comment='Delivery Method')
    carrier_description = models.JSONField(blank=True, null=True, db_comment='Carrier Description')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    prod_environment = models.BooleanField(blank=True, null=True, db_comment='Environment')
    debug_logging = models.BooleanField(blank=True, null=True, db_comment='Debug logging')
    free_over = models.BooleanField(blank=True, null=True, db_comment='Free if order amount is above')
    return_label_on_delivery = models.BooleanField(blank=True, null=True, db_comment='Generate Return Label')
    get_return_label_from_portal = models.BooleanField(blank=True, null=True, db_comment='Return Label Accessible from Customer Portal')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    max_weight = models.FloatField(blank=True, null=True, db_comment='Max Weight')
    max_volume = models.FloatField(blank=True, null=True, db_comment='Max Volume')
    margin = models.FloatField(blank=True, null=True, db_comment='Margin')
    fixed_margin = models.FloatField(blank=True, null=True, db_comment='Fixed Margin')
    amount = models.FloatField(blank=True, null=True, db_comment='Amount')
    fixed_price = models.FloatField(blank=True, null=True, db_comment='Fixed Price')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')

    class Meta:
        managed = False
        db_table = 'delivery_carrier'
        db_table_comment = 'Shipping Methods'


class DeliveryCarrierCountryRel(models.Model):
    pk = models.CompositePrimaryKey('carrier_id', 'country_id')
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'delivery_carrier_country_rel'
        db_table_comment = 'RELATION BETWEEN delivery_carrier AND res_country'


class DeliveryCarrierStateRel(models.Model):
    pk = models.CompositePrimaryKey('carrier_id', 'state_id')
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'delivery_carrier_state_rel'
        db_table_comment = 'RELATION BETWEEN delivery_carrier AND res_country_state'


class DeliveryPriceRule(models.Model):
    sequence = models.IntegerField(db_comment='Sequence')
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING, db_comment='Carrier')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='deliverypricerule_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    variable = models.CharField(db_comment='Variable')
    operator = models.CharField(db_comment='Operator')
    variable_factor = models.CharField(db_comment='Variable Factor')
    list_base_price = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Sale Base Price')
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Sale Price')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    max_value = models.FloatField(db_comment='Maximum Value')

    class Meta:
        managed = False
        db_table = 'delivery_price_rule'
        db_table_comment = 'Delivery Price Rules'


class DeliveryZipPrefix(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='deliveryzipprefix_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(unique=True, db_comment='Prefix')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'delivery_zip_prefix'
        db_table_comment = 'Delivery Zip Prefix'


class DeliveryZipPrefixRel(models.Model):
    pk = models.CompositePrimaryKey('carrier_id', 'zip_prefix_id')
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING)
    zip_prefix = models.ForeignKey(DeliveryZipPrefix, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'delivery_zip_prefix_rel'
        db_table_comment = 'RELATION BETWEEN delivery_carrier AND delivery_zip_prefix'


class DigestDigest(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='digestdigest_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    periodicity = models.CharField(db_comment='Periodicity')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    next_run_date = models.DateField(blank=True, null=True, db_comment='Next Mailing Date')
    name = models.JSONField(db_comment='Name')
    kpi_res_users_connected = models.BooleanField(blank=True, null=True, db_comment='Connected Users')
    kpi_mail_message_total = models.BooleanField(blank=True, null=True, db_comment='Messages Sent')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    kpi_account_total_revenue = models.BooleanField(blank=True, null=True, db_comment='Revenue')
    kpi_website_sale_total = models.BooleanField(blank=True, null=True, db_comment='eCommerce Sales')
    kpi_pos_total = models.BooleanField(blank=True, null=True, db_comment='POS Sales')
    kpi_livechat_rating = models.BooleanField(blank=True, null=True, db_comment='% of Happiness')
    kpi_livechat_conversations = models.BooleanField(blank=True, null=True, db_comment='Conversations handled')
    kpi_livechat_response = models.BooleanField(blank=True, null=True, db_comment='Time to answer (sec)')
    kpi_all_sale_total = models.BooleanField(blank=True, null=True, db_comment='All Sales')

    class Meta:
        managed = False
        db_table = 'digest_digest'
        db_table_comment = 'Digest'


class DigestDigestResUsersRel(models.Model):
    pk = models.CompositePrimaryKey('digest_digest_id', 'res_users_id')
    digest_digest = models.ForeignKey(DigestDigest, models.DO_NOTHING)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'digest_digest_res_users_rel'
        db_table_comment = 'RELATION BETWEEN digest_digest AND res_users'


class DigestTip(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True, db_comment='Authorized Group')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='digesttip_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(blank=True, null=True, db_comment='Name')
    tip_description = models.JSONField(blank=True, null=True, db_comment='Tip description')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'digest_tip'
        db_table_comment = 'Digest Tips'


class DigestTipResUsersRel(models.Model):
    pk = models.CompositePrimaryKey('digest_tip_id', 'res_users_id')
    digest_tip = models.ForeignKey(DigestTip, models.DO_NOTHING)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'digest_tip_res_users_rel'
        db_table_comment = 'RELATION BETWEEN digest_tip AND res_users'


class DiscussChannel(models.Model):
    parent_channel = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Channel')
    from_message = models.OneToOneField('MailMessage', models.DO_NOTHING, blank=True, null=True, db_comment='From Message')
    group_public = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True, db_comment='Authorized Group')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='discusschannel_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    channel_type = models.CharField(db_comment='Channel Type')
    default_display_mode = models.CharField(blank=True, null=True, db_comment='Default Display Mode')
    sfu_channel_uuid = models.CharField(blank=True, null=True, db_comment='Sfu Channel Uuid')
    sfu_server_url = models.CharField(blank=True, null=True, db_comment='Sfu Server Url')
    uuid = models.CharField(unique=True, max_length=50, blank=True, null=True, db_comment='UUID')
    description = models.TextField(blank=True, null=True, db_comment='Description')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    allow_public_upload = models.BooleanField(blank=True, null=True, db_comment='Allow Public Upload')
    last_interest_dt = models.DateTimeField(blank=True, null=True, db_comment='Last Interest')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    livechat_channel = models.ForeignKey('ImLivechatChannel', models.DO_NOTHING, blank=True, null=True, db_comment='Channel')
    livechat_operator = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Operator')
    chatbot_current_step = models.ForeignKey(ChatbotScriptStep, models.DO_NOTHING, blank=True, null=True, db_comment='Chatbot Current Step')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    anonymous_name = models.CharField(blank=True, null=True, db_comment='Anonymous Name')
    livechat_active = models.BooleanField(blank=True, null=True, db_comment='Is livechat ongoing?')
    rating_last_value = models.FloatField(blank=True, null=True, db_comment='Rating Last Value')
    livechat_visitor = models.ForeignKey('WebsiteVisitor', models.DO_NOTHING, blank=True, null=True, db_comment='Visitor')

    class Meta:
        managed = False
        db_table = 'discuss_channel'
        db_table_comment = 'Discussion Channel'


class DiscussChannelHrDepartmentRel(models.Model):
    pk = models.CompositePrimaryKey('discuss_channel_id', 'hr_department_id')
    discuss_channel = models.ForeignKey(DiscussChannel, models.DO_NOTHING)
    hr_department = models.ForeignKey('HrDepartment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discuss_channel_hr_department_rel'
        db_table_comment = 'RELATION BETWEEN discuss_channel AND hr_department'


class DiscussChannelMember(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    guest = models.ForeignKey('MailGuest', models.DO_NOTHING, blank=True, null=True, db_comment='Guest')
    channel = models.ForeignKey(DiscussChannel, models.DO_NOTHING, db_comment='Channel')
    fetched_message = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True, db_comment='Last Fetched')
    seen_message = models.ForeignKey('MailMessage', models.DO_NOTHING, related_name='discusschannelmember_seen_message_set', blank=True, null=True, db_comment='Last Seen')
    new_message_separator = models.IntegerField(db_comment='New Message Separator')
    rtc_inviting_session = models.ForeignKey('DiscussChannelRtcSession', models.DO_NOTHING, blank=True, null=True, db_comment='Ringing session')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='discusschannelmember_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    custom_channel_name = models.CharField(blank=True, null=True, db_comment='Custom channel name')
    fold_state = models.CharField(blank=True, null=True, db_comment='Conversation Fold State')
    custom_notifications = models.CharField(blank=True, null=True, db_comment='Customized Notifications')
    mute_until_dt = models.DateTimeField(blank=True, null=True, db_comment='Mute notifications until')
    unpin_dt = models.DateTimeField(blank=True, null=True, db_comment='Unpin date')
    last_interest_dt = models.DateTimeField(blank=True, null=True, db_comment='Last Interest')
    last_seen_dt = models.DateTimeField(blank=True, null=True, db_comment='Last seen date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'discuss_channel_member'
        unique_together = (('channel', 'guest'), ('channel', 'partner'),)
        db_table_comment = 'Channel Member'


class DiscussChannelResGroupsRel(models.Model):
    pk = models.CompositePrimaryKey('discuss_channel_id', 'res_groups_id')
    discuss_channel = models.ForeignKey(DiscussChannel, models.DO_NOTHING)
    res_groups = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discuss_channel_res_groups_rel'
        db_table_comment = 'RELATION BETWEEN discuss_channel AND res_groups'


class DiscussChannelRtcSession(models.Model):
    channel_member = models.OneToOneField(DiscussChannelMember, models.DO_NOTHING, db_comment='Channel Member')
    channel = models.ForeignKey(DiscussChannel, models.DO_NOTHING, blank=True, null=True, db_comment='Channel')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='discusschannelrtcsession_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    is_screen_sharing_on = models.BooleanField(blank=True, null=True, db_comment='Is sharing the screen')
    is_camera_on = models.BooleanField(blank=True, null=True, db_comment='Is sending user video')
    is_muted = models.BooleanField(blank=True, null=True, db_comment='Is microphone muted')
    is_deaf = models.BooleanField(blank=True, null=True, db_comment='Has disabled incoming sound')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated On')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')

    class Meta:
        managed = False
        db_table = 'discuss_channel_rtc_session'
        db_table_comment = 'Mail RTC session'


class DiscussGifFavorite(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='discussgiffavorite_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    tenor_gif_id = models.CharField(db_comment='GIF id from Tenor')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'discuss_gif_favorite'
        unique_together = (('create_uid', 'tenor_gif_id'),)
        db_table_comment = 'Save favorite GIF from Tenor API'


class DiscussVoiceMetadata(models.Model):
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True, db_comment='Attachment')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='discussvoicemetadata_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'discuss_voice_metadata'
        db_table_comment = 'Metadata for voice attachments'


class EmailTemplateAttachmentRel(models.Model):
    pk = models.CompositePrimaryKey('email_template_id', 'attachment_id')
    email_template = models.ForeignKey('MailTemplate', models.DO_NOTHING)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_attachment_rel'
        db_table_comment = 'RELATION BETWEEN mail_template AND ir_attachment'


class EmployeeCategoryRel(models.Model):
    pk = models.CompositePrimaryKey('employee_id', 'category_id')
    employee = models.ForeignKey('HrEmployee', models.DO_NOTHING)
    category = models.ForeignKey('HrEmployeeCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_category_rel'
        db_table_comment = 'RELATION BETWEEN hr_employee AND hr_employee_category'


class EventEvent(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Responsible')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    organizer = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Organizer')
    event_type = models.ForeignKey('EventType', models.DO_NOTHING, blank=True, null=True, db_comment='Template')
    stage = models.ForeignKey('EventStage', models.DO_NOTHING, blank=True, null=True, db_comment='Stage')
    seats_max = models.IntegerField(blank=True, null=True, db_comment='Maximum Attendees')
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='eventevent_address_set', blank=True, null=True, db_comment='Venue')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='eventevent_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventevent_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    kanban_state = models.CharField(blank=True, null=True, db_comment='Kanban State')
    kanban_state_label = models.CharField(blank=True, null=True, db_comment='Kanban State Label')
    date_tz = models.CharField(db_comment='Display Timezone')
    lang = models.CharField(blank=True, null=True, db_comment='Language')
    badge_format = models.CharField(db_comment='Badge Dimension')
    name = models.JSONField(db_comment='Event')
    description = models.JSONField(blank=True, null=True, db_comment='Description')
    registration_properties_definition = models.JSONField(blank=True, null=True, db_comment='Registration Properties')
    ticket_instructions = models.JSONField(blank=True, null=True, db_comment='Ticket Instructions')
    note = models.TextField(blank=True, null=True, db_comment='Note')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    seats_limited = models.BooleanField(db_comment='Limit Attendees')
    date_begin = models.DateTimeField(db_comment='Start Date')
    date_end = models.DateTimeField(db_comment='End Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    menu = models.ForeignKey('WebsiteMenu', models.DO_NOTHING, blank=True, null=True, db_comment='Event Menu')
    website_meta_og_img = models.CharField(blank=True, null=True, db_comment='Website opengraph image')
    website_visibility = models.CharField(db_comment='Website Visibility')
    website_meta_title = models.JSONField(blank=True, null=True, db_comment='Website meta title')
    website_meta_description = models.JSONField(blank=True, null=True, db_comment='Website meta description')
    website_meta_keywords = models.JSONField(blank=True, null=True, db_comment='Website meta keywords')
    seo_name = models.JSONField(blank=True, null=True, db_comment='Seo name')
    subtitle = models.JSONField(blank=True, null=True, db_comment='Event Subtitle')
    cover_properties = models.TextField(blank=True, null=True, db_comment='Cover Properties')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')
    website_menu = models.BooleanField(blank=True, null=True, db_comment='Website Menu')
    introduction_menu = models.BooleanField(blank=True, null=True, db_comment='Introduction Menu')
    location_menu = models.BooleanField(blank=True, null=True, db_comment='Location Menu')
    register_menu = models.BooleanField(blank=True, null=True, db_comment='Register Menu')
    community_menu = models.BooleanField(blank=True, null=True, db_comment='Community Menu')

    class Meta:
        managed = False
        db_table = 'event_event'
        db_table_comment = 'Event'


class EventEventConfigurator(models.Model):
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    event = models.ForeignKey(EventEvent, models.DO_NOTHING, blank=True, null=True, db_comment='Event')
    event_ticket = models.ForeignKey('EventEventTicket', models.DO_NOTHING, blank=True, null=True, db_comment='Ticket Type')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventeventconfigurator_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'event_event_configurator'
        db_table_comment = 'Event Configurator'


class EventEventEventTagRel(models.Model):
    pk = models.CompositePrimaryKey('event_event_id', 'event_tag_id')
    event_event = models.ForeignKey(EventEvent, models.DO_NOTHING)
    event_tag = models.ForeignKey('EventTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_event_event_tag_rel'
        db_table_comment = 'RELATION BETWEEN event_event AND event_tag'


class EventEventTicket(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    event_type = models.ForeignKey('EventType', models.DO_NOTHING, blank=True, null=True, db_comment='Event Category')
    seats_max = models.IntegerField(blank=True, null=True, db_comment='Maximum Attendees')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventeventticket_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    event = models.ForeignKey(EventEvent, models.DO_NOTHING, db_comment='Event')
    color = models.CharField(blank=True, null=True, db_comment='Color')
    name = models.JSONField(db_comment='Name')
    description = models.JSONField(blank=True, null=True, db_comment='Description')
    seats_limited = models.BooleanField(blank=True, null=True, db_comment='Limit Attendees')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    start_sale_datetime = models.DateTimeField(blank=True, null=True, db_comment='Registration Start')
    end_sale_datetime = models.DateTimeField(blank=True, null=True, db_comment='Registration End')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Product')
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Price')

    class Meta:
        managed = False
        db_table = 'event_event_ticket'
        db_table_comment = 'Event Ticket'


class EventMail(models.Model):
    event = models.ForeignKey(EventEvent, models.DO_NOTHING, db_comment='Event')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Display order')
    interval_nbr = models.IntegerField(blank=True, null=True, db_comment='Interval')
    last_registration = models.ForeignKey('EventRegistration', models.DO_NOTHING, blank=True, null=True, db_comment='Last Attendee')
    mail_count_done = models.IntegerField(blank=True, null=True, db_comment='# Sent')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventmail_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    interval_unit = models.CharField(db_comment='Unit')
    interval_type = models.CharField(db_comment='Trigger ')
    template_ref = models.CharField(db_comment='Template')
    mail_done = models.BooleanField(blank=True, null=True, db_comment='Sent')
    scheduled_date = models.DateTimeField(blank=True, null=True, db_comment='Schedule Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'event_mail'
        db_table_comment = 'Event Automated Mailing'


class EventMailRegistration(models.Model):
    scheduler = models.ForeignKey(EventMail, models.DO_NOTHING, db_comment='Mail Scheduler')
    registration = models.ForeignKey('EventRegistration', models.DO_NOTHING, db_comment='Attendee')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventmailregistration_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    mail_sent = models.BooleanField(blank=True, null=True, db_comment='Mail Sent')
    scheduled_date = models.DateTimeField(blank=True, null=True, db_comment='Scheduled Time')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'event_mail_registration'
        db_table_comment = 'Registration Mail Scheduler'


class EventQuestion(models.Model):
    event_type = models.ForeignKey('EventType', models.DO_NOTHING, blank=True, null=True, db_comment='Event Type')
    event = models.ForeignKey(EventEvent, models.DO_NOTHING, blank=True, null=True, db_comment='Event')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventquestion_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    question_type = models.CharField(db_comment='Question Type')
    title = models.JSONField(db_comment='Title')
    once_per_order = models.BooleanField(blank=True, null=True, db_comment='Ask once per order')
    is_mandatory_answer = models.BooleanField(blank=True, null=True, db_comment='Mandatory Answer')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'event_question'
        db_table_comment = 'Event Question'


class EventQuestionAnswer(models.Model):
    question = models.ForeignKey(EventQuestion, models.DO_NOTHING, db_comment='Question')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventquestionanswer_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Answer')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'event_question_answer'
        db_table_comment = 'Event Question Answer'


class EventRegistration(models.Model):
    event = models.ForeignKey(EventEvent, models.DO_NOTHING, db_comment='Event')
    event_ticket = models.ForeignKey(EventEventTicket, models.DO_NOTHING, blank=True, null=True, db_comment='Ticket Type')
    utm_campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True, db_comment='Campaign')
    utm_source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True, db_comment='Source')
    utm_medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True, db_comment='Medium')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Booked by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventregistration_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    barcode = models.CharField(unique=True, blank=True, null=True, db_comment='Barcode')
    name = models.CharField(blank=True, null=True, db_comment='Attendee Name')
    email = models.CharField(blank=True, null=True, db_comment='Email')
    phone = models.CharField(blank=True, null=True, db_comment='Phone')
    company_name = models.CharField(blank=True, null=True, db_comment='Company Name')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    registration_properties = models.JSONField(blank=True, null=True, db_comment='Properties')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    date_closed = models.DateTimeField(blank=True, null=True, db_comment='Attended Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    visitor = models.ForeignKey('WebsiteVisitor', models.DO_NOTHING, blank=True, null=True, db_comment='Visitor')
    pos_order_line = models.ForeignKey('PosOrderLine', models.DO_NOTHING, blank=True, null=True, db_comment='PoS Order Line')
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True, db_comment='Sales Order')
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True, db_comment='Sales Order Line')
    sale_status = models.CharField(blank=True, null=True, db_comment='Sale Status')

    class Meta:
        managed = False
        db_table = 'event_registration'
        db_table_comment = 'Event Registration'


class EventRegistrationAnswer(models.Model):
    question = models.ForeignKey(EventQuestion, models.DO_NOTHING, db_comment='Question')
    registration = models.ForeignKey(EventRegistration, models.DO_NOTHING, db_comment='Registration')
    value_answer = models.ForeignKey(EventQuestionAnswer, models.DO_NOTHING, blank=True, null=True, db_comment='Suggested answer')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventregistrationanswer_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    value_text_box = models.TextField(blank=True, null=True, db_comment='Text answer')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'event_registration_answer'
        db_table_comment = 'Event Registration Answer'


class EventStage(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventstage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Stage Name')
    description = models.JSONField(blank=True, null=True, db_comment='Stage description')
    legend_blocked = models.JSONField(db_comment='Red Kanban Label')
    legend_done = models.JSONField(db_comment='Green Kanban Label')
    legend_normal = models.JSONField(db_comment='Grey Kanban Label')
    fold = models.BooleanField(blank=True, null=True, db_comment='Folded in Kanban')
    pipe_end = models.BooleanField(blank=True, null=True, db_comment='End Stage')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'event_stage'
        db_table_comment = 'Event Stage'


class EventTag(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    category = models.ForeignKey('EventTagCategory', models.DO_NOTHING, db_comment='Category')
    category_sequence = models.IntegerField(blank=True, null=True, db_comment='Category Sequence')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventtag_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')

    class Meta:
        managed = False
        db_table = 'event_tag'
        db_table_comment = 'Event Tag'


class EventTagCategory(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventtagcategory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')

    class Meta:
        managed = False
        db_table = 'event_tag_category'
        db_table_comment = 'Event Tag Category'


class EventTagEventTypeRel(models.Model):
    pk = models.CompositePrimaryKey('event_type_id', 'event_tag_id')
    event_type = models.ForeignKey('EventType', models.DO_NOTHING)
    event_tag = models.ForeignKey(EventTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_tag_event_type_rel'
        db_table_comment = 'RELATION BETWEEN event_type AND event_tag'


class EventType(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    seats_max = models.IntegerField(blank=True, null=True, db_comment='Maximum Registrations')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventtype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    default_timezone = models.CharField(blank=True, null=True, db_comment='Timezone')
    name = models.JSONField(db_comment='Event Template')
    ticket_instructions = models.JSONField(blank=True, null=True, db_comment='Ticket Instructions')
    note = models.TextField(blank=True, null=True, db_comment='Note')
    has_seats_limitation = models.BooleanField(blank=True, null=True, db_comment='Limited Seats')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    website_menu = models.BooleanField(blank=True, null=True, db_comment='Display a dedicated menu on Website')
    community_menu = models.BooleanField(blank=True, null=True, db_comment='Community Menu')

    class Meta:
        managed = False
        db_table = 'event_type'
        db_table_comment = 'Event Template'


class EventTypeMail(models.Model):
    event_type = models.ForeignKey(EventType, models.DO_NOTHING, db_comment='Event Type')
    interval_nbr = models.IntegerField(blank=True, null=True, db_comment='Interval')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventtypemail_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    interval_unit = models.CharField(db_comment='Unit')
    interval_type = models.CharField(db_comment='Trigger')
    template_ref = models.CharField(db_comment='Template')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'event_type_mail'
        db_table_comment = 'Mail Scheduling on Event Category'


class EventTypeTicket(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    event_type = models.ForeignKey(EventType, models.DO_NOTHING, db_comment='Event Category')
    seats_max = models.IntegerField(blank=True, null=True, db_comment='Maximum Attendees')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='eventtypeticket_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    description = models.JSONField(blank=True, null=True, db_comment='Description')
    seats_limited = models.BooleanField(blank=True, null=True, db_comment='Limit Attendees')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Product')
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Price')

    class Meta:
        managed = False
        db_table = 'event_type_ticket'
        db_table_comment = 'Event Template Ticket'


class ExpenseTax(models.Model):
    pk = models.CompositePrimaryKey('expense_id', 'tax_id')
    expense = models.ForeignKey('HrExpense', models.DO_NOTHING)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'expense_tax'
        db_table_comment = 'RELATION BETWEEN hr_expense AND account_tax'


class FetchmailServer(models.Model):
    port = models.IntegerField(blank=True, null=True, db_comment='Port')
    object = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True, db_comment='Create a New Record')
    priority = models.IntegerField(blank=True, null=True, db_comment='Server Priority')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='fetchmailserver_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    server = models.CharField(blank=True, null=True, db_comment='Server Name')
    server_type = models.CharField(db_comment='Server Type')
    user = models.CharField(blank=True, null=True, db_comment='Username')
    password = models.CharField(blank=True, null=True, db_comment='Password')
    script = models.CharField(blank=True, null=True, db_comment='Script')
    configuration = models.TextField(blank=True, null=True, db_comment='Configuration')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    is_ssl = models.BooleanField(blank=True, null=True, db_comment='SSL/TLS')
    attach = models.BooleanField(blank=True, null=True, db_comment='Keep Attachments')
    original = models.BooleanField(blank=True, null=True, db_comment='Keep Original')
    date = models.DateTimeField(blank=True, null=True, db_comment='Last Fetch Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    google_gmail_access_token_expiration = models.IntegerField(blank=True, null=True, db_comment='Access Token Expiration Timestamp')
    google_gmail_authorization_code = models.CharField(blank=True, null=True, db_comment='Authorization Code')
    google_gmail_refresh_token = models.CharField(blank=True, null=True, db_comment='Refresh Token')
    google_gmail_access_token = models.CharField(blank=True, null=True, db_comment='Access Token')

    class Meta:
        managed = False
        db_table = 'fetchmail_server'
        db_table_comment = 'Incoming Mail Server'


class FinancialReport(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey(AccountReport, models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='financialreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    account_report = models.ForeignKey(AccountFinancialReport, models.DO_NOTHING, db_comment='Account Reports')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    view_format = models.CharField(blank=True, null=True, db_comment='Format')
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    name = models.JSONField(db_comment='Financial Report')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    enable_filter = models.BooleanField(blank=True, null=True, db_comment='Enable Comparison')
    debit_credit = models.BooleanField(blank=True, null=True, db_comment='Display Debit/Credit Columns')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'financial_report'
        db_table_comment = 'Financial Reports'


class FollowupLine(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    delay = models.IntegerField(db_comment='Due Days')
    followup = models.ForeignKey(AccountFollowup, models.DO_NOTHING, blank=True, null=True, db_comment='Follow Ups')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='followupline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Follow-Up Action')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'followup_line'
        db_table_comment = 'Follow-up Criteria'


class HeaderFooterQuotationTemplateRel(models.Model):
    pk = models.CompositePrimaryKey('quotation_document_id', 'sale_order_template_id')
    quotation_document = models.ForeignKey('QuotationDocument', models.DO_NOTHING)
    sale_order_template = models.ForeignKey('SaleOrderTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'header_footer_quotation_template_rel'
        db_table_comment = 'RELATION BETWEEN quotation_document AND sale_order_template'


class HrContractType(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrcontracttype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code = models.CharField(blank=True, null=True, db_comment='Code')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_contract_type'
        db_table_comment = 'Contract Type'


class HrDepartment(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Department')
    manager = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True, db_comment='Manager')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    master_department = models.ForeignKey('self', models.DO_NOTHING, related_name='hrdepartment_master_department_set', blank=True, null=True, db_comment='Master Department')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrdepartment_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    complete_name = models.CharField(blank=True, null=True, db_comment='Complete Name')
    parent_path = models.CharField(blank=True, null=True, db_comment='Parent Path')
    name = models.JSONField(db_comment='Department Name')
    note = models.TextField(blank=True, null=True, db_comment='Note')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_department'
        db_table_comment = 'Department'


class HrDepartureReason(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    reason_code = models.IntegerField(blank=True, null=True, db_comment='Reason Code')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrdeparturereason_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Reason')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_departure_reason'
        db_table_comment = 'Departure Reason'


class HrDepartureWizard(models.Model):
    departure_reason = models.ForeignKey(HrDepartureReason, models.DO_NOTHING, db_comment='Departure Reason')
    employee = models.ForeignKey('HrEmployee', models.DO_NOTHING, db_comment='Employee')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrdeparturewizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    departure_date = models.DateField(db_comment='Departure Date')
    departure_description = models.TextField(blank=True, null=True, db_comment='Additional Information')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_departure_wizard'
        db_table_comment = 'Departure Wizard'


class HrEmployee(models.Model):
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, db_comment='Resource')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True, db_comment='Working Hours')
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True, db_comment='Main Attachment')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True, db_comment='Department')
    job = models.ForeignKey('HrJob', models.DO_NOTHING, blank=True, null=True, db_comment='Job Position')
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Work Address')
    work_contact = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='hremployee_work_contact_set', blank=True, null=True, db_comment='Work Contact')
    work_location = models.ForeignKey('HrWorkLocation', models.DO_NOTHING, blank=True, null=True, db_comment='Work Location')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='User')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Manager')
    coach = models.ForeignKey('self', models.DO_NOTHING, related_name='hremployee_coach_set', blank=True, null=True, db_comment='Coach')
    private_state = models.ForeignKey('ResCountryState', models.DO_NOTHING, blank=True, null=True, db_comment='Private State')
    private_country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Private Country')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name='hremployee_country_set', blank=True, null=True, db_comment='Nationality (Country)')
    children = models.IntegerField(blank=True, null=True, db_comment='Number of Dependent Children')
    country_of_birth = models.ForeignKey('ResCountry', models.DO_NOTHING, db_column='country_of_birth', related_name='hremployee_country_of_birth_set', blank=True, null=True, db_comment='Country of Birth')
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True, db_comment='Bank Account')
    distance_home_work = models.IntegerField(blank=True, null=True, db_comment='Home-Work Distance')
    km_home_work = models.IntegerField(blank=True, null=True, db_comment='Home-Work Distance in Km')
    departure_reason = models.ForeignKey(HrDepartureReason, models.DO_NOTHING, blank=True, null=True, db_comment='Departure Reason')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='hremployee_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hremployee_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Employee Name')
    job_title = models.CharField(blank=True, null=True, db_comment='Job Title')
    work_phone = models.CharField(blank=True, null=True, db_comment='Work Phone')
    mobile_phone = models.CharField(blank=True, null=True, db_comment='Work Mobile')
    work_email = models.CharField(blank=True, null=True, db_comment='Work Email')
    private_street = models.CharField(blank=True, null=True, db_comment='Private Street')
    private_street2 = models.CharField(blank=True, null=True, db_comment='Private Street2')
    private_city = models.CharField(blank=True, null=True, db_comment='Private City')
    private_zip = models.CharField(blank=True, null=True, db_comment='Private Zip')
    private_phone = models.CharField(blank=True, null=True, db_comment='Private Phone')
    private_email = models.CharField(blank=True, null=True, db_comment='Private Email')
    lang = models.CharField(blank=True, null=True, db_comment='Lang')
    gender = models.CharField(blank=True, null=True, db_comment='Gender')
    marital = models.CharField(db_comment='Marital Status')
    spouse_complete_name = models.CharField(blank=True, null=True, db_comment='Spouse Complete Name')
    place_of_birth = models.CharField(blank=True, null=True, db_comment='Place of Birth')
    ssnid = models.CharField(blank=True, null=True, db_comment='SSN No')
    sinid = models.CharField(blank=True, null=True, db_comment='SIN No')
    identification_id = models.CharField(blank=True, null=True, db_comment='Identification No')
    passport_id = models.CharField(blank=True, null=True, db_comment='Passport No')
    permit_no = models.CharField(blank=True, null=True, db_comment='Work Permit No')
    visa_no = models.CharField(blank=True, null=True, db_comment='Visa No')
    certificate = models.CharField(blank=True, null=True, db_comment='Certificate Level')
    study_field = models.CharField(blank=True, null=True, db_comment='Field of Study')
    study_school = models.CharField(blank=True, null=True, db_comment='School')
    emergency_contact = models.CharField(blank=True, null=True, db_comment='Contact Name')
    emergency_phone = models.CharField(blank=True, null=True, db_comment='Contact Phone')
    distance_home_work_unit = models.CharField(db_comment='Home-Work Distance unit')
    employee_type = models.CharField(db_comment='Employee Type')
    barcode = models.CharField(unique=True, blank=True, null=True, db_comment='Badge ID')
    pin = models.CharField(blank=True, null=True, db_comment='PIN')
    private_car_plate = models.CharField(blank=True, null=True, db_comment='Private Car Plate')
    spouse_birthdate = models.DateField(blank=True, null=True, db_comment='Spouse Birthdate')
    birthday = models.DateField(blank=True, null=True, db_comment='Date of Birth')
    visa_expire = models.DateField(blank=True, null=True, db_comment='Visa Expiration Date')
    work_permit_expiration_date = models.DateField(blank=True, null=True, db_comment='Work Permit Expiration Date')
    departure_date = models.DateField(blank=True, null=True, db_comment='Departure Date')
    employee_properties = models.JSONField(blank=True, null=True, db_comment='Properties')
    additional_note = models.TextField(blank=True, null=True, db_comment='Additional Note')
    notes = models.TextField(blank=True, null=True, db_comment='Notes')
    departure_description = models.TextField(blank=True, null=True, db_comment='Additional Information')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    is_flexible = models.BooleanField(blank=True, null=True, db_comment='Is Flexible')
    is_fully_flexible = models.BooleanField(blank=True, null=True, db_comment='Is Fully Flexible')
    work_permit_scheduled_activity = models.BooleanField(blank=True, null=True, db_comment='Work Permit Scheduled Activity')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    expense_manager = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='hremployee_expense_manager_set', blank=True, null=True, db_comment='Expense')

    class Meta:
        managed = False
        db_table = 'hr_employee'
        unique_together = (('user', 'company'),)
        db_table_comment = 'Employee'


class HrEmployeeCategory(models.Model):
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hremployeecategory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(unique=True, db_comment='Tag Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_employee_category'
        db_table_comment = 'Employee Category'


class HrEmployeeCvWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hremployeecvwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    color_primary = models.CharField(db_comment='Primary Color')
    color_secondary = models.CharField(db_comment='Secondary Color')
    show_skills = models.BooleanField(blank=True, null=True, db_comment='Skills')
    show_contact = models.BooleanField(blank=True, null=True, db_comment='Contact Information')
    show_others = models.BooleanField(blank=True, null=True, db_comment='Others')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_employee_cv_wizard'
        db_table_comment = 'Print Resume'


class HrEmployeeHrEmployeeCvWizardRel(models.Model):
    pk = models.CompositePrimaryKey('hr_employee_cv_wizard_id', 'hr_employee_id')
    hr_employee_cv_wizard = models.ForeignKey(HrEmployeeCvWizard, models.DO_NOTHING)
    hr_employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_employee_hr_employee_cv_wizard_rel'
        db_table_comment = 'RELATION BETWEEN hr_employee_cv_wizard AND hr_employee'


class HrEmployeeHrSkillRel(models.Model):
    pk = models.CompositePrimaryKey('hr_employee_id', 'hr_skill_id')
    hr_employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)
    hr_skill = models.ForeignKey('HrSkill', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_employee_hr_skill_rel'
        db_table_comment = 'RELATION BETWEEN hr_employee AND hr_skill'


class HrEmployeeSkill(models.Model):
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, db_comment='Employee')
    skill = models.ForeignKey('HrSkill', models.DO_NOTHING, db_comment='Skill')
    skill_level = models.ForeignKey('HrSkillLevel', models.DO_NOTHING, db_comment='Skill Level')
    skill_type = models.ForeignKey('HrSkillType', models.DO_NOTHING, db_comment='Skill Type')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hremployeeskill_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_employee_skill'
        unique_together = (('employee', 'skill'),)
        db_table_comment = 'Skill level for an employee'


class HrEmployeeSkillLog(models.Model):
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, db_comment='Employee')
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True, db_comment='Department')
    skill = models.ForeignKey('HrSkill', models.DO_NOTHING, db_comment='Skill')
    skill_level = models.ForeignKey('HrSkillLevel', models.DO_NOTHING, db_comment='Skill Level')
    skill_type = models.ForeignKey('HrSkillType', models.DO_NOTHING, db_comment='Skill Type')
    level_progress = models.IntegerField(blank=True, null=True, db_comment='Progress')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hremployeeskilllog_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    date = models.DateField(blank=True, null=True, db_comment='Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_employee_skill_log'
        unique_together = (('employee', 'department', 'skill', 'date'),)
        db_table_comment = 'Skills History'


class HrExpense(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True, db_comment='Main Attachment')
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, db_comment='Employee')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True, db_comment='Category')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True, db_comment='Unit of Measure')
    sheet = models.ForeignKey('HrExpenseSheet', models.DO_NOTHING, blank=True, null=True, db_comment='Expense Report')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, db_comment='Currency')
    vendor = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Vendor')
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Account')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrexpense_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Description')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    payment_mode = models.CharField(db_comment='Paid By')
    date = models.DateField(blank=True, null=True, db_comment='Expense Date')
    accounting_date = models.DateField(blank=True, null=True, db_comment='Accounting Date')
    analytic_distribution = models.JSONField(blank=True, null=True, db_comment='Analytic Distribution')
    description = models.TextField(blank=True, null=True, db_comment='Internal Notes')
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    tax_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Tax amount in Currency')
    tax_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Tax amount')
    total_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total In Currency')
    untaxed_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total Untaxed Amount In Currency')
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total')
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Unit Price')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True, db_comment='Customer to Reinvoice')

    class Meta:
        managed = False
        db_table = 'hr_expense'
        db_table_comment = 'Expense'


class HrExpenseApproveDuplicate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrexpenseapproveduplicate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_expense_approve_duplicate'
        db_table_comment = 'Expense Approve Duplicate'


class HrExpenseApproveDuplicateHrExpenseSheetRel(models.Model):
    pk = models.CompositePrimaryKey('hr_expense_approve_duplicate_id', 'hr_expense_sheet_id')
    hr_expense_approve_duplicate = models.ForeignKey(HrExpenseApproveDuplicate, models.DO_NOTHING)
    hr_expense_sheet = models.ForeignKey('HrExpenseSheet', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_expense_approve_duplicate_hr_expense_sheet_rel'
        db_table_comment = 'RELATION BETWEEN hr_expense_approve_duplicate AND hr_expense_sheet'


class HrExpenseHrExpenseApproveDuplicateRel(models.Model):
    pk = models.CompositePrimaryKey('hr_expense_approve_duplicate_id', 'hr_expense_id')
    hr_expense_approve_duplicate = models.ForeignKey(HrExpenseApproveDuplicate, models.DO_NOTHING)
    hr_expense = models.ForeignKey(HrExpense, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_expense_hr_expense_approve_duplicate_rel'
        db_table_comment = 'RELATION BETWEEN hr_expense_approve_duplicate AND hr_expense'


class HrExpenseRefuseWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrexpenserefusewizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    reason = models.CharField(db_comment='Reason')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_expense_refuse_wizard'
        db_table_comment = 'Expense Refuse Reason Wizard'


class HrExpenseRefuseWizardHrExpenseSheetRel(models.Model):
    pk = models.CompositePrimaryKey('hr_expense_refuse_wizard_id', 'hr_expense_sheet_id')
    hr_expense_refuse_wizard = models.ForeignKey(HrExpenseRefuseWizard, models.DO_NOTHING)
    hr_expense_sheet = models.ForeignKey('HrExpenseSheet', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_expense_refuse_wizard_hr_expense_sheet_rel'
        db_table_comment = 'RELATION BETWEEN hr_expense_refuse_wizard AND hr_expense_sheet'


class HrExpenseSheet(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True, db_comment='Main Attachment')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, db_comment='Employee')
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True, db_comment='Department')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Manager')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    employee_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Journal')
    payment_method_line = models.ForeignKey(AccountPaymentMethodLine, models.DO_NOTHING, blank=True, null=True, db_comment='Payment Method')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, related_name='hrexpensesheet_journal_set', blank=True, null=True, db_comment='Expense Journal')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='hrexpensesheet_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrexpensesheet_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Expense Report Summary')
    state = models.CharField(db_comment='Status')
    approval_state = models.CharField(blank=True, null=True, db_comment='Approval State')
    payment_state = models.CharField(blank=True, null=True, db_comment='Payment Status')
    accounting_date = models.DateField(blank=True, null=True, db_comment='Expense Report Date')
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total')
    untaxed_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Untaxed Amount')
    total_tax_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Taxes')
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount Due')
    approval_date = models.DateTimeField(blank=True, null=True, db_comment='Approval Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_expense_sheet'
        db_table_comment = 'Expense Report'


class HrExpenseSplit(models.Model):
    wizard = models.ForeignKey('HrExpenseSplitWizard', models.DO_NOTHING, blank=True, null=True, db_comment='Wizard')
    expense = models.ForeignKey(HrExpense, models.DO_NOTHING, blank=True, null=True, db_comment='Expense')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Product')
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, db_comment='Employee')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrexpensesplit_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Description')
    analytic_distribution = models.JSONField(blank=True, null=True, db_comment='Analytic Distribution')
    total_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Total In Currency')
    product_has_cost = models.BooleanField(blank=True, null=True, db_comment='Is product with non zero cost selected')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True, db_comment='Customer to Reinvoice')

    class Meta:
        managed = False
        db_table = 'hr_expense_split'
        db_table_comment = 'Expense Split'


class HrExpenseSplitWizard(models.Model):
    expense = models.ForeignKey(HrExpense, models.DO_NOTHING, db_comment='Expense')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrexpensesplitwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_expense_split_wizard'
        db_table_comment = 'Expense Split Wizard'


class HrJob(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    expected_employees = models.IntegerField(blank=True, null=True, db_comment='Total Forecasted Employees')
    no_of_employee = models.IntegerField(blank=True, null=True, db_comment='Current Number of Employees')
    no_of_recruitment = models.IntegerField(blank=True, null=True, db_comment='Target')
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True, db_comment='Department')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    contract_type = models.ForeignKey(HrContractType, models.DO_NOTHING, blank=True, null=True, db_comment='Employment Type')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrjob_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Job Position')
    description = models.TextField(blank=True, null=True, db_comment='Job Description')
    requirements = models.TextField(blank=True, null=True, db_comment='Requirements')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_job'
        unique_together = (('name', 'company', 'department'),)
        db_table_comment = 'Job Position'


class HrResumeLine(models.Model):
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, db_comment='Employee')
    line_type = models.ForeignKey('HrResumeLineType', models.DO_NOTHING, blank=True, null=True, db_comment='Type')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrresumeline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    display_type = models.CharField(blank=True, null=True, db_comment='Display Type')
    date_start = models.DateField(db_comment='Date Start')
    date_end = models.DateField(blank=True, null=True, db_comment='Date End')
    name = models.JSONField(db_comment='Name')
    description = models.JSONField(blank=True, null=True, db_comment='Description')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_resume_line'
        db_table_comment = 'Resume line of an employee'


class HrResumeLineType(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrresumelinetype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_resume_line_type'
        db_table_comment = 'Type of a resume line'


class HrSkill(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    skill_type = models.ForeignKey('HrSkillType', models.DO_NOTHING, db_comment='Skill Type')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrskill_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_skill'
        db_table_comment = 'Skill'


class HrSkillLevel(models.Model):
    skill_type = models.ForeignKey('HrSkillType', models.DO_NOTHING, blank=True, null=True, db_comment='Skill Type')
    level_progress = models.IntegerField(blank=True, null=True, db_comment='Progress')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrskilllevel_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    default_level = models.BooleanField(blank=True, null=True, db_comment='Default Level')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_skill_level'
        db_table_comment = 'Skill Level'


class HrSkillType(models.Model):
    color = models.IntegerField(blank=True, null=True, db_comment='Color')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrskilltype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_skill_type'
        db_table_comment = 'Skill Type'


class HrWorkLocation(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Work Address')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='hrworklocation_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Work Location')
    location_type = models.CharField(db_comment='Cover Image')
    location_number = models.CharField(blank=True, null=True, db_comment='Location Number')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'hr_work_location'
        db_table_comment = 'Work Location'


class IapAccount(models.Model):
    service = models.ForeignKey('IapService', models.DO_NOTHING, db_comment='Service')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iapaccount_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    account_token = models.CharField(max_length=43, blank=True, null=True, db_comment='Account Token')
    balance = models.CharField(blank=True, null=True, db_comment='Balance')
    state = models.CharField(blank=True, null=True, db_comment='State')
    service_locked = models.BooleanField(blank=True, null=True, db_comment='Service Locked')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    warning_threshold = models.FloatField(blank=True, null=True, db_comment='Email Alert Threshold')
    sender_name = models.CharField(blank=True, null=True, db_comment='Sender Name')

    class Meta:
        managed = False
        db_table = 'iap_account'
        db_table_comment = 'IAP Account'


class IapAccountResCompanyRel(models.Model):
    pk = models.CompositePrimaryKey('iap_account_id', 'res_company_id')
    iap_account = models.ForeignKey(IapAccount, models.DO_NOTHING)
    res_company = models.ForeignKey('ResCompany', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iap_account_res_company_rel'
        db_table_comment = 'RELATION BETWEEN iap_account AND res_company'


class IapAccountResUsersRel(models.Model):
    pk = models.CompositePrimaryKey('iap_account_id', 'res_users_id')
    iap_account = models.ForeignKey(IapAccount, models.DO_NOTHING)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iap_account_res_users_rel'
        db_table_comment = 'RELATION BETWEEN iap_account AND res_users'


class IapService(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iapservice_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    technical_name = models.CharField(unique=True, db_comment='Technical Name')
    description = models.JSONField(db_comment='Description')
    unit_name = models.JSONField(db_comment='Unit Name')
    integer_balance = models.BooleanField(db_comment='Integer Balance')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'iap_service'
        db_table_comment = 'IAP Service'


class ImLivechatChannel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='imlivechatchannel_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Channel Name')
    header_background_color = models.CharField(blank=True, null=True, db_comment='Header Background Color')
    title_color = models.CharField(blank=True, null=True, db_comment='Title Color')
    button_background_color = models.CharField(blank=True, null=True, db_comment='Button Background Color')
    button_text_color = models.CharField(blank=True, null=True, db_comment='Button Text Color')
    button_text = models.JSONField(blank=True, null=True, db_comment='Text of the Button')
    default_message = models.JSONField(blank=True, null=True, db_comment='Welcome Message')
    input_placeholder = models.JSONField(blank=True, null=True, db_comment='Chat Input Placeholder')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    website_description = models.JSONField(blank=True, null=True, db_comment='Website description')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')

    class Meta:
        managed = False
        db_table = 'im_livechat_channel'
        db_table_comment = 'Livechat Channel'


class ImLivechatChannelCountryRel(models.Model):
    pk = models.CompositePrimaryKey('channel_id', 'country_id')
    channel = models.ForeignKey('ImLivechatChannelRule', models.DO_NOTHING)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'im_livechat_channel_country_rel'
        db_table_comment = 'RELATION BETWEEN im_livechat_channel_rule AND res_country'


class ImLivechatChannelImUser(models.Model):
    pk = models.CompositePrimaryKey('channel_id', 'user_id')
    channel = models.ForeignKey(ImLivechatChannel, models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'im_livechat_channel_im_user'
        db_table_comment = 'RELATION BETWEEN im_livechat_channel AND res_users'


class ImLivechatChannelRule(models.Model):
    auto_popup_timer = models.IntegerField(blank=True, null=True, db_comment='Open automatically timer')
    chatbot_script = models.ForeignKey(ChatbotScript, models.DO_NOTHING, blank=True, null=True, db_comment='Chatbot')
    channel = models.ForeignKey(ImLivechatChannel, models.DO_NOTHING, blank=True, null=True, db_comment='Channel')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Matching order')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='imlivechatchannelrule_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    regex_url = models.CharField(blank=True, null=True, db_comment='URL Regex')
    action = models.CharField(db_comment='Live Chat Button')
    chatbot_only_if_no_operator = models.BooleanField(blank=True, null=True, db_comment='Enabled only if no operator')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'im_livechat_channel_rule'
        db_table_comment = 'Livechat Channel Rules'


class ImportBankStatement(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Journal ID')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='importbankstatement_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    file_name = models.CharField(blank=True, null=True, db_comment='File Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'import_bank_statement'
        db_table_comment = 'Import button'


class IrActClient(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iractclient_write_uid_set', blank=True, null=True)
    type = models.CharField()
    path = models.CharField(unique=True, blank=True, null=True)
    binding_type = models.CharField()
    binding_view_types = models.CharField(blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(db_comment='Client action tag')
    target = models.CharField(blank=True, null=True, db_comment='Target Window')
    res_model = models.CharField(blank=True, null=True, db_comment='Destination Model')
    context = models.CharField(db_comment='Context Value')
    params_store = models.BinaryField(blank=True, null=True, db_comment='Params storage')

    class Meta:
        managed = False
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iractreportxml_write_uid_set', blank=True, null=True)
    type = models.CharField()
    path = models.CharField(unique=True, blank=True, null=True)
    binding_type = models.CharField()
    binding_view_types = models.CharField(blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING, blank=True, null=True, db_comment='Paper Format')
    model = models.CharField(db_comment='Model Name')
    report_type = models.CharField(db_comment='Report Type')
    report_name = models.CharField(db_comment='Template Name')
    report_file = models.CharField(blank=True, null=True, db_comment='Report File')
    attachment = models.CharField(blank=True, null=True, db_comment='Save as Attachment Prefix')
    domain = models.CharField(blank=True, null=True, db_comment='Filter domain')
    print_report_name = models.JSONField(blank=True, null=True, db_comment='Printed Report Name')
    multi = models.BooleanField(blank=True, null=True, db_comment='On Multiple Doc.')
    attachment_use = models.BooleanField(blank=True, null=True, db_comment='Reload from Attachment')
    is_invoice_report = models.BooleanField(blank=True, null=True, db_comment='Invoice report')

    class Meta:
        managed = False
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iractserver_write_uid_set', blank=True, null=True)
    type = models.CharField()
    path = models.CharField(unique=True, blank=True, null=True)
    binding_type = models.CharField()
    binding_view_types = models.CharField(blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='iractserver_model_set', db_comment='Model')
    crud_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='iractserver_crud_model_set', blank=True, null=True, db_comment='Record to Create')
    link_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True, db_comment='Link Field')
    update_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, related_name='iractserver_update_field_set', blank=True, null=True, db_comment='Field to Update')
    update_related_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='iractserver_update_related_model_set', blank=True, null=True, db_comment='Update Related Model')
    selection_value = models.ForeignKey('IrModelFieldsSelection', models.DO_NOTHING, db_column='selection_value', blank=True, null=True, db_comment='Custom Value')
    usage = models.CharField(db_comment='Usage')
    state = models.CharField(db_comment='Type')
    model_name = models.CharField(blank=True, null=True, db_comment='Model Name')
    update_path = models.CharField(blank=True, null=True, db_comment='Field to Update Path')
    update_m2m_operation = models.CharField(blank=True, null=True, db_comment='Many2many Operations')
    update_boolean_value = models.CharField(blank=True, null=True, db_comment='Boolean Value')
    evaluation_type = models.CharField(blank=True, null=True, db_comment='Value Type')
    resource_ref = models.CharField(blank=True, null=True, db_comment='Record')
    webhook_url = models.CharField(blank=True, null=True, db_comment='Webhook URL')
    code = models.TextField(blank=True, null=True, db_comment='Python Code')
    value = models.TextField(blank=True, null=True, db_comment='Value')
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='Email Template')
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True, db_comment='Activity Type')
    activity_date_deadline_range = models.IntegerField(blank=True, null=True, db_comment='Due Date In')
    activity_user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='iractserver_activity_user_set', blank=True, null=True, db_comment='Responsible')
    mail_post_method = models.CharField(blank=True, null=True, db_comment='Send Email As')
    activity_summary = models.CharField(blank=True, null=True, db_comment='Title')
    activity_date_deadline_range_type = models.CharField(blank=True, null=True, db_comment='Due type')
    activity_user_type = models.CharField(blank=True, null=True, db_comment='User Type')
    activity_user_field_name = models.CharField(blank=True, null=True, db_comment='User Field')
    activity_note = models.TextField(blank=True, null=True, db_comment='Note')
    mail_post_autofollow = models.BooleanField(blank=True, null=True, db_comment='Subscribe Recipients')
    sms_template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='SMS Template')
    sms_method = models.CharField(blank=True, null=True, db_comment='Send SMS As')
    website_path = models.CharField(blank=True, null=True, db_comment='Website Path')
    website_published = models.BooleanField(blank=True, null=True, db_comment='Available on the Website')

    class Meta:
        managed = False
        db_table = 'ir_act_server'


class IrActServerGroupRel(models.Model):
    pk = models.CompositePrimaryKey('act_id', 'gid')
    act = models.ForeignKey(IrActServer, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_server_group_rel'
        db_table_comment = 'RELATION BETWEEN ir_act_server AND res_groups'


class IrActServerResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('ir_act_server_id', 'res_partner_id')
    ir_act_server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_act_server_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN ir_act_server AND res_partner'


class IrActServerWebhookFieldRel(models.Model):
    pk = models.CompositePrimaryKey('server_id', 'field_id')
    server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_act_server_webhook_field_rel'
        db_table_comment = 'RELATION BETWEEN ir_act_server AND ir_model_fields'


class IrActUrl(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iracturl_write_uid_set', blank=True, null=True)
    type = models.CharField()
    path = models.CharField(unique=True, blank=True, null=True)
    binding_type = models.CharField()
    binding_view_types = models.CharField(blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    target = models.CharField(db_comment='Action Target')
    url = models.TextField(db_comment='Action URL')

    class Meta:
        managed = False
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iractwindow_write_uid_set', blank=True, null=True)
    type = models.CharField()
    path = models.CharField(unique=True, blank=True, null=True)
    binding_type = models.CharField()
    binding_view_types = models.CharField(blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True, db_comment='View Ref.')
    res_id = models.IntegerField(blank=True, null=True, db_comment='Record ID')
    limit = models.IntegerField(blank=True, null=True, db_comment='Limit')
    search_view = models.ForeignKey('IrUiView', models.DO_NOTHING, related_name='iractwindow_search_view_set', blank=True, null=True, db_comment='Search View Ref.')
    domain = models.CharField(blank=True, null=True, db_comment='Domain Value')
    context = models.CharField(db_comment='Context Value')
    res_model = models.CharField(db_comment='Destination Model')
    target = models.CharField(blank=True, null=True, db_comment='Target Window')
    view_mode = models.CharField(db_comment='View Mode')
    mobile_view_mode = models.CharField(blank=True, null=True, db_comment='Mobile View Mode')
    usage = models.CharField(blank=True, null=True, db_comment='Action Usage')
    filter = models.BooleanField(blank=True, null=True, db_comment='Filter')

    class Meta:
        managed = False
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    pk = models.CompositePrimaryKey('act_id', 'gid')
    act = models.ForeignKey(IrActWindow, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_window_group_rel'
        db_table_comment = 'RELATION BETWEEN ir_act_window AND res_groups'


class IrActWindowView(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True, db_comment='View')
    act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True, db_comment='Action')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iractwindowview_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    view_mode = models.CharField(db_comment='View Type')
    multi = models.BooleanField(blank=True, null=True, db_comment='On Multiple Doc.')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)
        db_table_comment = 'Action Window View'


class IrActions(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True, db_comment='Binding Model')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iractions_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    type = models.CharField(db_comment='Action Type')
    path = models.CharField(unique=True, blank=True, null=True, db_comment='Path to show in the URL')
    binding_type = models.CharField(db_comment='Binding Type')
    binding_view_types = models.CharField(blank=True, null=True, db_comment='Binding View Types')
    name = models.JSONField(db_comment='Action Name')
    help = models.JSONField(blank=True, null=True, db_comment='Action Description')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_actions'


class IrActionsTodo(models.Model):
    action_id = models.IntegerField(db_comment='Action')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iractionstodo_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    state = models.CharField(db_comment='Status')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_actions_todo'
        db_table_comment = 'Configuration Wizards'


class IrAsset(models.Model):
    sequence = models.IntegerField(db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irasset_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    bundle = models.CharField(db_comment='Bundle name')
    directive = models.CharField(blank=True, null=True, db_comment='Directive')
    path = models.CharField(db_comment='Path (or glob pattern)')
    target = models.CharField(blank=True, null=True, db_comment='Target')
    active = models.BooleanField(blank=True, null=True, db_comment='active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    theme_template = models.ForeignKey('ThemeIrAsset', models.DO_NOTHING, blank=True, null=True, db_comment='Theme Template')
    key = models.CharField(blank=True, null=True, db_comment='Key')

    class Meta:
        managed = False
        db_table = 'ir_asset'
        db_table_comment = 'Asset'


class IrAttachment(models.Model):
    res_id = models.IntegerField(blank=True, null=True, db_comment='Resource ID')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    file_size = models.IntegerField(blank=True, null=True, db_comment='File Size')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irattachment_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    res_model = models.CharField(blank=True, null=True, db_comment='Resource Model')
    res_field = models.CharField(blank=True, null=True, db_comment='Resource Field')
    type = models.CharField(db_comment='Type')
    url = models.CharField(max_length=1024, blank=True, null=True, db_comment='Url')
    access_token = models.CharField(blank=True, null=True, db_comment='Access Token')
    store_fname = models.CharField(blank=True, null=True, db_comment='Stored Filename')
    checksum = models.CharField(max_length=40, blank=True, null=True, db_comment='Checksum/SHA1')
    mimetype = models.CharField(blank=True, null=True, db_comment='Mime Type')
    description = models.TextField(blank=True, null=True, db_comment='Description')
    index_content = models.TextField(blank=True, null=True, db_comment='Indexed Content')
    public = models.BooleanField(blank=True, null=True, db_comment='Is public document')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    db_datas = models.BinaryField(blank=True, null=True, db_comment='Database Data')
    original = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Original (unoptimized, unresized) attachment')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    theme_template = models.ForeignKey('ThemeIrAttachment', models.DO_NOTHING, blank=True, null=True, db_comment='Theme Template')
    key = models.CharField(blank=True, null=True, db_comment='Key')

    class Meta:
        managed = False
        db_table = 'ir_attachment'
        db_table_comment = 'Attachment'


class IrConfigParameter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irconfigparameter_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    key = models.CharField(unique=True, db_comment='Key')
    value = models.TextField(db_comment='Value')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_config_parameter'
        db_table_comment = 'System Parameter'


class IrCron(models.Model):
    ir_actions_server = models.ForeignKey(IrActServer, models.DO_NOTHING, db_comment='Server action')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, db_comment='Scheduler User')
    interval_number = models.IntegerField(db_comment='Interval Number')
    priority = models.IntegerField(blank=True, null=True, db_comment='Priority')
    failure_count = models.IntegerField(blank=True, null=True, db_comment='Failure Count')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='ircron_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='ircron_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    cron_name = models.CharField(blank=True, null=True, db_comment='Name')
    interval_type = models.CharField(db_comment='Interval Unit')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    nextcall = models.DateTimeField(db_comment='Next Execution Date')
    lastcall = models.DateTimeField(blank=True, null=True, db_comment='Last Execution Date')
    first_failure_date = models.DateTimeField(blank=True, null=True, db_comment='First Failure Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_cron'
        db_table_comment = 'Scheduled Actions'


class IrCronProgress(models.Model):
    cron = models.ForeignKey(IrCron, models.DO_NOTHING, db_comment='Cron')
    remaining = models.IntegerField(blank=True, null=True, db_comment='Remaining')
    done = models.IntegerField(blank=True, null=True, db_comment='Done')
    timed_out_counter = models.IntegerField(blank=True, null=True, db_comment='Timed Out Counter')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='ircronprogress_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    deactivate = models.BooleanField(blank=True, null=True, db_comment='Deactivate')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_cron_progress'
        db_table_comment = 'Progress of Scheduled Actions'


class IrCronTrigger(models.Model):
    cron = models.ForeignKey(IrCron, models.DO_NOTHING, blank=True, null=True, db_comment='Cron')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='ircrontrigger_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    call_at = models.DateTimeField(blank=True, null=True, db_comment='Call At')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_cron_trigger'
        db_table_comment = 'Triggered actions'


class IrDefault(models.Model):
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_comment='Field')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='User')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='irdefault_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irdefault_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    condition = models.CharField(blank=True, null=True, db_comment='Condition')
    json_value = models.CharField(db_comment='Default Value (JSON format)')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_default'
        db_table_comment = 'Default Values'


class IrDemo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irdemo_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_demo'
        db_table_comment = 'Demo'


class IrDemoFailure(models.Model):
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_comment='Module')
    wizard = models.ForeignKey('IrDemoFailureWizard', models.DO_NOTHING, blank=True, null=True, db_comment='Wizard')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irdemofailure_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    error = models.CharField(blank=True, null=True, db_comment='Error')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_demo_failure'
        db_table_comment = 'Demo failure'


class IrDemoFailureWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irdemofailurewizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_demo_failure_wizard'
        db_table_comment = 'Demo Failure wizard'


class IrEmbeddedActions(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    parent_action = models.ForeignKey(IrActWindow, models.DO_NOTHING, db_comment='Parent Action')
    parent_res_id = models.IntegerField(blank=True, null=True, db_comment='Active Parent Id')
    action_id = models.IntegerField(blank=True, null=True, db_comment='Action')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='User')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='irembeddedactions_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irembeddedactions_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    parent_res_model = models.CharField(db_comment='Active Parent Model')
    python_method = models.CharField(blank=True, null=True, db_comment='Python Method')
    default_view_mode = models.CharField(blank=True, null=True, db_comment='Default View')
    domain = models.CharField(blank=True, null=True, db_comment='Domain')
    context = models.CharField(blank=True, null=True, db_comment='Context')
    name = models.JSONField(blank=True, null=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_embedded_actions'
        db_table_comment = 'Embedded Actions'


class IrEmbeddedActionsResGroupsRel(models.Model):
    pk = models.CompositePrimaryKey('ir_embedded_actions_id', 'res_groups_id')
    ir_embedded_actions = models.ForeignKey(IrEmbeddedActions, models.DO_NOTHING)
    res_groups = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_embedded_actions_res_groups_rel'
        db_table_comment = 'RELATION BETWEEN ir_embedded_actions AND res_groups'


class IrExports(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irexports_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Export Name')
    resource = models.CharField(blank=True, null=True, db_comment='Resource')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_exports'
        db_table_comment = 'Exports'


class IrExportsLine(models.Model):
    export = models.ForeignKey(IrExports, models.DO_NOTHING, blank=True, null=True, db_comment='Export')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irexportsline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Field Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_exports_line'
        db_table_comment = 'Exports Line'


class IrFilters(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='User')
    action_id = models.IntegerField(blank=True, null=True, db_comment='Action')
    embedded_action = models.ForeignKey(IrEmbeddedActions, models.DO_NOTHING, blank=True, null=True, db_comment='Embedded Action')
    embedded_parent_res_id = models.IntegerField(blank=True, null=True, db_comment='Embedded Parent Res')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='irfilters_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irfilters_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Filter Name')
    sort = models.CharField(db_comment='Sort')
    model_id = models.CharField(db_comment='Model')
    domain = models.TextField(db_comment='Domain')
    context = models.TextField(db_comment='Context')
    is_default = models.BooleanField(blank=True, null=True, db_comment='Default Filter')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_filters'
        unique_together = (('model_id', 'user', 'action_id', 'embedded_action', 'embedded_parent_res_id', 'name'), ('model_id', 'embedded_parent_res_id'),)
        db_table_comment = 'Filters'


class IrLogging(models.Model):
    create_uid = models.IntegerField(blank=True, null=True, db_comment='Created by')
    write_uid = models.IntegerField(blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    type = models.CharField(db_comment='Type')
    dbname = models.CharField(blank=True, null=True, db_comment='Database Name')
    level = models.CharField(blank=True, null=True, db_comment='Level')
    path = models.CharField(db_comment='Path')
    func = models.CharField(db_comment='Function')
    line = models.CharField(db_comment='Line')
    message = models.TextField(db_comment='Message')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_logging'
        db_table_comment = 'Logging'


class IrMailServer(models.Model):
    smtp_port = models.IntegerField(blank=True, null=True, db_comment='SMTP Port')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Priority')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmailserver_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    from_filter = models.CharField(blank=True, null=True, db_comment='FROM Filtering')
    smtp_host = models.CharField(blank=True, null=True, db_comment='SMTP Server')
    smtp_authentication = models.CharField(db_comment='Authenticate with')
    smtp_user = models.CharField(blank=True, null=True, db_comment='Username')
    smtp_pass = models.CharField(blank=True, null=True, db_comment='Password')
    smtp_encryption = models.CharField(db_comment='Connection Encryption')
    smtp_debug = models.BooleanField(blank=True, null=True, db_comment='Debugging')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    max_email_size = models.FloatField(blank=True, null=True, db_comment='Max Email Size')
    smtp_ssl_certificate = models.BinaryField(blank=True, null=True, db_comment='SSL Certificate')
    smtp_ssl_private_key = models.BinaryField(blank=True, null=True, db_comment='SSL Private Key')
    google_gmail_access_token_expiration = models.IntegerField(blank=True, null=True, db_comment='Access Token Expiration Timestamp')
    google_gmail_authorization_code = models.CharField(blank=True, null=True, db_comment='Authorization Code')
    google_gmail_refresh_token = models.CharField(blank=True, null=True, db_comment='Refresh Token')
    google_gmail_access_token = models.CharField(blank=True, null=True, db_comment='Access Token')

    class Meta:
        managed = False
        db_table = 'ir_mail_server'
        db_table_comment = 'Mail Server'


class IrModel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmodel_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    model = models.CharField(unique=True, db_comment='Model')
    order = models.CharField(db_comment='Order')
    state = models.CharField(blank=True, null=True, db_comment='Type')
    name = models.JSONField(db_comment='Model Description')
    info = models.TextField(blank=True, null=True, db_comment='Information')
    transient = models.BooleanField(blank=True, null=True, db_comment='Transient Model')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    is_mail_thread = models.BooleanField(blank=True, null=True, db_comment='Has Mail Thread')
    is_mail_activity = models.BooleanField(blank=True, null=True, db_comment='Has Mail Activity')
    is_mail_blacklist = models.BooleanField(blank=True, null=True, db_comment='Has Mail Blacklist')
    website_form_default_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True, db_comment='Field for custom form data')
    website_form_label = models.CharField(blank=True, null=True, db_comment='Label for form action')
    website_form_key = models.CharField(blank=True, null=True, db_comment='Website Form Key')
    website_form_access = models.BooleanField(blank=True, null=True, db_comment='Allowed to use in forms')

    class Meta:
        managed = False
        db_table = 'ir_model'
        db_table_comment = 'Models'


class IrModelAccess(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Model')
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True, db_comment='Group')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmodelaccess_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    perm_read = models.BooleanField(blank=True, null=True, db_comment='Read Access')
    perm_write = models.BooleanField(blank=True, null=True, db_comment='Write Access')
    perm_create = models.BooleanField(blank=True, null=True, db_comment='Create Access')
    perm_unlink = models.BooleanField(blank=True, null=True, db_comment='Delete Access')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_model_access'
        db_table_comment = 'Model Access'


class IrModelConstraint(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model', db_comment='Model')
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_column='module', db_comment='Module')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmodelconstraint_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Constraint')
    definition = models.CharField(blank=True, null=True, db_comment='Definition')
    type = models.CharField(max_length=1, db_comment='Constraint Type')
    message = models.JSONField(blank=True, null=True, db_comment='Message')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Write Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Create Date')

    class Meta:
        managed = False
        db_table = 'ir_model_constraint'
        unique_together = (('name', 'module'),)
        db_table_comment = 'Model Constraint'


class IrModelData(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmodeldata_write_uid_set', blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    noupdate = models.BooleanField(blank=True, null=True)
    name = models.CharField()
    module = models.CharField()
    model = models.CharField()

    class Meta:
        managed = False
        db_table = 'ir_model_data'
        unique_together = (('module', 'name'),)


class IrModelFields(models.Model):
    relation_field = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Relation field')
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Model')
    related_field = models.ForeignKey('self', models.DO_NOTHING, related_name='irmodelfields_related_field_set', blank=True, null=True, db_comment='Related Field')
    size = models.IntegerField(blank=True, null=True, db_comment='Size')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmodelfields_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Field Name')
    complete_name = models.CharField(blank=True, null=True, db_comment='Complete Name')
    model_0 = models.CharField(db_column='model', db_comment='Model Name')  # Field renamed because of name conflict.
    relation = models.CharField(blank=True, null=True, db_comment='Related Model')
    relation_field_0 = models.CharField(db_column='relation_field', blank=True, null=True, db_comment='Relation Field')  # Field renamed because of name conflict.
    ttype = models.CharField(db_comment='Field Type')
    related = models.CharField(blank=True, null=True, db_comment='Related Field Definition')
    state = models.CharField(db_comment='Type')
    on_delete = models.CharField(blank=True, null=True, db_comment='On Delete')
    domain = models.CharField(blank=True, null=True, db_comment='Domain')
    relation_table = models.CharField(blank=True, null=True, db_comment='Relation Table')
    column1 = models.CharField(blank=True, null=True, db_comment='Column 1')
    column2 = models.CharField(blank=True, null=True, db_comment='Column 2')
    depends = models.CharField(blank=True, null=True, db_comment='Dependencies')
    currency_field = models.CharField(blank=True, null=True, db_comment='Currency field')
    field_description = models.JSONField(db_comment='Field Label')
    help = models.JSONField(blank=True, null=True, db_comment='Field Help')
    compute = models.TextField(blank=True, null=True, db_comment='Compute')
    copied = models.BooleanField(blank=True, null=True, db_comment='Copied')
    required = models.BooleanField(blank=True, null=True, db_comment='Required')
    readonly = models.BooleanField(blank=True, null=True, db_comment='Readonly')
    index = models.BooleanField(blank=True, null=True, db_comment='Indexed')
    translate = models.BooleanField(blank=True, null=True, db_comment='Translatable')
    company_dependent = models.BooleanField(blank=True, null=True, db_comment='Company Dependent')
    group_expand = models.BooleanField(blank=True, null=True, db_comment='Expand Groups')
    selectable = models.BooleanField(blank=True, null=True, db_comment='Selectable')
    store = models.BooleanField(blank=True, null=True, db_comment='Stored')
    sanitize = models.BooleanField(blank=True, null=True, db_comment='Sanitize HTML')
    sanitize_overridable = models.BooleanField(blank=True, null=True, db_comment='Sanitize HTML overridable')
    sanitize_tags = models.BooleanField(blank=True, null=True, db_comment='Sanitize HTML Tags')
    sanitize_attributes = models.BooleanField(blank=True, null=True, db_comment='Sanitize HTML Attributes')
    sanitize_style = models.BooleanField(blank=True, null=True, db_comment='Sanitize HTML Style')
    sanitize_form = models.BooleanField(blank=True, null=True, db_comment='Sanitize HTML Form')
    strip_style = models.BooleanField(blank=True, null=True, db_comment='Strip Style Attribute')
    strip_classes = models.BooleanField(blank=True, null=True, db_comment='Strip Class Attribute')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    tracking = models.IntegerField(blank=True, null=True, db_comment='Enable Ordered Tracking')
    website_form_blacklisted = models.BooleanField(blank=True, null=True, db_comment='Blacklisted in web forms')

    class Meta:
        managed = False
        db_table = 'ir_model_fields'
        unique_together = (('model_0', 'name'),)
        db_table_comment = 'Fields'


class IrModelFieldsGroupRel(models.Model):
    pk = models.CompositePrimaryKey('field_id', 'group_id')
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_model_fields_group_rel'
        db_table_comment = 'RELATION BETWEEN ir_model_fields AND res_groups'


class IrModelFieldsSelection(models.Model):
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING, db_comment='Field')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmodelfieldsselection_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    value = models.CharField(db_comment='Value')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_model_fields_selection'
        unique_together = (('field', 'value'),)
        db_table_comment = 'Fields Selection'


class IrModelInherit(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Model')
    parent = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='irmodelinherit_parent_set', db_comment='Parent')
    parent_field = models.ForeignKey(IrModelFields, models.DO_NOTHING, blank=True, null=True, db_comment='Parent Field')

    class Meta:
        managed = False
        db_table = 'ir_model_inherit'
        unique_together = (('model', 'parent'),)
        db_table_comment = 'Model Inheritance Tree'


class IrModelRelation(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model', db_comment='Model')
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_column='module', db_comment='Module')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmodelrelation_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Relation Name')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Write Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Create Date')

    class Meta:
        managed = False
        db_table = 'ir_model_relation'
        db_table_comment = 'Relation Model'


class IrModelSpreadsheetDashboardRel(models.Model):
    pk = models.CompositePrimaryKey('spreadsheet_dashboard_id', 'ir_model_id')
    spreadsheet_dashboard = models.ForeignKey('SpreadsheetDashboard', models.DO_NOTHING)
    ir_model = models.ForeignKey(IrModel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_model_spreadsheet_dashboard_rel'
        db_table_comment = 'RELATION BETWEEN spreadsheet_dashboard AND ir_model'


class IrModuleCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmodulecategory_write_uid_set', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.JSONField()
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    description = models.JSONField(blank=True, null=True, db_comment='Description')
    visible = models.BooleanField(blank=True, null=True, db_comment='Visible')
    exclusive = models.BooleanField(blank=True, null=True, db_comment='Exclusive')

    class Meta:
        managed = False
        db_table = 'ir_module_category'


class IrModuleModule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmodulemodule_write_uid_set', blank=True, null=True)
    website = models.CharField(blank=True, null=True)
    summary = models.JSONField(blank=True, null=True)
    name = models.CharField(unique=True)
    author = models.CharField(blank=True, null=True)
    icon = models.CharField(blank=True, null=True)
    state = models.CharField(max_length=16, blank=True, null=True)
    latest_version = models.CharField(blank=True, null=True)
    shortdesc = models.JSONField(blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    application = models.BooleanField(blank=True, null=True)
    demo = models.BooleanField(blank=True, null=True)
    web = models.BooleanField(blank=True, null=True)
    license = models.CharField(max_length=32, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    auto_install = models.BooleanField(blank=True, null=True)
    to_buy = models.BooleanField(blank=True, null=True)
    maintainer = models.CharField(blank=True, null=True, db_comment='Maintainer')
    published_version = models.CharField(blank=True, null=True, db_comment='Published Version')
    url = models.CharField(blank=True, null=True, db_comment='URL')
    contributors = models.TextField(blank=True, null=True, db_comment='Contributors')
    menus_by_module = models.TextField(blank=True, null=True, db_comment='Menus')
    reports_by_module = models.TextField(blank=True, null=True, db_comment='Reports')
    views_by_module = models.TextField(blank=True, null=True, db_comment='Views')
    module_type = models.CharField(blank=True, null=True, db_comment='Module Type')
    imported = models.BooleanField(blank=True, null=True, db_comment='Imported Module')

    class Meta:
        managed = False
        db_table = 'ir_module_module'


class IrModuleModuleDependency(models.Model):
    name = models.CharField(blank=True, null=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True)
    auto_install_required = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_dependency'


class IrModuleModuleExclusion(models.Model):
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True, db_comment='Module')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irmodulemoduleexclusion_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_module_module_exclusion'
        db_table_comment = 'Module exclusion'


class IrProfile(models.Model):
    sql_count = models.IntegerField(blank=True, null=True, db_comment='Queries Count')
    entry_count = models.IntegerField(blank=True, null=True, db_comment='Entry count')
    session = models.CharField(blank=True, null=True, db_comment='Session')
    name = models.CharField(blank=True, null=True, db_comment='Description')
    init_stack_trace = models.TextField(blank=True, null=True, db_comment='Initial stack trace')
    sql = models.TextField(blank=True, null=True, db_comment='Sql')
    traces_async = models.TextField(blank=True, null=True, db_comment='Traces Async')
    traces_sync = models.TextField(blank=True, null=True, db_comment='Traces Sync')
    qweb = models.TextField(blank=True, null=True, db_comment='Qweb')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Creation Date')
    duration = models.FloatField(blank=True, null=True, db_comment='Duration')

    class Meta:
        managed = False
        db_table = 'ir_profile'
        db_table_comment = 'Profiling results'


class IrRule(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Model')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irrule_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    domain_force = models.TextField(blank=True, null=True, db_comment='Domain')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    perm_read = models.BooleanField(blank=True, null=True, db_comment='Read')
    perm_write = models.BooleanField(blank=True, null=True, db_comment='Write')
    perm_create = models.BooleanField(blank=True, null=True, db_comment='Create')
    perm_unlink = models.BooleanField(blank=True, null=True, db_comment='Delete')
    global_field = models.BooleanField(db_column='global', blank=True, null=True, db_comment='Global')  # Field renamed because it was a Python reserved word.
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_rule'
        db_table_comment = 'Record Rule'


class IrSequence(models.Model):
    number_next = models.IntegerField(db_comment='Next Number')
    number_increment = models.IntegerField(db_comment='Step')
    padding = models.IntegerField(db_comment='Sequence Size')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irsequence_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    code = models.CharField(blank=True, null=True, db_comment='Sequence Code')
    implementation = models.CharField(db_comment='Implementation')
    prefix = models.CharField(blank=True, null=True, db_comment='Prefix')
    suffix = models.CharField(blank=True, null=True, db_comment='Suffix')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_date_range = models.BooleanField(blank=True, null=True, db_comment='Use subsequences per date_range')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_sequence'
        db_table_comment = 'Sequence'


class IrSequenceDateRange(models.Model):
    sequence = models.ForeignKey(IrSequence, models.DO_NOTHING, db_comment='Main Sequence')
    number_next = models.IntegerField(db_comment='Next Number')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='irsequencedaterange_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    date_from = models.DateField(db_comment='From')
    date_to = models.DateField(db_comment='To')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_sequence_date_range'
        db_table_comment = 'Sequence Date Range'


class IrUiMenu(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Menu')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iruimenu_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    parent_path = models.CharField(blank=True, null=True, db_comment='Parent Path')
    web_icon = models.CharField(blank=True, null=True, db_comment='Web Icon File')
    action = models.CharField(blank=True, null=True, db_comment='Action')
    name = models.JSONField(db_comment='Menu')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_ui_menu'
        db_table_comment = 'Menu'


class IrUiMenuGroupRel(models.Model):
    pk = models.CompositePrimaryKey('menu_id', 'gid')
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_ui_menu_group_rel'
        db_table_comment = 'RELATION BETWEEN ir_ui_menu AND res_groups'


class IrUiView(models.Model):
    priority = models.IntegerField(db_comment='Sequence')
    inherit = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Inherited View')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iruiview_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='View Name')
    model = models.CharField(blank=True, null=True, db_comment='Model')
    key = models.CharField(blank=True, null=True, db_comment='Key')
    type = models.CharField(blank=True, null=True, db_comment='View Type')
    arch_fs = models.CharField(blank=True, null=True, db_comment='Arch Filename')
    mode = models.CharField(db_comment='View inheritance mode')
    arch_db = models.JSONField(blank=True, null=True, db_comment='Arch Blob')
    arch_prev = models.TextField(blank=True, null=True, db_comment='Previous View Architecture')
    arch_updated = models.BooleanField(blank=True, null=True, db_comment='Modified Architecture')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    customize_show = models.BooleanField(blank=True, null=True, db_comment='Show As Optional Inherit')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    theme_template = models.ForeignKey('ThemeIrUiView', models.DO_NOTHING, blank=True, null=True, db_comment='Theme Template')
    website_meta_og_img = models.CharField(blank=True, null=True, db_comment='Website opengraph image')
    visibility = models.CharField(blank=True, null=True, db_comment='Visibility')
    visibility_password = models.CharField(blank=True, null=True, db_comment='Visibility Password')
    website_meta_title = models.JSONField(blank=True, null=True, db_comment='Website meta title')
    website_meta_description = models.JSONField(blank=True, null=True, db_comment='Website meta description')
    website_meta_keywords = models.JSONField(blank=True, null=True, db_comment='Website meta keywords')
    seo_name = models.JSONField(blank=True, null=True, db_comment='Seo name')
    track = models.BooleanField(blank=True, null=True, db_comment='Track')

    class Meta:
        managed = False
        db_table = 'ir_ui_view'
        db_table_comment = 'View'


class IrUiViewCustom(models.Model):
    ref = models.ForeignKey(IrUiView, models.DO_NOTHING, db_comment='Original View')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, db_comment='User')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='iruiviewcustom_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='iruiviewcustom_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    arch = models.TextField(db_comment='View Architecture')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'ir_ui_view_custom'
        db_table_comment = 'Custom View'


class IrUiViewGroupRel(models.Model):
    pk = models.CompositePrimaryKey('view_id', 'group_id')
    view = models.ForeignKey(IrUiView, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_group_rel'
        db_table_comment = 'RELATION BETWEEN ir_ui_view AND res_groups'


class JournalAccountControlRel(models.Model):
    pk = models.CompositePrimaryKey('journal_id', 'account_id')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'journal_account_control_rel'
        db_table_comment = 'RELATION BETWEEN account_journal AND account_account'


class KitAccountTaxReport(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    root_report = models.ForeignKey(AccountReport, models.DO_NOTHING, blank=True, null=True, db_comment='Root Report')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    load_more_limit = models.IntegerField(blank=True, null=True, db_comment='Load More Limit')
    prefix_groups_threshold = models.IntegerField(blank=True, null=True, db_comment='Prefix Groups Threshold')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='kitaccounttaxreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart of Accounts')
    availability_condition = models.CharField(blank=True, null=True, db_comment='Availability')
    integer_rounding = models.CharField(blank=True, null=True, db_comment='Integer Rounding')
    default_opening_date_filter = models.CharField(blank=True, null=True, db_comment='Default Opening')
    currency_translation = models.CharField(blank=True, null=True, db_comment='Currency Translation')
    filter_multi_company = models.CharField(blank=True, null=True, db_comment='Multi-Company')
    filter_hide_0_lines = models.CharField(blank=True, null=True, db_comment='Hide lines at 0')
    filter_hierarchy = models.CharField(blank=True, null=True, db_comment='Account Groups')
    filter_account_type = models.CharField(blank=True, null=True, db_comment='Account Types')
    target_move = models.CharField(db_comment='Target Moves')
    date_from = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    name = models.JSONField(db_comment='Tax Report')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_sections = models.BooleanField(blank=True, null=True, db_comment='Composite Report')
    only_tax_exigible = models.BooleanField(blank=True, null=True, db_comment='Only Tax Exigible Lines')
    search_bar = models.BooleanField(blank=True, null=True, db_comment='Search Bar')
    filter_date_range = models.BooleanField(blank=True, null=True, db_comment='Date Range')
    filter_show_draft = models.BooleanField(blank=True, null=True, db_comment='Draft Entries')
    filter_unreconciled = models.BooleanField(blank=True, null=True, db_comment='Unreconciled Entries')
    filter_unfold_all = models.BooleanField(blank=True, null=True, db_comment='Unfold All')
    filter_period_comparison = models.BooleanField(blank=True, null=True, db_comment='Period Comparison')
    filter_growth_comparison = models.BooleanField(blank=True, null=True, db_comment='Growth Comparison')
    filter_journals = models.BooleanField(blank=True, null=True, db_comment='Journals')
    filter_analytic = models.BooleanField(blank=True, null=True, db_comment='Analytic Filter')
    filter_partner = models.BooleanField(blank=True, null=True, db_comment='Partners')
    filter_fiscal_position = models.BooleanField(blank=True, null=True, db_comment='Filter Multivat')
    filter_aml_ir_filters = models.BooleanField(blank=True, null=True, db_comment='Favorite Filters')
    filter_budgets = models.BooleanField(blank=True, null=True, db_comment='Budgets')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'kit_account_tax_report'
        db_table_comment = 'Tax Report'


class L10NInPortCode(models.Model):
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, blank=True, null=True, db_comment='State')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='l10ninportcode_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code = models.CharField(unique=True, db_comment='Port Code')
    name = models.CharField(db_comment='Port')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'l10n_in_port_code'
        db_table_comment = 'Indian port code'


class LinkTracker(models.Model):
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True, db_comment='Campaign')
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True, db_comment='Source')
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True, db_comment='Medium')
    count = models.IntegerField(blank=True, null=True, db_comment='Number of Clicks')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='linktracker_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    url = models.CharField(db_comment='Target URL')
    title = models.CharField(blank=True, null=True, db_comment='Page Title')
    label = models.CharField(blank=True, null=True, db_comment='Button label')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    mass_mailing = models.ForeignKey('MailingMailing', models.DO_NOTHING, blank=True, null=True, db_comment='Mass Mailing')

    class Meta:
        managed = False
        db_table = 'link_tracker'
        db_table_comment = 'Link Tracker'


class LinkTrackerClick(models.Model):
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True, db_comment='UTM Campaign')
    link = models.ForeignKey(LinkTracker, models.DO_NOTHING, db_comment='Link')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='linktrackerclick_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    ip = models.CharField(blank=True, null=True, db_comment='Internet Protocol')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    mailing_trace = models.ForeignKey('MailingTrace', models.DO_NOTHING, blank=True, null=True, db_comment='Mail Statistics')
    mass_mailing = models.ForeignKey('MailingMailing', models.DO_NOTHING, blank=True, null=True, db_comment='Mass Mailing')

    class Meta:
        managed = False
        db_table = 'link_tracker_click'
        db_table_comment = 'Link Tracker Click'


class LinkTrackerCode(models.Model):
    link = models.ForeignKey(LinkTracker, models.DO_NOTHING, db_comment='Link')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='linktrackercode_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code = models.CharField(unique=True, db_comment='Short URL Code')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'link_tracker_code'
        db_table_comment = 'Link Tracker Code'


class LotLabelLayout(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='lotlabellayout_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    label_quantity = models.CharField(db_comment='Quantity to print')
    print_format = models.CharField(db_comment='Format')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'lot_label_layout'
        db_table_comment = 'Choose the sheet layout to print lot labels'


class LotLabelLayoutStockMoveLineRel(models.Model):
    pk = models.CompositePrimaryKey('lot_label_layout_id', 'stock_move_line_id')
    lot_label_layout = models.ForeignKey(LotLabelLayout, models.DO_NOTHING)
    stock_move_line = models.ForeignKey('StockMoveLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lot_label_layout_stock_move_line_rel'
        db_table_comment = 'RELATION BETWEEN lot_label_layout AND stock_move_line'


class MailActivity(models.Model):
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Document Model')
    res_id = models.IntegerField(blank=True, null=True, db_comment='Related Document ID')
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True, db_comment='Activity Type')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, db_comment='Assigned to')
    request_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Requesting Partner')
    recommended_activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, related_name='mailactivity_recommended_activity_type_set', blank=True, null=True, db_comment='Recommended Activity Type')
    previous_activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, related_name='mailactivity_previous_activity_type_set', blank=True, null=True, db_comment='Previous Activity Type')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='mailactivity_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailactivity_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    res_model_0 = models.CharField(db_column='res_model', blank=True, null=True, db_comment='Related Document Model')  # Field renamed because of name conflict.
    res_name = models.CharField(blank=True, null=True, db_comment='Document Name')
    summary = models.CharField(blank=True, null=True, db_comment='Summary')
    user_tz = models.CharField(blank=True, null=True, db_comment='Timezone')
    date_deadline = models.DateField(db_comment='Due Date')
    date_done = models.DateField(blank=True, null=True, db_comment='Done Date')
    note = models.TextField(blank=True, null=True, db_comment='Note')
    automated = models.BooleanField(blank=True, null=True, db_comment='Automated activity')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_activity'
        db_table_comment = 'Activity'


class MailActivityPlan(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Applies to')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailactivityplan_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    res_model_0 = models.CharField(db_column='res_model', db_comment='Model')  # Field renamed because of name conflict.
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True, db_comment='Department')

    class Meta:
        managed = False
        db_table = 'mail_activity_plan'
        db_table_comment = 'Activity Plan'


class MailActivityPlanMailActivityScheduleRel(models.Model):
    pk = models.CompositePrimaryKey('mail_activity_schedule_id', 'mail_activity_plan_id')
    mail_activity_schedule = models.ForeignKey('MailActivitySchedule', models.DO_NOTHING)
    mail_activity_plan = models.ForeignKey(MailActivityPlan, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_activity_plan_mail_activity_schedule_rel'
        db_table_comment = 'RELATION BETWEEN mail_activity_schedule AND mail_activity_plan'


class MailActivityPlanTemplate(models.Model):
    plan = models.ForeignKey(MailActivityPlan, models.DO_NOTHING, db_comment='Plan')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, db_comment='Activity Type')
    delay_count = models.IntegerField(blank=True, null=True, db_comment='Interval')
    responsible = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Assigned to')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='mailactivityplantemplate_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailactivityplantemplate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    delay_unit = models.CharField(db_comment='Delay units')
    delay_from = models.CharField(db_comment='Trigger')
    summary = models.CharField(blank=True, null=True, db_comment='Summary')
    responsible_type = models.CharField(db_comment='Assignment')
    note = models.TextField(blank=True, null=True, db_comment='Note')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_activity_plan_template'
        db_table_comment = 'Activity plan template'


class MailActivityRel(models.Model):
    pk = models.CompositePrimaryKey('activity_id', 'recommended_id')
    activity = models.ForeignKey('MailActivityType', models.DO_NOTHING)
    recommended = models.ForeignKey('MailActivityType', models.DO_NOTHING, related_name='mailactivityrel_recommended_set')

    class Meta:
        managed = False
        db_table = 'mail_activity_rel'
        db_table_comment = 'RELATION BETWEEN mail_activity_type AND mail_activity_type'


class MailActivitySchedule(models.Model):
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Applies to')
    plan = models.ForeignKey(MailActivityPlan, models.DO_NOTHING, blank=True, null=True, db_comment='Plan')
    plan_on_demand_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Assigned To')
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True, db_comment='Activity Type')
    activity_user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='mailactivityschedule_activity_user_set', blank=True, null=True, db_comment='Assigned to')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='mailactivityschedule_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailactivityschedule_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    res_model_0 = models.CharField(db_column='res_model', db_comment='Model')  # Field renamed because of name conflict.
    summary = models.CharField(blank=True, null=True, db_comment='Summary')
    plan_date = models.DateField(blank=True, null=True, db_comment='Plan Date')
    date_deadline = models.DateField(blank=True, null=True, db_comment='Due Date')
    res_ids = models.TextField(blank=True, null=True, db_comment='Document IDs')
    note = models.TextField(blank=True, null=True, db_comment='Note')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_activity_schedule'
        db_table_comment = 'Activity schedule plan Wizard'


class MailActivityType(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Create Uid')
    delay_count = models.IntegerField(blank=True, null=True, db_comment='Schedule')
    triggered_next_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Trigger')
    default_user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='mailactivitytype_default_user_set', blank=True, null=True, db_comment='Default User')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailactivitytype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    delay_unit = models.CharField(db_comment='Delay units')
    delay_from = models.CharField(db_comment='Delay Type')
    icon = models.CharField(blank=True, null=True, db_comment='Icon')
    decoration_type = models.CharField(blank=True, null=True, db_comment='Decoration Type')
    res_model = models.CharField(blank=True, null=True, db_comment='Model')
    chaining_type = models.CharField(db_comment='Chaining Type')
    category = models.CharField(blank=True, null=True, db_comment='Action')
    name = models.JSONField(db_comment='Name')
    summary = models.JSONField(blank=True, null=True, db_comment='Default Summary')
    default_note = models.JSONField(blank=True, null=True, db_comment='Default Note')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    keep_done = models.BooleanField(blank=True, null=True, db_comment='Keep Done')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_activity_type'
        db_table_comment = 'Activity Type'


class MailActivityTypeMailTemplateRel(models.Model):
    pk = models.CompositePrimaryKey('mail_activity_type_id', 'mail_template_id')
    mail_activity_type = models.ForeignKey(MailActivityType, models.DO_NOTHING)
    mail_template = models.ForeignKey('MailTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_activity_type_mail_template_rel'
        db_table_comment = 'RELATION BETWEEN mail_activity_type AND mail_template'


class MailAlias(models.Model):
    alias_domain = models.ForeignKey('MailAliasDomain', models.DO_NOTHING, blank=True, null=True, db_comment='Alias Domain')
    alias_model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Aliased Model')
    alias_force_thread_id = models.IntegerField(blank=True, null=True, db_comment='Record Thread ID')
    alias_parent_model = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='mailalias_alias_parent_model_set', blank=True, null=True, db_comment='Parent Model')
    alias_parent_thread_id = models.IntegerField(blank=True, null=True, db_comment='Parent Record Thread ID')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailalias_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    alias_name = models.CharField(blank=True, null=True, db_comment='Alias Name')
    alias_full_name = models.CharField(blank=True, null=True, db_comment='Alias Email')
    alias_contact = models.CharField(db_comment='Alias Contact Security')
    alias_status = models.CharField(blank=True, null=True, db_comment='Alias Status')
    alias_bounced_content = models.JSONField(blank=True, null=True, db_comment='Custom Bounced Message')
    alias_defaults = models.TextField(db_comment='Default Values')
    alias_incoming_local = models.BooleanField(blank=True, null=True, db_comment='Local-part based incoming detection')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'mail_alias'
        db_table_comment = 'Email Aliases'


class MailAliasDomain(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailaliasdomain_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    bounce_alias = models.CharField(db_comment='Bounce Alias')
    catchall_alias = models.CharField(db_comment='Catchall Alias')
    default_from = models.CharField(blank=True, null=True, db_comment='Default From Alias')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_alias_domain'
        unique_together = (('bounce_alias', 'name'), ('catchall_alias', 'name'),)
        db_table_comment = 'Email Domain'


class MailBlacklist(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailblacklist_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    email = models.CharField(unique=True, db_comment='Email Address')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    opt_out_reason = models.ForeignKey('MailingSubscriptionOptout', models.DO_NOTHING, blank=True, null=True, db_comment='Opt-out Reason')

    class Meta:
        managed = False
        db_table = 'mail_blacklist'
        db_table_comment = 'Mail Blacklist'


class MailBlacklistRemove(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailblacklistremove_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    email = models.CharField(db_comment='Email')
    reason = models.CharField(blank=True, null=True, db_comment='Reason')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_blacklist_remove'
        db_table_comment = 'Remove email from blacklist wizard'


class MailCannedResponse(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailcannedresponse_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    source = models.CharField(db_comment='Shortcut')
    description = models.CharField(blank=True, null=True, db_comment='Description')
    substitution = models.TextField(db_comment='Substitution')
    is_shared = models.BooleanField(blank=True, null=True, db_comment='Determines if the canned_response is currently shared with other users')
    last_used = models.DateTimeField(blank=True, null=True, db_comment='Last Used')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_canned_response'
        db_table_comment = 'Canned Response'


class MailCannedResponseResGroupsRel(models.Model):
    pk = models.CompositePrimaryKey('mail_canned_response_id', 'res_groups_id')
    mail_canned_response = models.ForeignKey(MailCannedResponse, models.DO_NOTHING)
    res_groups = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_canned_response_res_groups_rel'
        db_table_comment = 'RELATION BETWEEN mail_canned_response AND res_groups'


class MailComposeMessage(models.Model):
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='Use template')
    parent = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Message')
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Author')
    res_domain_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Responsible')
    record_alias_domain = models.ForeignKey(MailAliasDomain, models.DO_NOTHING, blank=True, null=True, db_comment='Alias Domain')
    record_company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True, db_comment='Subtype')
    mail_activity_type = models.ForeignKey(MailActivityType, models.DO_NOTHING, blank=True, null=True, db_comment='Mail Activity Type')
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True, db_comment='Outgoing mail server')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='mailcomposemessage_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailcomposemessage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    lang = models.CharField(blank=True, null=True, db_comment='Language')
    subject = models.CharField(blank=True, null=True, db_comment='Subject')
    email_layout_xmlid = models.CharField(blank=True, null=True, db_comment='Email Notification Layout')
    email_from = models.CharField(blank=True, null=True, db_comment='From')
    composition_mode = models.CharField(blank=True, null=True, db_comment='Composition mode')
    model = models.CharField(blank=True, null=True, db_comment='Related Document Model')
    record_name = models.CharField(blank=True, null=True, db_comment='Record Name')
    message_type = models.CharField(db_comment='Type')
    reply_to = models.CharField(blank=True, null=True, db_comment='Reply To')
    scheduled_date = models.CharField(blank=True, null=True, db_comment='Scheduled Date')
    template_name = models.CharField(blank=True, null=True, db_comment='Template Name')
    body = models.TextField(blank=True, null=True, db_comment='Contents')
    res_ids = models.TextField(blank=True, null=True, db_comment='Related Document IDs')
    res_domain = models.TextField(blank=True, null=True, db_comment='Active domain')
    email_add_signature = models.BooleanField(blank=True, null=True, db_comment='Add signature')
    reply_to_force_new = models.BooleanField(blank=True, null=True, db_comment='Considers answers as new thread')
    auto_delete = models.BooleanField(blank=True, null=True, db_comment='Delete Emails')
    auto_delete_keep_log = models.BooleanField(blank=True, null=True, db_comment='Keep Message Copy')
    force_send = models.BooleanField(blank=True, null=True, db_comment='Send mailing or notifications directly')
    use_exclusion_list = models.BooleanField(blank=True, null=True, db_comment='Check Exclusion List')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    mass_mailing = models.ForeignKey('MailingMailing', models.DO_NOTHING, blank=True, null=True, db_comment='Mass Mailing')
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True, db_comment='Mass Mailing Campaign')
    mass_mailing_name = models.CharField(blank=True, null=True, db_comment='Mass Mailing Name')

    class Meta:
        managed = False
        db_table = 'mail_compose_message'
        db_table_comment = 'Email composition wizard'


class MailComposeMessageIrAttachmentsRel(models.Model):
    pk = models.CompositePrimaryKey('wizard_id', 'attachment_id')
    wizard = models.ForeignKey(MailComposeMessage, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_ir_attachments_rel'
        db_table_comment = 'RELATION BETWEEN mail_compose_message AND ir_attachment'


class MailComposeMessageMailingListRel(models.Model):
    pk = models.CompositePrimaryKey('mail_compose_message_id', 'mailing_list_id')
    mail_compose_message = models.ForeignKey(MailComposeMessage, models.DO_NOTHING)
    mailing_list = models.ForeignKey('MailingList', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_mailing_list_rel'
        db_table_comment = 'RELATION BETWEEN mail_compose_message AND mailing_list'


class MailComposeMessageResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('wizard_id', 'partner_id')
    wizard = models.ForeignKey(MailComposeMessage, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN mail_compose_message AND res_partner'


class MailFollowers(models.Model):
    res_id = models.IntegerField(blank=True, null=True, db_comment='Related Document ID')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Related Partner')
    res_model = models.CharField(db_comment='Related Document Model Name')

    class Meta:
        managed = False
        db_table = 'mail_followers'
        unique_together = (('res_model', 'res_id', 'partner'),)
        db_table_comment = 'Document Followers'


class MailFollowersMailMessageSubtypeRel(models.Model):
    pk = models.CompositePrimaryKey('mail_followers_id', 'mail_message_subtype_id')
    mail_followers = models.ForeignKey(MailFollowers, models.DO_NOTHING)
    mail_message_subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_followers_mail_message_subtype_rel'
        db_table_comment = 'RELATION BETWEEN mail_followers AND mail_message_subtype'


class MailGatewayAllowed(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailgatewayallowed_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    email = models.CharField(db_comment='Email Address')
    email_normalized = models.CharField(blank=True, null=True, db_comment='Normalized Email')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_gateway_allowed'
        db_table_comment = 'Mail Gateway Allowed'


class MailGuest(models.Model):
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailguest_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    access_token = models.CharField(db_comment='Access Token')
    lang = models.CharField(blank=True, null=True, db_comment='Language')
    timezone = models.CharField(blank=True, null=True, db_comment='Timezone')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_guest'
        db_table_comment = 'Guest'


class MailIceServer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailiceserver_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    server_type = models.CharField(db_comment='Type')
    uri = models.CharField(db_comment='URI')
    username = models.CharField(blank=True, null=True, db_comment='Username')
    credential = models.CharField(blank=True, null=True, db_comment='Credential')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_ice_server'
        db_table_comment = 'ICE server'


class MailLinkPreview(models.Model):
    message = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True, db_comment='Message')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='maillinkpreview_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    source_url = models.CharField(db_comment='URL')
    og_type = models.CharField(blank=True, null=True, db_comment='Type')
    og_title = models.CharField(blank=True, null=True, db_comment='Title')
    og_site_name = models.CharField(blank=True, null=True, db_comment='Site name')
    og_image = models.CharField(blank=True, null=True, db_comment='Image')
    og_mimetype = models.CharField(blank=True, null=True, db_comment='MIME type')
    image_mimetype = models.CharField(blank=True, null=True, db_comment='Image MIME type')
    og_description = models.TextField(blank=True, null=True, db_comment='Description')
    is_hidden = models.BooleanField(blank=True, null=True, db_comment='Is Hidden')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Create Date')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_link_preview'
        db_table_comment = 'Store link preview data'


class MailMail(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING, db_comment='Message')
    fetchmail_server = models.ForeignKey(FetchmailServer, models.DO_NOTHING, blank=True, null=True, db_comment='Inbound Mail Server')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailmail_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    email_cc = models.CharField(blank=True, null=True, db_comment='Cc')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    failure_type = models.CharField(blank=True, null=True, db_comment='Failure type')
    body_html = models.TextField(blank=True, null=True, db_comment='Text Contents')
    references = models.TextField(blank=True, null=True, db_comment='References')
    headers = models.TextField(blank=True, null=True, db_comment='Headers')
    email_to = models.TextField(blank=True, null=True, db_comment='To')
    failure_reason = models.TextField(blank=True, null=True, db_comment='Failure Reason')
    is_notification = models.BooleanField(blank=True, null=True, db_comment='Notification Email')
    auto_delete = models.BooleanField(blank=True, null=True, db_comment='Auto Delete')
    scheduled_date = models.DateTimeField(blank=True, null=True, db_comment='Scheduled Send Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    mailing = models.ForeignKey('MailingMailing', models.DO_NOTHING, blank=True, null=True, db_comment='Mass Mailing')

    class Meta:
        managed = False
        db_table = 'mail_mail'
        db_table_comment = 'Outgoing Mails'


class MailMailResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('mail_mail_id', 'res_partner_id')
    mail_mail = models.ForeignKey(MailMail, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mail_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN mail_mail AND res_partner'


class MailMassMailingListRel(models.Model):
    pk = models.CompositePrimaryKey('mailing_list_id', 'mailing_mailing_id')
    mailing_list = models.ForeignKey('MailingList', models.DO_NOTHING)
    mailing_mailing = models.ForeignKey('MailingMailing', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_list_rel'
        db_table_comment = 'RELATION BETWEEN mailing_list AND mailing_mailing'


class MailMessage(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Message')
    res_id = models.IntegerField(blank=True, null=True, db_comment='Related Document ID')
    record_alias_domain = models.ForeignKey(MailAliasDomain, models.DO_NOTHING, blank=True, null=True, db_comment='Alias Domain')
    record_company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True, db_comment='Subtype')
    mail_activity_type = models.ForeignKey(MailActivityType, models.DO_NOTHING, blank=True, null=True, db_comment='Mail Activity Type')
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Author')
    author_guest = models.ForeignKey(MailGuest, models.DO_NOTHING, blank=True, null=True, db_comment='Guest')
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True, db_comment='Outgoing mail server')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailmessage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    subject = models.CharField(blank=True, null=True, db_comment='Subject')
    model = models.CharField(blank=True, null=True, db_comment='Related Document Model')
    record_name = models.CharField(blank=True, null=True, db_comment='Message Record Name')
    message_type = models.CharField(db_comment='Type')
    email_from = models.CharField(blank=True, null=True, db_comment='From')
    message_id = models.CharField(blank=True, null=True, db_comment='Message-Id')
    reply_to = models.CharField(blank=True, null=True, db_comment='Reply-To')
    email_layout_xmlid = models.CharField(blank=True, null=True, db_comment='Layout')
    body = models.TextField(blank=True, null=True, db_comment='Contents')
    is_internal = models.BooleanField(blank=True, null=True, db_comment='Employee Only')
    reply_to_force_new = models.BooleanField(blank=True, null=True, db_comment='No threading for answers')
    email_add_signature = models.BooleanField(blank=True, null=True, db_comment='Email Add Signature')
    date = models.DateTimeField(blank=True, null=True, db_comment='Date')
    pinned_at = models.DateTimeField(blank=True, null=True, db_comment='Pinned')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_message'
        db_table_comment = 'Message'


class MailMessageReaction(models.Model):
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, db_comment='Message')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Reacting Partner')
    guest = models.ForeignKey(MailGuest, models.DO_NOTHING, blank=True, null=True, db_comment='Reacting Guest')
    content = models.CharField(db_comment='Content')

    class Meta:
        managed = False
        db_table = 'mail_message_reaction'
        unique_together = (('message', 'content', 'guest'), ('message', 'content', 'partner'),)
        db_table_comment = 'Message Reaction'


class MailMessageResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('mail_message_id', 'res_partner_id')
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN mail_message AND res_partner'


class MailMessageResPartnerStarredRel(models.Model):
    pk = models.CompositePrimaryKey('mail_message_id', 'res_partner_id')
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_starred_rel'
        db_table_comment = 'RELATION BETWEEN mail_message AND res_partner'


class MailMessageSchedule(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, db_comment='Message')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailmessageschedule_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    notification_parameters = models.TextField(blank=True, null=True, db_comment='Notification Parameter')
    scheduled_datetime = models.DateTimeField(db_comment='Scheduled Send Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_message_schedule'
        db_table_comment = 'Scheduled Messages'


class MailMessageSubtype(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailmessagesubtype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    relation_field = models.CharField(blank=True, null=True, db_comment='Relation field')
    res_model = models.CharField(blank=True, null=True, db_comment='Model')
    name = models.JSONField(db_comment='Message Type')
    description = models.JSONField(blank=True, null=True, db_comment='Description')
    internal = models.BooleanField(blank=True, null=True, db_comment='Internal Only')
    default = models.BooleanField(blank=True, null=True, db_comment='Default')
    hidden = models.BooleanField(blank=True, null=True, db_comment='Hidden')
    track_recipients = models.BooleanField(blank=True, null=True, db_comment='Track Recipients')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_message_subtype'
        db_table_comment = 'Message subtypes'


class MailMessageTranslation(models.Model):
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, db_comment='Message')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailmessagetranslation_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    source_lang = models.CharField(db_comment='Source Language')
    target_lang = models.CharField(db_comment='Target Language')
    body = models.TextField(db_comment='Translation Body')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Create Date')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_message_translation'
        unique_together = (('message', 'target_lang'),)
        db_table_comment = 'Message Translation'


class MailNotification(models.Model):
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Author')
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, db_comment='Message')
    mail_mail = models.ForeignKey(MailMail, models.DO_NOTHING, blank=True, null=True, db_comment='Mail')
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='mailnotification_res_partner_set', blank=True, null=True, db_comment='Recipient')
    notification_type = models.CharField(db_comment='Notification Type')
    notification_status = models.CharField(blank=True, null=True, db_comment='Status')
    failure_type = models.CharField(blank=True, null=True, db_comment='Failure type')
    failure_reason = models.TextField(blank=True, null=True, db_comment='Failure reason')
    is_read = models.BooleanField(blank=True, null=True, db_comment='Is Read')
    read_date = models.DateTimeField(blank=True, null=True, db_comment='Read Date')
    sms_id_int = models.IntegerField(blank=True, null=True, db_comment='SMS ID')
    sms_number = models.CharField(blank=True, null=True, db_comment='SMS Number')
    letter = models.ForeignKey('SnailmailLetter', models.DO_NOTHING, blank=True, null=True, db_comment='Snailmail Letter')

    class Meta:
        managed = False
        db_table = 'mail_notification'
        unique_together = (('mail_message', 'res_partner'),)
        db_table_comment = 'Message Notifications'


class MailNotificationMailResendMessageRel(models.Model):
    pk = models.CompositePrimaryKey('mail_resend_message_id', 'mail_notification_id')
    mail_resend_message = models.ForeignKey('MailResendMessage', models.DO_NOTHING)
    mail_notification = models.ForeignKey(MailNotification, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_notification_mail_resend_message_rel'
        db_table_comment = 'RELATION BETWEEN mail_resend_message AND mail_notification'


class MailPush(models.Model):
    mail_push_device = models.ForeignKey('MailPushDevice', models.DO_NOTHING, db_comment='devices')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailpush_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    payload = models.TextField(blank=True, null=True, db_comment='Payload')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_push'
        db_table_comment = 'Push Notifications'


class MailPushDevice(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Partner')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailpushdevice_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    endpoint = models.CharField(unique=True, db_comment='Browser endpoint')
    keys = models.CharField(db_comment='Browser keys')
    expiration_time = models.DateTimeField(blank=True, null=True, db_comment='Expiration Token Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_push_device'
        db_table_comment = 'Push Notification Device'


class MailResendMessage(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True, db_comment='Message')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailresendmessage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_resend_message'
        db_table_comment = 'Email resend wizard'


class MailResendPartner(models.Model):
    notification = models.ForeignKey(MailNotification, models.DO_NOTHING, db_comment='Notification')
    resend_wizard = models.ForeignKey(MailResendMessage, models.DO_NOTHING, blank=True, null=True, db_comment='Resend wizard')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailresendpartner_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    message = models.CharField(blank=True, null=True, db_comment='Error message')
    resend = models.BooleanField(blank=True, null=True, db_comment='Try Again')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_resend_partner'
        db_table_comment = 'Partner with additional information for mail resend'


class MailScheduledMessage(models.Model):
    res_id = models.IntegerField(db_comment='Related Document Id')
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Author')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailscheduledmessage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    subject = models.CharField(blank=True, null=True, db_comment='Subject')
    model = models.CharField(db_comment='Related Document Model')
    body = models.TextField(blank=True, null=True, db_comment='Contents')
    notification_parameters = models.TextField(blank=True, null=True, db_comment='Notification parameters')
    is_note = models.BooleanField(blank=True, null=True, db_comment='Is a note')
    scheduled_date = models.DateTimeField(db_comment='Scheduled Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_scheduled_message'
        db_table_comment = 'Scheduled Message'


class MailScheduledMessageResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('mail_scheduled_message_id', 'res_partner_id')
    mail_scheduled_message = models.ForeignKey(MailScheduledMessage, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_scheduled_message_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN mail_scheduled_message AND res_partner'


class MailTemplate(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True, db_comment='Applies to')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='User')
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True, db_comment='Outgoing Mail Server')
    ref_ir_act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True, db_comment='Sidebar action')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='mailtemplate_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailtemplate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    template_fs = models.CharField(blank=True, null=True, db_comment='Template Filename')
    lang = models.CharField(blank=True, null=True, db_comment='Language')
    model_0 = models.CharField(db_column='model', blank=True, null=True, db_comment='Related Document Model')  # Field renamed because of name conflict.
    email_from = models.CharField(blank=True, null=True, db_comment='From')
    email_to = models.CharField(blank=True, null=True, db_comment='To (Emails)')
    partner_to = models.CharField(blank=True, null=True, db_comment='To (Partners)')
    email_cc = models.CharField(blank=True, null=True, db_comment='Cc')
    reply_to = models.CharField(blank=True, null=True, db_comment='Reply To')
    email_layout_xmlid = models.CharField(blank=True, null=True, db_comment='Email Notification Layout')
    scheduled_date = models.CharField(blank=True, null=True, db_comment='Scheduled Date')
    name = models.JSONField(blank=True, null=True, db_comment='Name')
    description = models.JSONField(blank=True, null=True, db_comment='Template Description')
    subject = models.JSONField(blank=True, null=True, db_comment='Subject')
    body_html = models.JSONField(blank=True, null=True, db_comment='Body')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_default_to = models.BooleanField(blank=True, null=True, db_comment='Default recipients')
    auto_delete = models.BooleanField(blank=True, null=True, db_comment='Auto Delete')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_template'
        db_table_comment = 'Email Templates'


class MailTemplateIrActionsReportRel(models.Model):
    pk = models.CompositePrimaryKey('mail_template_id', 'ir_actions_report_id')
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING)
    ir_actions_report = models.ForeignKey(IrActReportXml, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_template_ir_actions_report_rel'
        db_table_comment = 'RELATION BETWEEN mail_template AND ir_act_report_xml'


class MailTemplateMailTemplateResetRel(models.Model):
    pk = models.CompositePrimaryKey('mail_template_reset_id', 'mail_template_id')
    mail_template_reset = models.ForeignKey('MailTemplateReset', models.DO_NOTHING)
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_template_mail_template_reset_rel'
        db_table_comment = 'RELATION BETWEEN mail_template_reset AND mail_template'


class MailTemplatePreview(models.Model):
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, db_comment='Related Mail Template')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailtemplatepreview_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    resource_ref = models.CharField(blank=True, null=True, db_comment='Record')
    lang = models.CharField(blank=True, null=True, db_comment='Template Preview Language')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_template_preview'
        db_table_comment = 'Email Template Preview'


class MailTemplateReset(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailtemplatereset_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_template_reset'
        db_table_comment = 'Mail Template Reset'


class MailTrackingValue(models.Model):
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING, blank=True, null=True, db_comment='Field')
    old_value_integer = models.IntegerField(blank=True, null=True, db_comment='Old Value Integer')
    new_value_integer = models.IntegerField(blank=True, null=True, db_comment='New Value Integer')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, db_comment='Message ID')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailtrackingvalue_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    old_value_char = models.CharField(blank=True, null=True, db_comment='Old Value Char')
    new_value_char = models.CharField(blank=True, null=True, db_comment='New Value Char')
    field_info = models.JSONField(blank=True, null=True, db_comment='Removed field information')
    old_value_text = models.TextField(blank=True, null=True, db_comment='Old Value Text')
    new_value_text = models.TextField(blank=True, null=True, db_comment='New Value Text')
    old_value_datetime = models.DateTimeField(blank=True, null=True, db_comment='Old Value DateTime')
    new_value_datetime = models.DateTimeField(blank=True, null=True, db_comment='New Value Datetime')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    old_value_float = models.FloatField(blank=True, null=True, db_comment='Old Value Float')
    new_value_float = models.FloatField(blank=True, null=True, db_comment='New Value Float')

    class Meta:
        managed = False
        db_table = 'mail_tracking_value'
        db_table_comment = 'Mail Tracking Value'


class MailWizardInvite(models.Model):
    res_id = models.IntegerField(blank=True, null=True, db_comment='Related Document ID')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailwizardinvite_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    res_model = models.CharField(db_comment='Related Document Model')
    message = models.TextField(blank=True, null=True, db_comment='Message')
    notify = models.BooleanField(blank=True, null=True, db_comment='Notify Recipients')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite'
        db_table_comment = 'Invite wizard'


class MailWizardInviteResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('mail_wizard_invite_id', 'res_partner_id')
    mail_wizard_invite = models.ForeignKey(MailWizardInvite, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN mail_wizard_invite AND res_partner'


class MailingContact(models.Model):
    message_bounce = models.IntegerField(blank=True, null=True, db_comment='Bounce')
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, blank=True, null=True, db_comment='Title')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailingcontact_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    email_normalized = models.CharField(blank=True, null=True, db_comment='Normalized Email')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    first_name = models.CharField(blank=True, null=True, db_comment='First Name')
    last_name = models.CharField(blank=True, null=True, db_comment='Last Name')
    company_name = models.CharField(blank=True, null=True, db_comment='Company Name')
    email = models.CharField(blank=True, null=True, db_comment='Email')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_contact'
        db_table_comment = 'Mailing Contact'


class MailingContactImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailingcontactimport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    contact_list = models.TextField(blank=True, null=True, db_comment='Contact List')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_contact_import'
        db_table_comment = 'Mailing Contact Import'


class MailingContactImportMailingListRel(models.Model):
    pk = models.CompositePrimaryKey('mailing_contact_import_id', 'mailing_list_id')
    mailing_contact_import = models.ForeignKey(MailingContactImport, models.DO_NOTHING)
    mailing_list = models.ForeignKey('MailingList', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mailing_contact_import_mailing_list_rel'
        db_table_comment = 'RELATION BETWEEN mailing_contact_import AND mailing_list'


class MailingContactMailingContactToListRel(models.Model):
    pk = models.CompositePrimaryKey('mailing_contact_to_list_id', 'mailing_contact_id')
    mailing_contact_to_list = models.ForeignKey('MailingContactToList', models.DO_NOTHING)
    mailing_contact = models.ForeignKey(MailingContact, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mailing_contact_mailing_contact_to_list_rel'
        db_table_comment = 'RELATION BETWEEN mailing_contact_to_list AND mailing_contact'


class MailingContactResPartnerCategoryRel(models.Model):
    pk = models.CompositePrimaryKey('mailing_contact_id', 'res_partner_category_id')
    mailing_contact = models.ForeignKey(MailingContact, models.DO_NOTHING)
    res_partner_category = models.ForeignKey('ResPartnerCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mailing_contact_res_partner_category_rel'
        db_table_comment = 'RELATION BETWEEN mailing_contact AND res_partner_category'


class MailingContactToList(models.Model):
    mailing_list = models.ForeignKey('MailingList', models.DO_NOTHING, db_comment='Mailing List')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailingcontacttolist_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_contact_to_list'
        db_table_comment = 'Add Contacts to Mailing List'


class MailingFilter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Saved by')
    mailing_model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Recipients Model')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailingfilter_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Filter Name')
    mailing_domain = models.CharField(db_comment='Filter Domain')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_filter'
        db_table_comment = 'Mailing Favorite Filters'


class MailingList(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailinglist_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Mailing List')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    is_public = models.BooleanField(blank=True, null=True, db_comment='Show In Preferences')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_list'
        db_table_comment = 'Mailing List'


class MailingListMailingListMergeRel(models.Model):
    pk = models.CompositePrimaryKey('mailing_list_merge_id', 'mailing_list_id')
    mailing_list_merge = models.ForeignKey('MailingListMerge', models.DO_NOTHING)
    mailing_list = models.ForeignKey(MailingList, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mailing_list_mailing_list_merge_rel'
        db_table_comment = 'RELATION BETWEEN mailing_list_merge AND mailing_list'


class MailingListMerge(models.Model):
    dest_list = models.ForeignKey(MailingList, models.DO_NOTHING, blank=True, null=True, db_comment='Destination Mailing List')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailinglistmerge_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    merge_options = models.CharField(db_comment='Merge Option')
    new_list_name = models.CharField(blank=True, null=True, db_comment='New Mailing List Name')
    archive_src_lists = models.BooleanField(blank=True, null=True, db_comment='Archive source mailing lists')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_list_merge'
        db_table_comment = 'Merge Mass Mailing List'


class MailingMailing(models.Model):
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, db_comment='Source')
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True, db_comment='UTM Campaign')
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True, db_comment='Medium')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Responsible')
    mailing_model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Recipients Model')
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True, db_comment='Mail Server')
    mailing_filter = models.ForeignKey(MailingFilter, models.DO_NOTHING, blank=True, null=True, db_comment='Favorite Filter')
    ab_testing_pc = models.IntegerField(blank=True, null=True, db_comment='A/B Testing percentage')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='mailingmailing_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailingmailing_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    lang = models.CharField(blank=True, null=True, db_comment='Language')
    subject = models.CharField(db_comment='Subject')
    preview = models.CharField(blank=True, null=True, db_comment='Preview')
    email_from = models.CharField(db_comment='Send From')
    schedule_type = models.CharField(db_comment='Schedule')
    state = models.CharField(db_comment='Status')
    mailing_type = models.CharField(db_comment='Mailing Type')
    reply_to_mode = models.CharField(blank=True, null=True, db_comment='Reply-To Mode')
    reply_to = models.CharField(blank=True, null=True, db_comment='Reply To')
    mailing_domain = models.CharField(blank=True, null=True, db_comment='Domain')
    body_arch = models.TextField(blank=True, null=True, db_comment='Body')
    body_html = models.TextField(blank=True, null=True, db_comment='Body converted to be sent by mail')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    favorite = models.BooleanField(blank=True, null=True, db_comment='Favorite')
    keep_archives = models.BooleanField(blank=True, null=True, db_comment='Keep Archives')
    ab_testing_enabled = models.BooleanField(blank=True, null=True, db_comment='Allow A/B Testing')
    kpi_mail_required = models.BooleanField(blank=True, null=True, db_comment='KPI mail required')
    favorite_date = models.DateTimeField(blank=True, null=True, db_comment='Favorite Date')
    sent_date = models.DateTimeField(blank=True, null=True, db_comment='Sent Date')
    schedule_date = models.DateTimeField(blank=True, null=True, db_comment='Scheduled for')
    calendar_date = models.DateTimeField(blank=True, null=True, db_comment='Calendar Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_mailing'
        db_table_comment = 'Mass Mailing'


class MailingMailingScheduleDate(models.Model):
    mass_mailing = models.ForeignKey(MailingMailing, models.DO_NOTHING, db_comment='Mass Mailing')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailingmailingscheduledate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    schedule_date = models.DateTimeField(blank=True, null=True, db_comment='Scheduled for')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_mailing_schedule_date'
        db_table_comment = 'schedule a mailing'


class MailingMailingTest(models.Model):
    mass_mailing = models.ForeignKey(MailingMailing, models.DO_NOTHING, db_comment='Mailing')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailingmailingtest_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    email_to = models.TextField(db_comment='Recipients')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_mailing_test'
        db_table_comment = 'Sample Mail Wizard'


class MailingSubscription(models.Model):
    contact = models.ForeignKey(MailingContact, models.DO_NOTHING, db_comment='Contact')
    list = models.ForeignKey(MailingList, models.DO_NOTHING, db_comment='Mailing List')
    opt_out_reason = models.ForeignKey('MailingSubscriptionOptout', models.DO_NOTHING, blank=True, null=True, db_comment='Reason')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailingsubscription_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    opt_out = models.BooleanField(blank=True, null=True, db_comment='Opt Out')
    opt_out_datetime = models.DateTimeField(blank=True, null=True, db_comment='Unsubscription Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_subscription'
        unique_together = (('contact', 'list'),)
        db_table_comment = 'Mailing List Subscription'


class MailingSubscriptionOptout(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailingsubscriptionoptout_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(blank=True, null=True, db_comment='Reason')
    is_feedback = models.BooleanField(blank=True, null=True, db_comment='Ask For Feedback')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_subscription_optout'
        db_table_comment = 'Mailing Subscription Reason'


class MailingTrace(models.Model):
    mail_mail = models.ForeignKey(MailMail, models.DO_NOTHING, blank=True, null=True, db_comment='Mail')
    mail_mail_id_int = models.IntegerField(blank=True, null=True, db_comment='Mail ID (tech)')
    res_id = models.IntegerField(blank=True, null=True, db_comment='Document ID')
    mass_mailing = models.ForeignKey(MailingMailing, models.DO_NOTHING, blank=True, null=True, db_comment='Mailing')
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True, db_comment='Campaign')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mailingtrace_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    trace_type = models.CharField(db_comment='Type')
    email = models.CharField(blank=True, null=True, db_comment='Email')
    message_id = models.CharField(blank=True, null=True, db_comment='Message-ID')
    model = models.CharField(db_comment='Document model')
    trace_status = models.CharField(blank=True, null=True, db_comment='Status')
    failure_type = models.CharField(blank=True, null=True, db_comment='Failure type')
    failure_reason = models.TextField(blank=True, null=True, db_comment='Failure reason')
    sent_datetime = models.DateTimeField(blank=True, null=True, db_comment='Sent On')
    open_datetime = models.DateTimeField(blank=True, null=True, db_comment='Opened On')
    reply_datetime = models.DateTimeField(blank=True, null=True, db_comment='Replied On')
    links_click_datetime = models.DateTimeField(blank=True, null=True, db_comment='Clicked On')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mailing_trace'
        db_table_comment = 'Mailing Statistics'


class MassMailingIrAttachmentsRel(models.Model):
    pk = models.CompositePrimaryKey('mass_mailing_id', 'attachment_id')
    mass_mailing = models.ForeignKey(MailingMailing, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mass_mailing_ir_attachments_rel'
        db_table_comment = 'RELATION BETWEEN mailing_mailing AND ir_attachment'


class MessageAttachmentRel(models.Model):
    pk = models.CompositePrimaryKey('message_id', 'attachment_id')
    message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'message_attachment_rel'
        db_table_comment = 'RELATION BETWEEN mail_message AND ir_attachment'


class ModuleCountry(models.Model):
    pk = models.CompositePrimaryKey('module_id', 'country_id')
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'module_country'
        db_table_comment = 'RELATION BETWEEN ir_module_module AND res_country'


class MrpAccountWipAccounting(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, db_comment='Journal')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpaccountwipaccounting_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    reference = models.CharField(blank=True, null=True, db_comment='Reference')
    date = models.DateField(blank=True, null=True, db_comment='Date')
    reversal_date = models.DateField(db_comment='Reversal Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_account_wip_accounting'
        db_table_comment = 'Wizard to post Manufacturing WIP account move'


class MrpAccountWipAccountingLine(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Account')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    wip_accounting = models.ForeignKey(MrpAccountWipAccounting, models.DO_NOTHING, blank=True, null=True, db_comment='WIP accounting wizard')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpaccountwipaccountingline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    label = models.CharField(blank=True, null=True, db_comment='Label')
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Debit')
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Credit')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_account_wip_accounting_line'
        db_table_comment = 'Account move line to be created when posting WIP account move'


class MrpAccountWipAccountingMrpProductionRel(models.Model):
    pk = models.CompositePrimaryKey('mrp_account_wip_accounting_id', 'mrp_production_id')
    mrp_account_wip_accounting = models.ForeignKey(MrpAccountWipAccounting, models.DO_NOTHING)
    mrp_production = models.ForeignKey('MrpProduction', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_account_wip_accounting_mrp_production_rel'
        db_table_comment = 'RELATION BETWEEN mrp_account_wip_accounting AND mrp_production'


class MrpBatchProduce(models.Model):
    production = models.ForeignKey('MrpProduction', models.DO_NOTHING, blank=True, null=True, db_comment='Production')
    lot_qty = models.IntegerField(blank=True, null=True, db_comment='Number of SN')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpbatchproduce_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    lot_name = models.CharField(blank=True, null=True, db_comment='First Lot/SN')
    component_separator = models.CharField(db_comment='Component separator')
    lots_separator = models.CharField(db_comment='Lot separator')
    lots_quantity_separator = models.CharField(db_comment='Lot quantity separator')
    production_text = models.TextField(blank=True, null=True, db_comment='Batch Production')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_batch_produce'
        db_table_comment = 'Produce a batch of production order'


class MrpBom(models.Model):
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, db_comment='Product')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True, db_comment='Product Variant')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Unit of Measure')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True, db_comment='Operation Type')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    produce_delay = models.IntegerField(blank=True, null=True, db_comment='Manufacturing Lead Time')
    days_to_prepare_mo = models.IntegerField(blank=True, null=True, db_comment='Days to prepare Manufacturing Order')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpbom_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code = models.CharField(blank=True, null=True, db_comment='Reference')
    type = models.CharField(db_comment='BoM Type')
    ready_to_produce = models.CharField(db_comment='Manufacturing Readiness')
    consumption = models.CharField(db_comment='Flexible Consumption')
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    allow_operation_dependencies = models.BooleanField(blank=True, null=True, db_comment='Operation Dependencies')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_bom'
        db_table_comment = 'Bill of Material'


class MrpBomByproduct(models.Model):
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='By-product')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Unit of Measure')
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, blank=True, null=True, db_comment='BoM')
    operation = models.ForeignKey('MrpRoutingWorkcenter', models.DO_NOTHING, blank=True, null=True, db_comment='Produced in Operation')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpbombyproduct_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    cost_share = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Cost Share (%)')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_bom_byproduct'
        db_table_comment = 'Byproduct'


class MrpBomByproductProductTemplateAttributeValueRel(models.Model):
    pk = models.CompositePrimaryKey('mrp_bom_byproduct_id', 'product_template_attribute_value_id')
    mrp_bom_byproduct = models.ForeignKey(MrpBomByproduct, models.DO_NOTHING)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_bom_byproduct_product_template_attribute_value_rel'
        db_table_comment = 'RELATION BETWEEN mrp_bom_byproduct AND product_template_attribute_value'


class MrpBomLine(models.Model):
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Component')
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='Product Template')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Product Unit of Measure')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, db_comment='Parent BoM')
    operation = models.ForeignKey('MrpRoutingWorkcenter', models.DO_NOTHING, blank=True, null=True, db_comment='Consumed in Operation')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpbomline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    manual_consumption = models.BooleanField(blank=True, null=True, db_comment='Highlight Consumption')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    cost_share = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Cost Share (%)')

    class Meta:
        managed = False
        db_table = 'mrp_bom_line'
        db_table_comment = 'Bill of Material Line'


class MrpBomLineProductTemplateAttributeValueRel(models.Model):
    pk = models.CompositePrimaryKey('mrp_bom_line_id', 'product_template_attribute_value_id')
    mrp_bom_line = models.ForeignKey(MrpBomLine, models.DO_NOTHING)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_bom_line_product_template_attribute_value_rel'
        db_table_comment = 'RELATION BETWEEN mrp_bom_line AND product_template_attribute_value'


class MrpConsumptionWarning(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpconsumptionwarning_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_consumption_warning'
        db_table_comment = 'Wizard in case of consumption in warning/strict and more component has been used for a MO (related to the bom)'


class MrpConsumptionWarningLine(models.Model):
    mrp_consumption_warning = models.ForeignKey(MrpConsumptionWarning, models.DO_NOTHING, db_comment='Parent Wizard')
    mrp_production = models.ForeignKey('MrpProduction', models.DO_NOTHING, db_comment='Manufacturing Order')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Product')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpconsumptionwarningline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    product_consumed_qty_uom = models.FloatField(blank=True, null=True, db_comment='Consumed')
    product_expected_qty_uom = models.FloatField(blank=True, null=True, db_comment='To Consume')

    class Meta:
        managed = False
        db_table = 'mrp_consumption_warning_line'
        db_table_comment = 'Line of issue consumption'


class MrpConsumptionWarningMrpProductionRel(models.Model):
    pk = models.CompositePrimaryKey('mrp_consumption_warning_id', 'mrp_production_id')
    mrp_consumption_warning = models.ForeignKey(MrpConsumptionWarning, models.DO_NOTHING)
    mrp_production = models.ForeignKey('MrpProduction', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_consumption_warning_mrp_production_rel'
        db_table_comment = 'RELATION BETWEEN mrp_consumption_warning AND mrp_production'


class MrpProduction(models.Model):
    backorder_sequence = models.IntegerField(blank=True, null=True, db_comment='Backorder Sequence')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Product')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Product Unit of Measure')
    lot_producing = models.ForeignKey('StockLot', models.DO_NOTHING, blank=True, null=True, db_comment='Lot/Serial Number')
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, db_comment='Operation Type')
    location_src = models.ForeignKey('StockLocation', models.DO_NOTHING, db_comment='Components Location')
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name='mrpproduction_location_dest_set', db_comment='Finished Products Location')
    location_final = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name='mrpproduction_location_final_set', blank=True, null=True, db_comment='Final Location from procurement')
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, blank=True, null=True, db_comment='Bill of Material')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Responsible')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    procurement_group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, blank=True, null=True, db_comment='Procurement Group')
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING, blank=True, null=True, db_comment='Orderpoint')
    production_location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name='mrpproduction_production_location_set', blank=True, null=True, db_comment='Production Location')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='mrpproduction_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpproduction_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Reference')
    priority = models.CharField(blank=True, null=True, db_comment='Priority')
    origin = models.CharField(blank=True, null=True, db_comment='Source')
    state = models.CharField(blank=True, null=True, db_comment='State')
    reservation_state = models.CharField(blank=True, null=True, db_comment='MO Readiness')
    product_description_variants = models.CharField(blank=True, null=True, db_comment='Custom Description')
    consumption = models.CharField(db_comment='Consumption')
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity To Produce')
    qty_producing = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Quantity Producing')
    propagate_cancel = models.BooleanField(blank=True, null=True, db_comment='Propagate cancel and split')
    is_locked = models.BooleanField(blank=True, null=True, db_comment='Is Locked')
    is_planned = models.BooleanField(blank=True, null=True, db_comment='Its Operations are Planned')
    allow_workorder_dependencies = models.BooleanField(blank=True, null=True, db_comment='Allow Work Order Dependencies')
    is_outdated_bom = models.BooleanField(blank=True, null=True, db_comment='Outdated BoM')
    date_deadline = models.DateTimeField(blank=True, null=True, db_comment='Deadline')
    date_start = models.DateTimeField(db_comment='Start')
    date_finished = models.DateTimeField(blank=True, null=True, db_comment='End')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    product_uom_qty = models.FloatField(blank=True, null=True, db_comment='Total Quantity')
    extra_cost = models.FloatField(blank=True, null=True, db_comment='Extra Unit Cost')
    sale_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True, db_comment='Origin sale order line')

    class Meta:
        managed = False
        db_table = 'mrp_production'
        unique_together = (('name', 'company'),)
        db_table_comment = 'Manufacturing Order'


class MrpProductionBackorder(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpproductionbackorder_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_production_backorder'
        db_table_comment = 'Wizard to mark as done or create back order'


class MrpProductionBackorderLine(models.Model):
    mrp_production_backorder = models.ForeignKey(MrpProductionBackorder, models.DO_NOTHING, db_comment='MO Backorder')
    mrp_production = models.ForeignKey(MrpProduction, models.DO_NOTHING, db_comment='Manufacturing Order')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpproductionbackorderline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    to_backorder = models.BooleanField(blank=True, null=True, db_comment='To Backorder')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_production_backorder_line'
        db_table_comment = 'Backorder Confirmation Line'


class MrpProductionMrpProductionBackorderRel(models.Model):
    pk = models.CompositePrimaryKey('mrp_production_backorder_id', 'mrp_production_id')
    mrp_production_backorder = models.ForeignKey(MrpProductionBackorder, models.DO_NOTHING)
    mrp_production = models.ForeignKey(MrpProduction, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_production_mrp_production_backorder_rel'
        db_table_comment = 'RELATION BETWEEN mrp_production_backorder AND mrp_production'


class MrpProductionPickingLabelTypeRel(models.Model):
    pk = models.CompositePrimaryKey('picking_label_type_id', 'mrp_production_id')
    picking_label_type = models.ForeignKey('PickingLabelType', models.DO_NOTHING)
    mrp_production = models.ForeignKey(MrpProduction, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_production_picking_label_type_rel'
        db_table_comment = 'RELATION BETWEEN picking_label_type AND mrp_production'


class MrpProductionSplit(models.Model):
    production_split_multi = models.ForeignKey('MrpProductionSplitMulti', models.DO_NOTHING, blank=True, null=True, db_comment='Split Productions')
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True, db_comment='Manufacturing Order')
    counter = models.IntegerField(blank=True, null=True, db_comment='Split #')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpproductionsplit_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_production_split'
        db_table_comment = 'Wizard to Split a Production'


class MrpProductionSplitLine(models.Model):
    mrp_production_split = models.ForeignKey(MrpProductionSplit, models.DO_NOTHING, db_comment='Split Production')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Responsible')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='mrpproductionsplitline_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpproductionsplitline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity To Produce')
    date = models.DateTimeField(blank=True, null=True, db_comment='Schedule Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_production_split_line'
        db_table_comment = 'Split Production Detail'


class MrpProductionSplitMulti(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpproductionsplitmulti_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_production_split_multi'
        db_table_comment = 'Wizard to Split Multiple Productions'


class MrpRoutingWorkcenter(models.Model):
    workcenter = models.ForeignKey('MrpWorkcenter', models.DO_NOTHING, db_comment='Work Center')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, db_comment='Bill of Material')
    time_mode_batch = models.IntegerField(blank=True, null=True, db_comment='Based on')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrproutingworkcenter_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Operation')
    worksheet_type = models.CharField(blank=True, null=True, db_comment='Worksheet')
    worksheet_google_slide = models.CharField(blank=True, null=True, db_comment='Google Slide')
    time_mode = models.CharField(blank=True, null=True, db_comment='Duration Computation')
    note = models.TextField(blank=True, null=True, db_comment='Description')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    time_cycle_manual = models.FloatField(blank=True, null=True, db_comment='Manual Duration')

    class Meta:
        managed = False
        db_table = 'mrp_routing_workcenter'
        db_table_comment = 'Work Center Usage'


class MrpRoutingWorkcenterDependenciesRel(models.Model):
    pk = models.CompositePrimaryKey('operation_id', 'blocked_by_id')
    operation = models.ForeignKey(MrpRoutingWorkcenter, models.DO_NOTHING)
    blocked_by = models.ForeignKey(MrpRoutingWorkcenter, models.DO_NOTHING, related_name='mrproutingworkcenterdependenciesrel_blocked_by_set')

    class Meta:
        managed = False
        db_table = 'mrp_routing_workcenter_dependencies_rel'
        db_table_comment = 'RELATION BETWEEN mrp_routing_workcenter AND mrp_routing_workcenter'


class MrpRoutingWorkcenterProductTemplateAttributeValueRel(models.Model):
    pk = models.CompositePrimaryKey('mrp_routing_workcenter_id', 'product_template_attribute_value_id')
    mrp_routing_workcenter = models.ForeignKey(MrpRoutingWorkcenter, models.DO_NOTHING)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_routing_workcenter_product_template_attribute_value_rel'
        db_table_comment = 'RELATION BETWEEN mrp_routing_workcenter AND product_template_attribute_value'


class MrpUnbuild(models.Model):
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Product')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Unit of Measure')
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, blank=True, null=True, db_comment='Bill of Material')
    mo = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True, db_comment='Manufacturing Order')
    lot = models.ForeignKey('StockLot', models.DO_NOTHING, blank=True, null=True, db_comment='Lot/Serial Number')
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, db_comment='Source Location')
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name='mrpunbuild_location_dest_set', db_comment='Destination Location')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpunbuild_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Reference')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    product_qty = models.FloatField(db_comment='Quantity')

    class Meta:
        managed = False
        db_table = 'mrp_unbuild'
        db_table_comment = 'Unbuild Order'


class MrpWorkcenter(models.Model):
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, db_comment='Resource')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True, db_comment='Working Hours')
    sequence = models.IntegerField(db_comment='Sequence')
    color = models.IntegerField(blank=True, null=True, db_comment='Color')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpworkcenter_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Work Center')
    code = models.CharField(blank=True, null=True, db_comment='Code')
    working_state = models.CharField(blank=True, null=True, db_comment='Workcenter Status')
    note = models.TextField(blank=True, null=True, db_comment='Description')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    time_efficiency = models.FloatField(blank=True, null=True, db_comment='Time Efficiency')
    default_capacity = models.FloatField(blank=True, null=True, db_comment='Capacity')
    costs_hour = models.FloatField(blank=True, null=True, db_comment='Cost per hour')
    time_start = models.FloatField(blank=True, null=True, db_comment='Setup Time')
    time_stop = models.FloatField(blank=True, null=True, db_comment='Cleanup Time')
    oee_target = models.FloatField(blank=True, null=True, db_comment='OEE Target')
    expense_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Expense Account')
    analytic_distribution = models.JSONField(blank=True, null=True, db_comment='Analytic Distribution')

    class Meta:
        managed = False
        db_table = 'mrp_workcenter'
        db_table_comment = 'Work Center'


class MrpWorkcenterAlternativeRel(models.Model):
    pk = models.CompositePrimaryKey('workcenter_id', 'alternative_workcenter_id')
    workcenter = models.ForeignKey(MrpWorkcenter, models.DO_NOTHING)
    alternative_workcenter = models.ForeignKey(MrpWorkcenter, models.DO_NOTHING, related_name='mrpworkcenteralternativerel_alternative_workcenter_set')

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_alternative_rel'
        db_table_comment = 'RELATION BETWEEN mrp_workcenter AND mrp_workcenter'


class MrpWorkcenterCapacity(models.Model):
    workcenter = models.ForeignKey(MrpWorkcenter, models.DO_NOTHING, db_comment='Work Center')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Product')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpworkcentercapacity_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    capacity = models.FloatField(blank=True, null=True, db_comment='Capacity')
    time_start = models.FloatField(blank=True, null=True, db_comment='Setup Time (minutes)')
    time_stop = models.FloatField(blank=True, null=True, db_comment='Cleanup Time (minutes)')

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_capacity'
        unique_together = (('workcenter', 'product'),)
        db_table_comment = 'Work Center Capacity'


class MrpWorkcenterMrpWorkcenterTagRel(models.Model):
    pk = models.CompositePrimaryKey('mrp_workcenter_id', 'mrp_workcenter_tag_id')
    mrp_workcenter = models.ForeignKey(MrpWorkcenter, models.DO_NOTHING)
    mrp_workcenter_tag = models.ForeignKey('MrpWorkcenterTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_mrp_workcenter_tag_rel'
        db_table_comment = 'RELATION BETWEEN mrp_workcenter AND mrp_workcenter_tag'


class MrpWorkcenterProductivity(models.Model):
    workcenter = models.ForeignKey(MrpWorkcenter, models.DO_NOTHING, db_comment='Work Center')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    workorder = models.ForeignKey('MrpWorkorder', models.DO_NOTHING, blank=True, null=True, db_comment='Work Order')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='User')
    loss = models.ForeignKey('MrpWorkcenterProductivityLoss', models.DO_NOTHING, db_comment='Loss Reason')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='mrpworkcenterproductivity_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpworkcenterproductivity_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    loss_type = models.CharField(blank=True, null=True, db_comment='Effectiveness')
    description = models.TextField(blank=True, null=True, db_comment='Description')
    date_start = models.DateTimeField(db_comment='Start Date')
    date_end = models.DateTimeField(blank=True, null=True, db_comment='End Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    duration = models.FloatField(blank=True, null=True, db_comment='Duration')
    account_move_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, blank=True, null=True, db_comment='Account Move Line')

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_productivity'
        db_table_comment = 'Workcenter Productivity Log'


class MrpWorkcenterProductivityLoss(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    loss = models.ForeignKey('MrpWorkcenterProductivityLossType', models.DO_NOTHING, blank=True, null=True, db_comment='Category')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpworkcenterproductivityloss_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    loss_type = models.CharField(blank=True, null=True, db_comment='Effectiveness Category')
    name = models.JSONField(db_comment='Blocking Reason')
    manual = models.BooleanField(blank=True, null=True, db_comment='Is a Blocking Reason')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_productivity_loss'
        db_table_comment = 'Workcenter Productivity Losses'


class MrpWorkcenterProductivityLossType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpworkcenterproductivitylosstype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    loss_type = models.CharField(db_comment='Category')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_productivity_loss_type'
        db_table_comment = 'MRP Workorder productivity losses'


class MrpWorkcenterTag(models.Model):
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpworkcentertag_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(unique=True, db_comment='Tag Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_tag'
        db_table_comment = 'Add tag for the workcenter'


class MrpWorkorder(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    workcenter = models.ForeignKey(MrpWorkcenter, models.DO_NOTHING, db_comment='Work Center')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Unit of Measure')
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING, db_comment='Manufacturing Order')
    leave = models.ForeignKey('ResourceCalendarLeaves', models.DO_NOTHING, blank=True, null=True, db_comment='Leave')
    duration_percent = models.IntegerField(blank=True, null=True, db_comment='Duration Deviation (%)')
    operation = models.ForeignKey(MrpRoutingWorkcenter, models.DO_NOTHING, blank=True, null=True, db_comment='Operation')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='mrpworkorder_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Work Order')
    barcode = models.CharField(blank=True, null=True, db_comment='Barcode')
    production_availability = models.CharField(blank=True, null=True, db_comment='Stock Availability')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    qty_produced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Quantity')
    duration_expected = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Expected Duration')
    qty_reported_from_previous_wo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Carried Quantity')
    date_start = models.DateTimeField(blank=True, null=True, db_comment='Start')
    date_finished = models.DateTimeField(blank=True, null=True, db_comment='End')
    production_date = models.DateTimeField(blank=True, null=True, db_comment='Production Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    duration = models.FloatField(blank=True, null=True, db_comment='Real Duration')
    duration_unit = models.FloatField(blank=True, null=True, db_comment='Duration Per Unit')
    costs_hour = models.FloatField(blank=True, null=True, db_comment='Cost per hour')

    class Meta:
        managed = False
        db_table = 'mrp_workorder'
        db_table_comment = 'Work Order'


class MrpWorkorderDependenciesRel(models.Model):
    pk = models.CompositePrimaryKey('workorder_id', 'blocked_by_id')
    workorder = models.ForeignKey(MrpWorkorder, models.DO_NOTHING)
    blocked_by = models.ForeignKey(MrpWorkorder, models.DO_NOTHING, related_name='mrpworkorderdependenciesrel_blocked_by_set')

    class Meta:
        managed = False
        db_table = 'mrp_workorder_dependencies_rel'
        db_table_comment = 'RELATION BETWEEN mrp_workorder AND mrp_workorder'


class MrpWorkorderMoAnalyticRel(models.Model):
    pk = models.CompositePrimaryKey('mrp_workorder_id', 'account_analytic_line_id')
    mrp_workorder = models.ForeignKey(MrpWorkorder, models.DO_NOTHING)
    account_analytic_line = models.ForeignKey(AccountAnalyticLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_workorder_mo_analytic_rel'
        db_table_comment = 'RELATION BETWEEN mrp_workorder AND account_analytic_line'


class MrpWorkorderWcAnalyticRel(models.Model):
    pk = models.CompositePrimaryKey('mrp_workorder_id', 'account_analytic_line_id')
    mrp_workorder = models.ForeignKey(MrpWorkorder, models.DO_NOTHING)
    account_analytic_line = models.ForeignKey(AccountAnalyticLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_workorder_wc_analytic_rel'
        db_table_comment = 'RELATION BETWEEN mrp_workorder AND account_analytic_line'


class MultipleInvoice(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence No')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Journal')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='multipleinvoice_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    copy_name = models.CharField(blank=True, null=True, db_comment='Invoice Copy Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'multiple_invoice'
        db_table_comment = 'Multiple Invoice'


class MultipleInvoiceLayout(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, db_comment='Journal')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='multipleinvoicelayout_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'multiple_invoice_layout'
        db_table_comment = 'Multiple Invoice Document Layout'


class OnboardingOnboarding(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='onboardingonboarding_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    route_name = models.CharField(unique=True, db_comment='One word name')
    text_completed = models.CharField(blank=True, null=True, db_comment='Message at completion')
    panel_close_action_name = models.CharField(blank=True, null=True, db_comment='Closing action')
    name = models.JSONField(blank=True, null=True, db_comment='Name of the onboarding')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'onboarding_onboarding'
        db_table_comment = 'Onboarding'


class OnboardingOnboardingOnboardingOnboardingStepRel(models.Model):
    pk = models.CompositePrimaryKey('onboarding_onboarding_id', 'onboarding_onboarding_step_id')
    onboarding_onboarding = models.ForeignKey(OnboardingOnboarding, models.DO_NOTHING)
    onboarding_onboarding_step = models.ForeignKey('OnboardingOnboardingStep', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'onboarding_onboarding_onboarding_onboarding_step_rel'
        db_table_comment = 'RELATION BETWEEN onboarding_onboarding AND onboarding_onboarding_step'


class OnboardingOnboardingStep(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='onboardingonboardingstep_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    done_icon = models.CharField(blank=True, null=True, db_comment='Font Awesome Icon when completed')
    step_image_filename = models.CharField(blank=True, null=True, db_comment='Step Image Filename')
    panel_step_open_action_name = models.CharField(blank=True, null=True, db_comment='Opening action')
    title = models.JSONField(blank=True, null=True, db_comment='Title')
    description = models.JSONField(blank=True, null=True, db_comment='Description')
    button_text = models.JSONField(db_comment='Button text')
    done_text = models.JSONField(blank=True, null=True, db_comment='Text to show when step is completed')
    step_image_alt = models.JSONField(blank=True, null=True, db_comment='Alt Text for the Step Image')
    is_per_company = models.BooleanField(blank=True, null=True, db_comment='Is per company')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'onboarding_onboarding_step'
        db_table_comment = 'Onboarding Step'


class OnboardingProgress(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    onboarding = models.ForeignKey(OnboardingOnboarding, models.DO_NOTHING, db_comment='Related onboarding tracked')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='onboardingprogress_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    onboarding_state = models.CharField(blank=True, null=True, db_comment='Onboarding progress')
    is_onboarding_closed = models.BooleanField(blank=True, null=True, db_comment='Was panel closed?')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'onboarding_progress'
        db_table_comment = 'Onboarding Progress Tracker'


class OnboardingProgressOnboardingProgressStepRel(models.Model):
    pk = models.CompositePrimaryKey('onboarding_progress_id', 'onboarding_progress_step_id')
    onboarding_progress = models.ForeignKey(OnboardingProgress, models.DO_NOTHING)
    onboarding_progress_step = models.ForeignKey('OnboardingProgressStep', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'onboarding_progress_onboarding_progress_step_rel'
        db_table_comment = 'RELATION BETWEEN onboarding_progress AND onboarding_progress_step'


class OnboardingProgressStep(models.Model):
    step = models.ForeignKey(OnboardingOnboardingStep, models.DO_NOTHING, db_comment='Onboarding Step')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='onboardingprogressstep_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    step_state = models.CharField(blank=True, null=True, db_comment='Onboarding Step Progress')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'onboarding_progress_step'
        db_table_comment = 'Onboarding Progress Step Tracker'


class PaymentCaptureWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='paymentcapturewizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    amount_to_capture = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount To Capture')
    void_remaining_amount = models.BooleanField(blank=True, null=True, db_comment='Void Remaining Amount')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'payment_capture_wizard'
        db_table_comment = 'Payment Capture Wizard'


class PaymentCaptureWizardPaymentTransactionRel(models.Model):
    pk = models.CompositePrimaryKey('payment_capture_wizard_id', 'payment_transaction_id')
    payment_capture_wizard = models.ForeignKey(PaymentCaptureWizard, models.DO_NOTHING)
    payment_transaction = models.ForeignKey('PaymentTransaction', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_capture_wizard_payment_transaction_rel'
        db_table_comment = 'RELATION BETWEEN payment_capture_wizard AND payment_transaction'


class PaymentCountryRel(models.Model):
    pk = models.CompositePrimaryKey('payment_id', 'country_id')
    payment = models.ForeignKey('PaymentProvider', models.DO_NOTHING)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_country_rel'
        db_table_comment = 'RELATION BETWEEN payment_provider AND res_country'


class PaymentCurrencyRel(models.Model):
    pk = models.CompositePrimaryKey('payment_provider_id', 'currency_id')
    payment_provider = models.ForeignKey('PaymentProvider', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_currency_rel'
        db_table_comment = 'RELATION BETWEEN payment_provider AND res_currency'


class PaymentLinkWizard(models.Model):
    res_id = models.IntegerField(db_comment='Related Document ID')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='paymentlinkwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    res_model = models.CharField(db_comment='Related Document Model')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Amount')
    amount_max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount Max')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    discount_date = models.DateField(blank=True, null=True, db_comment='Discount Date')
    open_installments = models.JSONField(blank=True, null=True, db_comment='Open Installments')
    has_eligible_epd = models.BooleanField(blank=True, null=True, db_comment='Has Eligible Epd')
    amount_paid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Already Paid')

    class Meta:
        managed = False
        db_table = 'payment_link_wizard'
        db_table_comment = 'Generate Payment Link'


class PaymentMethod(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    primary_payment_method = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Primary Payment Method')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='paymentmethod_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code = models.CharField(db_comment='Code')
    support_refund = models.CharField(db_comment='Refund')
    name = models.JSONField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    support_tokenization = models.BooleanField(blank=True, null=True, db_comment='Tokenization')
    support_express_checkout = models.BooleanField(blank=True, null=True, db_comment='Express Checkout')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'payment_method'
        db_table_comment = 'Payment Method'


class PaymentMethodPaymentProviderRel(models.Model):
    pk = models.CompositePrimaryKey('payment_method_id', 'payment_provider_id')
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING)
    payment_provider = models.ForeignKey('PaymentProvider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_method_payment_provider_rel'
        db_table_comment = 'RELATION BETWEEN payment_method AND payment_provider'


class PaymentMethodResCountryRel(models.Model):
    pk = models.CompositePrimaryKey('payment_method_id', 'res_country_id')
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING)
    res_country = models.ForeignKey('ResCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_method_res_country_rel'
        db_table_comment = 'RELATION BETWEEN payment_method AND res_country'


class PaymentMethodResCurrencyRel(models.Model):
    pk = models.CompositePrimaryKey('payment_method_id', 'res_currency_id')
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING)
    res_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_method_res_currency_rel'
        db_table_comment = 'RELATION BETWEEN payment_method AND res_currency'


class PaymentProvider(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    redirect_form_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True, db_comment='Redirect Form Template')
    inline_form_view = models.ForeignKey(IrUiView, models.DO_NOTHING, related_name='paymentprovider_inline_form_view_set', blank=True, null=True, db_comment='Inline Form Template')
    token_inline_form_view = models.ForeignKey(IrUiView, models.DO_NOTHING, related_name='paymentprovider_token_inline_form_view_set', blank=True, null=True, db_comment='Token Inline Form Template')
    express_checkout_form_view = models.ForeignKey(IrUiView, models.DO_NOTHING, related_name='paymentprovider_express_checkout_form_view_set', blank=True, null=True, db_comment='Express Checkout Form Template')
    color = models.IntegerField(blank=True, null=True, db_comment='Color')
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True, db_comment='Corresponding Module')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='paymentprovider_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code = models.CharField(db_comment='Code')
    state = models.CharField(db_comment='State')
    name = models.JSONField(db_comment='Name')
    pre_msg = models.JSONField(blank=True, null=True, db_comment='Help Message')
    pending_msg = models.JSONField(blank=True, null=True, db_comment='Pending Message')
    auth_msg = models.JSONField(blank=True, null=True, db_comment='Authorize Message')
    done_msg = models.JSONField(blank=True, null=True, db_comment='Done Message')
    cancel_msg = models.JSONField(blank=True, null=True, db_comment='Cancelled Message')
    maximum_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Maximum Amount')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Published')
    allow_tokenization = models.BooleanField(blank=True, null=True, db_comment='Allow Saving Payment Methods')
    capture_manually = models.BooleanField(blank=True, null=True, db_comment='Capture Amount Manually')
    allow_express_checkout = models.BooleanField(blank=True, null=True, db_comment='Allow Express Checkout')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    so_reference_type = models.CharField(blank=True, null=True, db_comment='Communication')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    razorpay_key_id = models.CharField(blank=True, null=True, db_comment='Razorpay Key Id')
    razorpay_key_secret = models.CharField(blank=True, null=True, db_comment='Razorpay Key Secret')
    razorpay_webhook_secret = models.CharField(blank=True, null=True, db_comment='Razorpay Webhook Secret')
    razorpay_account_id = models.CharField(blank=True, null=True, db_comment='Razorpay Account ID')
    razorpay_refresh_token = models.CharField(blank=True, null=True, db_comment='Razorpay Refresh Token')
    razorpay_public_token = models.CharField(blank=True, null=True, db_comment='Razorpay Public Token')
    razorpay_access_token = models.CharField(blank=True, null=True, db_comment='Razorpay Access Token')
    razorpay_access_token_expiry = models.DateTimeField(blank=True, null=True, db_comment='Razorpay Access Token Expiry')

    class Meta:
        managed = False
        db_table = 'payment_provider'
        db_table_comment = 'Payment Provider'


class PaymentProviderOnboardingWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='paymentprovideronboardingwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    payment_method = models.CharField(blank=True, null=True, db_comment='Payment Method')
    paypal_email_account = models.CharField(blank=True, null=True, db_comment='Email')
    manual_name = models.CharField(blank=True, null=True, db_comment='Method')
    journal_name = models.CharField(blank=True, null=True, db_comment='Bank Name')
    acc_number = models.CharField(blank=True, null=True, db_comment='Account Number')
    manual_post_msg = models.TextField(blank=True, null=True, db_comment='Payment Instructions')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'payment_provider_onboarding_wizard'
        db_table_comment = 'Payment provider onboarding wizard'


class PaymentProviderPosPaymentMethodRel(models.Model):
    pk = models.CompositePrimaryKey('pos_payment_method_id', 'payment_provider_id')
    pos_payment_method = models.ForeignKey('PosPaymentMethod', models.DO_NOTHING)
    payment_provider = models.ForeignKey(PaymentProvider, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_provider_pos_payment_method_rel'
        db_table_comment = 'RELATION BETWEEN pos_payment_method AND payment_provider'


class PaymentRefundWizard(models.Model):
    payment = models.ForeignKey(AccountPayment, models.DO_NOTHING, blank=True, null=True, db_comment='Payment')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='paymentrefundwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    amount_to_refund = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Refund Amount')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'payment_refund_wizard'
        db_table_comment = 'Payment Refund Wizard'


class PaymentToken(models.Model):
    provider = models.ForeignKey(PaymentProvider, models.DO_NOTHING, db_comment='Provider')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING, db_comment='Payment Method')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Partner')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='paymenttoken_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    payment_details = models.CharField(blank=True, null=True, db_comment='Payment Details')
    provider_ref = models.CharField(db_comment='Provider Reference')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'payment_token'
        db_table_comment = 'Payment Token'


class PaymentTransaction(models.Model):
    provider = models.ForeignKey(PaymentProvider, models.DO_NOTHING, db_comment='Provider')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING, db_comment='Payment Method')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, db_comment='Currency')
    token = models.ForeignKey(PaymentToken, models.DO_NOTHING, blank=True, null=True, db_comment='Payment Token')
    source_transaction = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Source Transaction')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Customer')
    partner_state = models.ForeignKey('ResCountryState', models.DO_NOTHING, blank=True, null=True, db_comment='State')
    partner_country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='paymenttransaction_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    reference = models.CharField(unique=True, db_comment='Reference')
    provider_reference = models.CharField(blank=True, null=True, db_comment='Provider Reference')
    state = models.CharField(db_comment='Status')
    operation = models.CharField(blank=True, null=True, db_comment='Operation')
    landing_route = models.CharField(blank=True, null=True, db_comment='Landing Route')
    partner_name = models.CharField(blank=True, null=True, db_comment='Partner Name')
    partner_lang = models.CharField(blank=True, null=True, db_comment='Language')
    partner_email = models.CharField(blank=True, null=True, db_comment='Email')
    partner_address = models.CharField(blank=True, null=True, db_comment='Address')
    partner_zip = models.CharField(blank=True, null=True, db_comment='Zip')
    partner_city = models.CharField(blank=True, null=True, db_comment='City')
    partner_phone = models.CharField(blank=True, null=True, db_comment='Phone')
    state_message = models.TextField(blank=True, null=True, db_comment='Message')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Amount')
    is_post_processed = models.BooleanField(blank=True, null=True, db_comment='Is Post-processed')
    tokenize = models.BooleanField(blank=True, null=True, db_comment='Create Token')
    last_state_change = models.DateTimeField(blank=True, null=True, db_comment='Last State Change Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    payment = models.ForeignKey(AccountPayment, models.DO_NOTHING, blank=True, null=True, db_comment='Payment')
    is_donation = models.BooleanField(blank=True, null=True, db_comment='Is donation')
    pos_order = models.ForeignKey('PosOrder', models.DO_NOTHING, blank=True, null=True, db_comment='POS Order')

    class Meta:
        managed = False
        db_table = 'payment_transaction'
        db_table_comment = 'Payment Transaction'


class PhoneBlacklist(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='phoneblacklist_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    number = models.CharField(unique=True, db_comment='Phone Number')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'phone_blacklist'
        db_table_comment = 'Phone Blacklist'


class PhoneBlacklistRemove(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='phoneblacklistremove_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    phone = models.CharField(db_comment='Phone Number')
    reason = models.CharField(blank=True, null=True, db_comment='Reason')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'phone_blacklist_remove'
        db_table_comment = 'Remove phone from blacklist'


class PickingLabelType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='pickinglabeltype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    label_type = models.CharField(db_comment='Labels to print')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'picking_label_type'
        db_table_comment = 'Choose whether to print product or lot/sn labels'


class PickingLabelTypeStockPickingRel(models.Model):
    pk = models.CompositePrimaryKey('picking_label_type_id', 'stock_picking_id')
    picking_label_type = models.ForeignKey(PickingLabelType, models.DO_NOTHING)
    stock_picking = models.ForeignKey('StockPicking', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'picking_label_type_stock_picking_rel'
        db_table_comment = 'RELATION BETWEEN picking_label_type AND stock_picking'


class PickingTypeFavoriteUserRel(models.Model):
    pk = models.CompositePrimaryKey('picking_type_id', 'user_id')
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'picking_type_favorite_user_rel'
        db_table_comment = 'RELATION BETWEEN stock_picking_type AND res_users'


class PortalShare(models.Model):
    res_id = models.IntegerField(db_comment='Related Document ID')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='portalshare_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    res_model = models.CharField(db_comment='Related Document Model')
    note = models.TextField(blank=True, null=True, db_comment='Note')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'portal_share'
        db_table_comment = 'Portal Sharing'


class PortalShareResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('portal_share_id', 'res_partner_id')
    portal_share = models.ForeignKey(PortalShare, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_share_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN portal_share AND res_partner'


class PortalWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='portalwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    welcome_message = models.TextField(blank=True, null=True, db_comment='Invitation Message')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'portal_wizard'
        db_table_comment = 'Grant Portal Access'


class PortalWizardResPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('portal_wizard_id', 'res_partner_id')
    portal_wizard = models.ForeignKey(PortalWizard, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_wizard_res_partner_rel'
        db_table_comment = 'RELATION BETWEEN portal_wizard AND res_partner'


class PortalWizardUser(models.Model):
    wizard = models.ForeignKey(PortalWizard, models.DO_NOTHING, db_comment='Wizard')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Contact')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='portalwizarduser_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    email = models.CharField(blank=True, null=True, db_comment='Email')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'portal_wizard_user'
        db_table_comment = 'Portal User Config'


class PosBill(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='posbill_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    value = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Coin/Bill Value')
    for_all_config = models.BooleanField(blank=True, null=True, db_comment='For All PoS')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'pos_bill'
        db_table_comment = 'Coins/Bills'


class PosBillPosConfigRel(models.Model):
    pk = models.CompositePrimaryKey('pos_config_id', 'pos_bill_id')
    pos_config = models.ForeignKey('PosConfig', models.DO_NOTHING)
    pos_bill = models.ForeignKey(PosBill, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_bill_pos_config_rel'
        db_table_comment = 'RELATION BETWEEN pos_config AND pos_bill'


class PosCategory(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Category')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    color = models.IntegerField(blank=True, null=True, db_comment='Color')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='poscategory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Category Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'pos_category'
        db_table_comment = 'Point of Sale Category'


class PosCategoryPosConfigRel(models.Model):
    pk = models.CompositePrimaryKey('pos_config_id', 'pos_category_id')
    pos_config = models.ForeignKey('PosConfig', models.DO_NOTHING)
    pos_category = models.ForeignKey(PosCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_category_pos_config_rel'
        db_table_comment = 'RELATION BETWEEN pos_config AND pos_category'


class PosCategoryProductTemplateRel(models.Model):
    pk = models.CompositePrimaryKey('product_template_id', 'pos_category_id')
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    pos_category = models.ForeignKey(PosCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_category_product_template_rel'
        db_table_comment = 'RELATION BETWEEN product_template AND pos_category'


class PosCategoryResConfigSettingsRel(models.Model):
    pk = models.CompositePrimaryKey('res_config_settings_id', 'pos_category_id')
    res_config_settings = models.ForeignKey('ResConfigSettings', models.DO_NOTHING)
    pos_category = models.ForeignKey(PosCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_category_res_config_settings_rel'
        db_table_comment = 'RELATION BETWEEN res_config_settings AND pos_category'


class PosCloseSessionWizard(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Destination account')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='posclosesessionwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    message = models.TextField(blank=True, null=True, db_comment='Information message')
    account_readonly = models.BooleanField(blank=True, null=True, db_comment='Destination account is readonly')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    amount_to_balance = models.FloatField(blank=True, null=True, db_comment='Amount to balance')

    class Meta:
        managed = False
        db_table = 'pos_close_session_wizard'
        db_table_comment = 'Close Session Wizard'


class PosConfig(models.Model):
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, db_comment='Operation Type')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Point of Sale Journal')
    invoice_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, related_name='posconfig_invoice_journal_set', blank=True, null=True, db_comment='Invoice Journal')
    sequence = models.ForeignKey(IrSequence, models.DO_NOTHING, blank=True, null=True, db_comment='Order IDs Sequence')
    sequence_line = models.ForeignKey(IrSequence, models.DO_NOTHING, related_name='posconfig_sequence_line_set', blank=True, null=True, db_comment='Order Line IDs Sequence')
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING, blank=True, null=True, db_comment='Default Pricelist')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    group_pos_manager = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True, db_comment='Point of Sale Manager Group')
    group_pos_user = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name='posconfig_group_pos_user_set', blank=True, null=True, db_comment='Point of Sale User Group')
    tip_product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True, db_comment='Tip Product')
    default_fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True, db_comment='Default Fiscal Position')
    rounding_method = models.ForeignKey(AccountCashRounding, models.DO_NOTHING, db_column='rounding_method', blank=True, null=True, db_comment='Cash rounding')
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True, db_comment='Warehouse')
    route = models.ForeignKey('StockRoute', models.DO_NOTHING, blank=True, null=True, db_comment='Spefic route for products delivered later.')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='posconfig_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    access_token = models.CharField(blank=True, null=True, db_comment='Access Token')
    name = models.CharField(db_comment='Point of Sale')
    iface_tax_included = models.CharField(db_comment='Tax Display')
    customer_display_type = models.CharField(blank=True, null=True, db_comment='Customer Facing Display')
    customer_display_bg_img_name = models.CharField(blank=True, null=True, db_comment='Background Image Name')
    proxy_ip = models.CharField(max_length=45, blank=True, null=True, db_comment='IP Address')
    uuid = models.CharField(blank=True, null=True, db_comment='Uuid')
    picking_policy = models.CharField(db_comment='Shipping Policy')
    receipt_header = models.TextField(blank=True, null=True, db_comment='Receipt Header')
    receipt_footer = models.TextField(blank=True, null=True, db_comment='Receipt Footer')
    is_order_printer = models.BooleanField(blank=True, null=True, db_comment='Order Printer')
    iface_cashdrawer = models.BooleanField(blank=True, null=True, db_comment='Cashdrawer')
    iface_electronic_scale = models.BooleanField(blank=True, null=True, db_comment='Electronic Scale')
    iface_print_via_proxy = models.BooleanField(blank=True, null=True, db_comment='Print via Proxy')
    iface_scan_via_proxy = models.BooleanField(blank=True, null=True, db_comment='Scan via Proxy')
    iface_big_scrollbars = models.BooleanField(blank=True, null=True, db_comment='Large Scrollbars')
    iface_print_auto = models.BooleanField(blank=True, null=True, db_comment='Automatic Receipt Printing')
    iface_print_skip_screen = models.BooleanField(blank=True, null=True, db_comment='Skip Preview Screen')
    restrict_price_control = models.BooleanField(blank=True, null=True, db_comment='Restrict Price Modifications to Managers')
    is_margins_costs_accessible_to_every_user = models.BooleanField(blank=True, null=True, db_comment='Margins & Costs')
    set_maximum_difference = models.BooleanField(blank=True, null=True, db_comment='Set Maximum Difference')
    basic_receipt = models.BooleanField(blank=True, null=True, db_comment='Basic Receipt')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    iface_tipproduct = models.BooleanField(blank=True, null=True, db_comment='Product tips')
    use_pricelist = models.BooleanField(blank=True, null=True, db_comment='Use a pricelist.')
    tax_regime_selection = models.BooleanField(blank=True, null=True, db_comment='Tax Regime Selection value')
    limit_categories = models.BooleanField(blank=True, null=True, db_comment='Restrict Categories')
    module_pos_restaurant = models.BooleanField(blank=True, null=True, db_comment='Is a Bar/Restaurant')
    module_pos_avatax = models.BooleanField(blank=True, null=True, db_comment='AvaTax PoS Integration')
    module_pos_discount = models.BooleanField(blank=True, null=True, db_comment='Global Discounts')
    is_posbox = models.BooleanField(blank=True, null=True, db_comment='PosBox')
    is_header_or_footer = models.BooleanField(blank=True, null=True, db_comment='Custom Header & Footer')
    module_pos_hr = models.BooleanField(blank=True, null=True, db_comment='Module Pos Hr')
    other_devices = models.BooleanField(blank=True, null=True, db_comment='Other Devices')
    cash_rounding = models.BooleanField(blank=True, null=True, db_comment='Cash Rounding')
    only_round_cash_method = models.BooleanField(blank=True, null=True, db_comment='Only apply rounding on cash')
    manual_discount = models.BooleanField(blank=True, null=True, db_comment='Line Discounts')
    ship_later = models.BooleanField(blank=True, null=True, db_comment='Ship Later')
    auto_validate_terminal_payment = models.BooleanField(blank=True, null=True, db_comment='Auto Validate Terminal Payment')
    show_product_images = models.BooleanField(blank=True, null=True, db_comment='Show Product Images')
    show_category_images = models.BooleanField(blank=True, null=True, db_comment='Show Category Images')
    module_pos_sms = models.BooleanField(blank=True, null=True, db_comment='SMS Enabled')
    is_closing_entry_by_product = models.BooleanField(blank=True, null=True, db_comment='Closing Entry by product')
    order_edit_tracking = models.BooleanField(blank=True, null=True, db_comment='Track orders edits')
    orderlines_sequence_in_cart_by_category = models.BooleanField(blank=True, null=True, db_comment="Order cart by category's sequence")
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    amount_authorized_diff = models.FloatField(blank=True, null=True, db_comment='Amount Authorized Difference')
    epson_printer_ip = models.CharField(blank=True, null=True, db_comment='Epson Printer IP')
    sms_receipt_template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='Sms Receipt template')
    crm_team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True, db_comment='Sales Team')
    down_payment_product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name='posconfig_down_payment_product_set', blank=True, null=True, db_comment='Down Payment Product')

    class Meta:
        managed = False
        db_table = 'pos_config'
        db_table_comment = 'Point of Sale Configuration'


class PosConfigPosNoteRel(models.Model):
    pk = models.CompositePrimaryKey('pos_config_id', 'pos_note_id')
    pos_config = models.ForeignKey(PosConfig, models.DO_NOTHING)
    pos_note = models.ForeignKey('PosNote', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_config_pos_note_rel'
        db_table_comment = 'RELATION BETWEEN pos_config AND pos_note'


class PosConfigPosPaymentMethodRel(models.Model):
    pk = models.CompositePrimaryKey('pos_config_id', 'pos_payment_method_id')
    pos_config = models.ForeignKey(PosConfig, models.DO_NOTHING)
    pos_payment_method = models.ForeignKey('PosPaymentMethod', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_config_pos_payment_method_rel'
        db_table_comment = 'RELATION BETWEEN pos_config AND pos_payment_method'


class PosConfigPrinterRel(models.Model):
    pk = models.CompositePrimaryKey('config_id', 'printer_id')
    config = models.ForeignKey(PosConfig, models.DO_NOTHING)
    printer = models.ForeignKey('PosPrinter', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_config_printer_rel'
        db_table_comment = 'RELATION BETWEEN pos_config AND pos_printer'


class PosConfigProductPricelistRel(models.Model):
    pk = models.CompositePrimaryKey('pos_config_id', 'product_pricelist_id')
    pos_config = models.ForeignKey(PosConfig, models.DO_NOTHING)
    product_pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_config_product_pricelist_rel'
        db_table_comment = 'RELATION BETWEEN pos_config AND product_pricelist'


class PosConfigTrustRelation(models.Model):
    pk = models.CompositePrimaryKey('is_trusting', 'is_trusted')
    is_trusting = models.ForeignKey(PosConfig, models.DO_NOTHING, db_column='is_trusting')
    is_trusted = models.ForeignKey(PosConfig, models.DO_NOTHING, db_column='is_trusted', related_name='posconfigtrustrelation_is_trusted_set')

    class Meta:
        managed = False
        db_table = 'pos_config_trust_relation'
        db_table_comment = 'RELATION BETWEEN pos_config AND pos_config'


class PosDailySalesReportsWizard(models.Model):
    pos_session = models.ForeignKey('PosSession', models.DO_NOTHING, db_comment='Pos Session')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='posdailysalesreportswizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    add_report_per_employee = models.BooleanField(blank=True, null=True, db_comment='Add a report per each employee')

    class Meta:
        managed = False
        db_table = 'pos_daily_sales_reports_wizard'
        db_table_comment = 'Point of Sale Daily Report'


class PosDetailConfigs(models.Model):
    pk = models.CompositePrimaryKey('pos_details_wizard_id', 'pos_config_id')
    pos_details_wizard = models.ForeignKey('PosDetailsWizard', models.DO_NOTHING)
    pos_config = models.ForeignKey(PosConfig, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_detail_configs'
        db_table_comment = 'RELATION BETWEEN pos_details_wizard AND pos_config'


class PosDetailsWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='posdetailswizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    start_date = models.DateTimeField(db_comment='Start Date')
    end_date = models.DateTimeField(db_comment='End Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'pos_details_wizard'
        db_table_comment = 'Point of Sale Details Report'


class PosHrAdvancedEmployeeHrEmployee(models.Model):
    pk = models.CompositePrimaryKey('pos_config_id', 'hr_employee_id')
    pos_config = models.ForeignKey(PosConfig, models.DO_NOTHING)
    hr_employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_hr_advanced_employee_hr_employee'
        db_table_comment = 'RELATION BETWEEN pos_config AND hr_employee'


class PosHrBasicEmployeeHrEmployee(models.Model):
    pk = models.CompositePrimaryKey('pos_config_id', 'hr_employee_id')
    pos_config = models.ForeignKey(PosConfig, models.DO_NOTHING)
    hr_employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_hr_basic_employee_hr_employee'
        db_table_comment = 'RELATION BETWEEN pos_config AND hr_employee'


class PosMakePayment(models.Model):
    config = models.ForeignKey(PosConfig, models.DO_NOTHING, db_comment='Point of Sale Configuration')
    payment_method = models.ForeignKey('PosPaymentMethod', models.DO_NOTHING, db_comment='Payment Method')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='posmakepayment_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    payment_name = models.CharField(blank=True, null=True, db_comment='Payment Reference')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Amount')
    payment_date = models.DateTimeField(db_comment='Payment Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'pos_make_payment'
        db_table_comment = 'Point of Sale Make Payment Wizard'


class PosNote(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='posnote_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(unique=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'pos_note'
        db_table_comment = 'PoS Note'


class PosOrder(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Employee')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING, blank=True, null=True, db_comment='Pricelist')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Customer')
    sequence_number = models.IntegerField(blank=True, null=True, db_comment='Sequence Number')
    session = models.ForeignKey('PosSession', models.DO_NOTHING, db_comment='Session')
    config = models.ForeignKey(PosConfig, models.DO_NOTHING, blank=True, null=True, db_comment='Point of Sale')
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING, db_column='account_move', blank=True, null=True, db_comment='Invoice')
    procurement_group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, blank=True, null=True, db_comment='Procurement Group')
    nb_print = models.IntegerField(blank=True, null=True, db_comment='Number of Print')
    sale_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, db_column='sale_journal', blank=True, null=True, db_comment='Sales Journal')
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True, db_comment='Fiscal Position')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='posorder_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='posorder_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    access_token = models.CharField(blank=True, null=True, db_comment='Security Token')
    name = models.CharField(db_comment='Order Ref')
    last_order_preparation_change = models.CharField(blank=True, null=True, db_comment='Last preparation change')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    floating_order_name = models.CharField(blank=True, null=True, db_comment='Order Name')
    pos_reference = models.CharField(blank=True, null=True, db_comment='Receipt Number')
    ticket_code = models.CharField(blank=True, null=True, db_comment='Ticket Code')
    uuid = models.CharField(blank=True, null=True, db_comment='Uuid')
    email = models.CharField(blank=True, null=True, db_comment='Email')
    mobile = models.CharField(blank=True, null=True, db_comment='Mobile')
    shipping_date = models.DateField(blank=True, null=True, db_comment='Shipping Date')
    general_note = models.TextField(blank=True, null=True, db_comment='General Note')
    amount_difference = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Difference')
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Taxes')
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Total')
    amount_paid = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Paid')
    amount_return = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Returned')
    currency_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Currency Rate')
    tip_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Tip Amount')
    to_invoice = models.BooleanField(blank=True, null=True, db_comment='To invoice')
    is_tipped = models.BooleanField(blank=True, null=True, db_comment='Is this already tipped?')
    has_deleted_line = models.BooleanField(blank=True, null=True, db_comment='Has Deleted Line')
    date_order = models.DateTimeField(blank=True, null=True, db_comment='Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    next_online_payment_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Next online payment amount to pay')
    crm_team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True, db_comment='Sales Team')
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True, db_comment='Cashier')
    cashier = models.CharField(blank=True, null=True, db_comment='Cashier name')

    class Meta:
        managed = False
        db_table = 'pos_order'
        db_table_comment = 'Point of Sale Orders'


class PosOrderLine(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Product')
    order = models.ForeignKey(PosOrder, models.DO_NOTHING, db_comment='Order Ref')
    refunded_orderline = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Refunded Order Line')
    combo_parent = models.ForeignKey('self', models.DO_NOTHING, related_name='posorderline_combo_parent_set', blank=True, null=True, db_comment='Combo Parent')
    combo_item = models.ForeignKey('ProductComboItem', models.DO_NOTHING, blank=True, null=True, db_comment='Combo Item')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='posorderline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Line No')
    notice = models.CharField(blank=True, null=True, db_comment='Discount Notice')
    price_type = models.CharField(blank=True, null=True, db_comment='Price Type')
    full_product_name = models.CharField(blank=True, null=True, db_comment='Full Product Name')
    customer_note = models.CharField(blank=True, null=True, db_comment='Customer Note')
    uuid = models.CharField(blank=True, null=True, db_comment='Uuid')
    note = models.CharField(blank=True, null=True, db_comment='Product Note')
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Unit Price')
    qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Quantity')
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Tax Excl.')
    price_subtotal_incl = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Tax Incl.')
    total_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total cost')
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Discount (%)')
    skip_change = models.BooleanField(blank=True, null=True, db_comment='Skip line when sending ticket to kitchen printers.')
    is_total_cost_computed = models.BooleanField(blank=True, null=True, db_comment='Is Total Cost Computed')
    is_edited = models.BooleanField(blank=True, null=True, db_comment='Edited')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    price_extra = models.FloatField(blank=True, null=True, db_comment='Price extra')
    l10n_in_hsn_code = models.CharField(blank=True, null=True, db_comment='HSN/SAC Code')
    sale_order_origin = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True, db_comment='Linked Sale Order')
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True, db_comment='Source Sale Order Line')
    down_payment_details = models.TextField(blank=True, null=True, db_comment='Down Payment Details')
    qty_delivered = models.FloatField(blank=True, null=True, db_comment='Delivery Quantity')
    event_ticket = models.ForeignKey(EventEventTicket, models.DO_NOTHING, blank=True, null=True, db_comment='Event Ticket')

    class Meta:
        managed = False
        db_table = 'pos_order_line'
        db_table_comment = 'Point of Sale Order Lines'


class PosOrderLineProductTemplateAttributeValueRel(models.Model):
    pk = models.CompositePrimaryKey('pos_order_line_id', 'product_template_attribute_value_id')
    pos_order_line = models.ForeignKey(PosOrderLine, models.DO_NOTHING)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_order_line_product_template_attribute_value_rel'
        db_table_comment = 'RELATION BETWEEN pos_order_line AND product_template_attribute_value'


class PosPackOperationLot(models.Model):
    pos_order_line = models.ForeignKey(PosOrderLine, models.DO_NOTHING, blank=True, null=True, db_comment='Pos Order Line')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='pospackoperationlot_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    lot_name = models.CharField(blank=True, null=True, db_comment='Lot Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'pos_pack_operation_lot'
        db_table_comment = 'Specify product lot/serial number in pos order line'


class PosPayment(models.Model):
    pos_order = models.ForeignKey(PosOrder, models.DO_NOTHING, db_comment='Order')
    payment_method = models.ForeignKey('PosPaymentMethod', models.DO_NOTHING, db_comment='Payment Method')
    session = models.ForeignKey('PosSession', models.DO_NOTHING, blank=True, null=True, db_comment='Session')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True, db_comment='Account Move')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='pospayment_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Label')
    card_type = models.CharField(blank=True, null=True, db_comment='Type of card used')
    card_brand = models.CharField(blank=True, null=True, db_comment='Brand of card')
    card_no = models.CharField(blank=True, null=True, db_comment='Card Number(Last 4 Digit)')
    cardholder_name = models.CharField(blank=True, null=True, db_comment='Card Owner name')
    payment_ref_no = models.CharField(blank=True, null=True, db_comment='Payment reference number')
    payment_method_authcode = models.CharField(blank=True, null=True, db_comment='Payment APPR Code')
    payment_method_issuer_bank = models.CharField(blank=True, null=True, db_comment='Payment Issuer Bank')
    payment_method_payment_mode = models.CharField(blank=True, null=True, db_comment='Payment Mode')
    transaction_id = models.CharField(blank=True, null=True, db_comment='Payment Transaction ID')
    payment_status = models.CharField(blank=True, null=True, db_comment='Payment Status')
    ticket = models.CharField(blank=True, null=True, db_comment='Payment Receipt Info')
    uuid = models.CharField(blank=True, null=True, db_comment='Uuid')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Amount')
    is_change = models.BooleanField(blank=True, null=True, db_comment='Is this payment change?')
    payment_date = models.DateTimeField(db_comment='Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    online_account_payment = models.ForeignKey(AccountPayment, models.DO_NOTHING, blank=True, null=True, db_comment='Online accounting payment')
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True, db_comment='Cashier')

    class Meta:
        managed = False
        db_table = 'pos_payment'
        db_table_comment = 'Point of Sale Payments'


class PosPaymentMethod(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    outstanding_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Outstanding Account')
    receivable_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='pospaymentmethod_receivable_account_set', blank=True, null=True, db_comment='Intermediary Account')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Journal')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='pospaymentmethod_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    use_payment_terminal = models.CharField(blank=True, null=True, db_comment='Use a Payment Terminal')
    payment_method_type = models.CharField(db_comment='Integration')
    qr_code_method = models.CharField(blank=True, null=True, db_comment='QR Code Format')
    name = models.JSONField(db_comment='Method')
    is_cash_count = models.BooleanField(blank=True, null=True, db_comment='Cash')
    split_transactions = models.BooleanField(blank=True, null=True, db_comment='Identify Customer')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    is_online_payment = models.BooleanField(blank=True, null=True, db_comment='Online Payment')

    class Meta:
        managed = False
        db_table = 'pos_payment_method'
        db_table_comment = 'Point of Sale Payment Methods'


class PosPrinter(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='posprinter_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Printer Name')
    printer_type = models.CharField(blank=True, null=True, db_comment='Printer Type')
    proxy_ip = models.CharField(blank=True, null=True, db_comment='Proxy IP Address')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    epson_printer_ip = models.CharField(blank=True, null=True, db_comment='Epson Printer IP Address')

    class Meta:
        managed = False
        db_table = 'pos_printer'
        db_table_comment = 'Point of Sale Printer'


class PosSession(models.Model):
    config = models.ForeignKey(PosConfig, models.DO_NOTHING, db_comment='Point of Sale')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, db_comment='Opened By')
    sequence_number = models.IntegerField(blank=True, null=True, db_comment='Order Sequence Number')
    login_number = models.IntegerField(blank=True, null=True, db_comment='Login Sequence Number')
    cash_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Cash Journal')
    move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True, db_comment='Journal Entry')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='possession_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='possession_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    access_token = models.CharField(blank=True, null=True, db_comment='Security Token')
    name = models.CharField(unique=True, db_comment='Session ID')
    state = models.CharField(db_comment='Status')
    opening_notes = models.TextField(blank=True, null=True, db_comment='Opening Notes')
    closing_notes = models.TextField(blank=True, null=True, db_comment='Closing Notes')
    cash_register_balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Ending Balance')
    cash_register_balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Starting Balance')
    cash_real_transaction = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Transaction')
    rescue = models.BooleanField(blank=True, null=True, db_comment='Recovery Session')
    update_stock_at_closing = models.BooleanField(blank=True, null=True, db_comment='Stock should be updated at closing')
    start_at = models.DateTimeField(blank=True, null=True, db_comment='Opening Date')
    stop_at = models.DateTimeField(blank=True, null=True, db_comment='Closing Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True, db_comment='Cashier')

    class Meta:
        managed = False
        db_table = 'pos_session'
        db_table_comment = 'Point of Sale Session'


class PrintPrenumberedChecks(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='printprenumberedchecks_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    next_check_number = models.CharField(db_comment='Next Check Number')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'print_prenumbered_checks'
        db_table_comment = 'Print Pre-numbered Checks'


class PrinterCategoryRel(models.Model):
    pk = models.CompositePrimaryKey('printer_id', 'category_id')
    printer = models.ForeignKey(PosPrinter, models.DO_NOTHING)
    category = models.ForeignKey(PosCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'printer_category_rel'
        db_table_comment = 'RELATION BETWEEN pos_printer AND pos_category'


class PrivacyLog(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, db_comment='Handled By')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='privacylog_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='privacylog_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    anonymized_name = models.CharField(db_comment='Anonymized Name')
    anonymized_email = models.CharField(db_comment='Anonymized Email')
    execution_details = models.TextField(blank=True, null=True, db_comment='Execution Details')
    records_description = models.TextField(blank=True, null=True, db_comment='Found Records')
    additional_note = models.TextField(blank=True, null=True, db_comment='Additional Note')
    date = models.DateTimeField(db_comment='Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'privacy_log'
        db_table_comment = 'Privacy Log'


class PrivacyLookupWizard(models.Model):
    log = models.ForeignKey(PrivacyLog, models.DO_NOTHING, blank=True, null=True, db_comment='Log')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='privacylookupwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    email = models.CharField(db_comment='Email')
    execution_details = models.TextField(blank=True, null=True, db_comment='Execution Details')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'privacy_lookup_wizard'
        db_table_comment = 'Privacy Lookup Wizard'


class PrivacyLookupWizardLine(models.Model):
    wizard = models.ForeignKey(PrivacyLookupWizard, models.DO_NOTHING, blank=True, null=True, db_comment='Wizard')
    res_id = models.IntegerField(db_comment='Resource ID')
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True, db_comment='Related Document Model')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='privacylookupwizardline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    res_name = models.CharField(blank=True, null=True, db_comment='Resource name')
    res_model_0 = models.CharField(db_column='res_model', blank=True, null=True, db_comment='Document Model')  # Field renamed because of name conflict.
    execution_details = models.CharField(blank=True, null=True, db_comment='Execution Details')
    has_active = models.BooleanField(blank=True, null=True, db_comment='Has Active')
    is_active = models.BooleanField(blank=True, null=True, db_comment='Is Active')
    is_unlinked = models.BooleanField(blank=True, null=True, db_comment='Is Unlinked')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'privacy_lookup_wizard_line'
        db_table_comment = 'Privacy Lookup Wizard Line'


class ProcurementGroup(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='procurementgroup_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Reference')
    move_type = models.CharField(blank=True, null=True, db_comment='Delivery Type')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    sale = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True, db_comment='Sale Order')
    pos_order = models.ForeignKey(PosOrder, models.DO_NOTHING, blank=True, null=True, db_comment='POS Order')

    class Meta:
        managed = False
        db_table = 'procurement_group'
        db_table_comment = 'Procurement Group'


class ProductAccessoryRel(models.Model):
    pk = models.CompositePrimaryKey('src_id', 'dest_id')
    src = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    dest = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_accessory_rel'
        db_table_comment = 'RELATION BETWEEN product_template AND product_product'


class ProductAlternativeRel(models.Model):
    pk = models.CompositePrimaryKey('src_id', 'dest_id')
    src = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    dest = models.ForeignKey('ProductTemplate', models.DO_NOTHING, related_name='productalternativerel_dest_set')

    class Meta:
        managed = False
        db_table = 'product_alternative_rel'
        db_table_comment = 'RELATION BETWEEN product_template AND product_template'


class ProductAttrExclusionValueIdsRel(models.Model):
    pk = models.CompositePrimaryKey('product_template_attribute_exclusion_id', 'product_template_attribute_value_id')
    product_template_attribute_exclusion = models.ForeignKey('ProductTemplateAttributeExclusion', models.DO_NOTHING)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attr_exclusion_value_ids_rel'
        db_table_comment = 'RELATION BETWEEN product_template_attribute_exclusion AND product_template_attribute_value'


class ProductAttribute(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productattribute_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_variant = models.CharField(db_comment='Variant Creation')
    display_type = models.CharField(db_comment='Display Type')
    name = models.JSONField(db_comment='Attribute')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    visibility = models.CharField(blank=True, null=True, db_comment='Visibility')

    class Meta:
        managed = False
        db_table = 'product_attribute'
        db_table_comment = 'Product Attribute'


class ProductAttributeCustomValue(models.Model):
    custom_product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING, db_comment='Attribute Value')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productattributecustomvalue_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    custom_value = models.CharField(blank=True, null=True, db_comment='Custom Value')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True, db_comment='Sales Order Line')
    pos_order_line = models.ForeignKey(PosOrderLine, models.DO_NOTHING, blank=True, null=True, db_comment='PoS Order Line')

    class Meta:
        managed = False
        db_table = 'product_attribute_custom_value'
        unique_together = (('custom_product_template_attribute_value', 'sale_order_line'),)
        db_table_comment = 'Product Attribute Custom Value'


class ProductAttributeProductTemplateRel(models.Model):
    pk = models.CompositePrimaryKey('product_attribute_id', 'product_template_id')
    product_attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING)
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_product_template_rel'
        db_table_comment = 'RELATION BETWEEN product_attribute AND product_template'


class ProductAttributeValue(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING, db_comment='Attribute')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productattributevalue_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    html_color = models.CharField(blank=True, null=True, db_comment='Color')
    name = models.JSONField(db_comment='Value')
    is_custom = models.BooleanField(blank=True, null=True, db_comment='Free text')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    default_extra_price = models.FloatField(blank=True, null=True, db_comment='Default Extra Price')

    class Meta:
        managed = False
        db_table = 'product_attribute_value'
        db_table_comment = 'Attribute Value'


class ProductAttributeValueProductTemplateAttributeLineRel(models.Model):
    pk = models.CompositePrimaryKey('product_attribute_value_id', 'product_template_attribute_line_id')
    product_attribute_value = models.ForeignKey(ProductAttributeValue, models.DO_NOTHING)
    product_template_attribute_line = models.ForeignKey('ProductTemplateAttributeLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_value_product_template_attribute_line_rel'
        db_table_comment = 'RELATION BETWEEN product_attribute_value AND product_template_attribute_line'


class ProductCategory(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Category')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productcategory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    complete_name = models.CharField(blank=True, null=True, db_comment='Complete Name')
    parent_path = models.CharField(blank=True, null=True, db_comment='Parent Path')
    product_properties_definition = models.JSONField(blank=True, null=True, db_comment='Product Properties')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    property_account_income_categ_id = models.JSONField(blank=True, null=True, db_comment='Income Account')
    property_account_expense_categ_id = models.JSONField(blank=True, null=True, db_comment='Expense Account')
    property_account_downpayment_categ_id = models.JSONField(blank=True, null=True, db_comment='Downpayment Account')
    removal_strategy = models.ForeignKey('ProductRemoval', models.DO_NOTHING, blank=True, null=True, db_comment='Force Removal Strategy')
    packaging_reserve_method = models.CharField(blank=True, null=True, db_comment='Reserve Packagings')
    property_valuation = models.JSONField(blank=True, null=True, db_comment='Inventory Valuation')
    property_cost_method = models.JSONField(blank=True, null=True, db_comment='Costing Method')
    property_stock_journal = models.JSONField(blank=True, null=True, db_comment='Stock Journal')
    property_stock_account_input_categ_id = models.JSONField(blank=True, null=True, db_comment='Stock Input Account')
    property_stock_account_output_categ_id = models.JSONField(blank=True, null=True, db_comment='Stock Output Account')
    property_stock_valuation_account_id = models.JSONField(blank=True, null=True, db_comment='Stock Valuation Account')
    property_account_creditor_price_difference_categ = models.JSONField(blank=True, null=True, db_comment='Price Difference Account')
    property_stock_account_production_cost_id = models.JSONField(blank=True, null=True, db_comment='Production Account')

    class Meta:
        managed = False
        db_table = 'product_category'
        db_table_comment = 'Product Category'


class ProductCombo(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productcombo_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'product_combo'
        db_table_comment = 'Product Combo'


class ProductComboItem(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    combo = models.ForeignKey(ProductCombo, models.DO_NOTHING, db_comment='Combo')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Product')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productcomboitem_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    extra_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Extra Price')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'product_combo_item'
        db_table_comment = 'Product Combo Item'


class ProductComboProductTemplateRel(models.Model):
    pk = models.CompositePrimaryKey('product_template_id', 'product_combo_id')
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    product_combo = models.ForeignKey(ProductCombo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_combo_product_template_rel'
        db_table_comment = 'RELATION BETWEEN product_template AND product_combo'


class ProductDocument(models.Model):
    ir_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, db_comment='Related attachment')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productdocument_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    attached_on_sale = models.CharField(db_comment='Sale : Visible at')
    shown_on_product_page = models.BooleanField(blank=True, null=True, db_comment='Publish on website')
    attached_on_mrp = models.CharField(db_comment='MRP : Visible at')

    class Meta:
        managed = False
        db_table = 'product_document'
        db_table_comment = 'Product Document'


class ProductDocumentSalePdfFormFieldRel(models.Model):
    pk = models.CompositePrimaryKey('product_document_id', 'sale_pdf_form_field_id')
    product_document = models.ForeignKey(ProductDocument, models.DO_NOTHING)
    sale_pdf_form_field = models.ForeignKey('SalePdfFormField', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_document_sale_pdf_form_field_rel'
        db_table_comment = 'RELATION BETWEEN product_document AND sale_pdf_form_field'


class ProductImage(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='Product Template')
    product_variant = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True, db_comment='Product Variant')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productimage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    video_url = models.CharField(blank=True, null=True, db_comment='Video URL')
    can_image_1024_be_zoomed = models.BooleanField(blank=True, null=True, db_comment='Can Image 1024 be zoomed')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'product_image'
        db_table_comment = 'Product Image'


class ProductLabelLayout(models.Model):
    custom_quantity = models.IntegerField(db_comment='Quantity')
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING, blank=True, null=True, db_comment='Pricelist')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productlabellayout_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    print_format = models.CharField(db_comment='Format')
    extra_html = models.TextField(blank=True, null=True, db_comment='Extra Content')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    move_quantity = models.CharField(db_comment='Quantity to print')

    class Meta:
        managed = False
        db_table = 'product_label_layout'
        db_table_comment = 'Choose the sheet layout to print the labels'


class ProductLabelLayoutProductProductRel(models.Model):
    pk = models.CompositePrimaryKey('product_label_layout_id', 'product_product_id')
    product_label_layout = models.ForeignKey(ProductLabelLayout, models.DO_NOTHING)
    product_product = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_label_layout_product_product_rel'
        db_table_comment = 'RELATION BETWEEN product_label_layout AND product_product'


class ProductLabelLayoutProductTemplateRel(models.Model):
    pk = models.CompositePrimaryKey('product_label_layout_id', 'product_template_id')
    product_label_layout = models.ForeignKey(ProductLabelLayout, models.DO_NOTHING)
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_label_layout_product_template_rel'
        db_table_comment = 'RELATION BETWEEN product_label_layout AND product_template'


class ProductLabelLayoutStockMoveRel(models.Model):
    pk = models.CompositePrimaryKey('product_label_layout_id', 'stock_move_id')
    product_label_layout = models.ForeignKey(ProductLabelLayout, models.DO_NOTHING)
    stock_move = models.ForeignKey('StockMove', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_label_layout_stock_move_rel'
        db_table_comment = 'RELATION BETWEEN product_label_layout AND stock_move'


class ProductOptionalRel(models.Model):
    pk = models.CompositePrimaryKey('src_id', 'dest_id')
    src = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    dest = models.ForeignKey('ProductTemplate', models.DO_NOTHING, related_name='productoptionalrel_dest_set')

    class Meta:
        managed = False
        db_table = 'product_optional_rel'
        db_table_comment = 'RELATION BETWEEN product_template AND product_template'


class ProductPackaging(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, db_comment='Product')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productpackaging_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Product Packaging')
    barcode = models.CharField(unique=True, blank=True, null=True, db_comment='Barcode')
    qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Contained Quantity')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    sales = models.BooleanField(blank=True, null=True, db_comment='Sales')
    package_type = models.ForeignKey('StockPackageType', models.DO_NOTHING, blank=True, null=True, db_comment='Package Type')
    purchase = models.BooleanField(blank=True, null=True, db_comment='Purchase')

    class Meta:
        managed = False
        db_table = 'product_packaging'
        db_table_comment = 'Product Packaging'


class ProductPricelist(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, db_comment='Currency')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productpricelist_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Pricelist Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    code = models.CharField(blank=True, null=True, db_comment='E-commerce Promotional Code')
    selectable = models.BooleanField(blank=True, null=True, db_comment='Selectable')

    class Meta:
        managed = False
        db_table = 'product_pricelist'
        db_table_comment = 'Pricelist'


class ProductPricelistItem(models.Model):
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING, db_comment='Pricelist')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True, db_comment='Category')
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True, db_comment='Variant')
    base_pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING, related_name='productpricelistitem_base_pricelist_set', blank=True, null=True, db_comment='Other Pricelist')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productpricelistitem_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    applied_on = models.CharField(db_comment='Apply On')
    display_applied_on = models.CharField(db_comment='Display Applied On')
    base = models.CharField(db_comment='Based on')
    compute_price = models.CharField(db_comment='Compute Price')
    min_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Min. Quantity')
    fixed_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Fixed Price')
    price_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Price Discount')
    price_round = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Price Rounding')
    price_surcharge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Extra Fee')
    price_markup = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Markup')
    price_min_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Min. Price Margin')
    price_max_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Max. Price Margin')
    date_start = models.DateTimeField(blank=True, null=True, db_comment='Start Date')
    date_end = models.DateTimeField(blank=True, null=True, db_comment='End Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    percent_price = models.FloatField(blank=True, null=True, db_comment='Percentage Price')

    class Meta:
        managed = False
        db_table = 'product_pricelist_item'
        db_table_comment = 'Pricelist Rule'


class ProductPricelistResConfigSettingsRel(models.Model):
    pk = models.CompositePrimaryKey('res_config_settings_id', 'product_pricelist_id')
    res_config_settings = models.ForeignKey('ResConfigSettings', models.DO_NOTHING)
    product_pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_pricelist_res_config_settings_rel'
        db_table_comment = 'RELATION BETWEEN res_config_settings AND product_pricelist'


class ProductProduct(models.Model):
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, db_comment='Product Template')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productproduct_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    default_code = models.CharField(blank=True, null=True, db_comment='Internal Reference')
    barcode = models.CharField(blank=True, null=True, db_comment='Barcode')
    combination_indices = models.CharField(blank=True, null=True, db_comment='Combination Indices')
    standard_price = models.JSONField(blank=True, null=True, db_comment='Cost')
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Volume')
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Weight')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    can_image_variant_1024_be_zoomed = models.BooleanField(blank=True, null=True, db_comment='Can Variant Image 1024 be zoomed')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Write Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    variant_ribbon = models.ForeignKey('ProductRibbon', models.DO_NOTHING, blank=True, null=True, db_comment='Variant Ribbon')
    base_unit = models.ForeignKey('WebsiteBaseUnit', models.DO_NOTHING, blank=True, null=True, db_comment='Custom Unit of Measure')
    base_unit_count = models.FloatField(db_comment='Base Unit Count')
    lot_properties_definition = models.JSONField(blank=True, null=True, db_comment='Lot Properties')

    class Meta:
        managed = False
        db_table = 'product_product'
        unique_together = (('product_tmpl', 'combination_indices'),)
        db_table_comment = 'Product Variant'


class ProductProductStockTrackConfirmationRel(models.Model):
    pk = models.CompositePrimaryKey('stock_track_confirmation_id', 'product_product_id')
    stock_track_confirmation = models.ForeignKey('StockTrackConfirmation', models.DO_NOTHING)
    product_product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_product_stock_track_confirmation_rel'
        db_table_comment = 'RELATION BETWEEN stock_track_confirmation AND product_product'


class ProductPublicCategory(models.Model):
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Category')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productpubliccategory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    website_meta_og_img = models.CharField(blank=True, null=True, db_comment='Website opengraph image')
    parent_path = models.CharField(blank=True, null=True, db_comment='Parent Path')
    website_meta_title = models.JSONField(blank=True, null=True, db_comment='Website meta title')
    website_meta_description = models.JSONField(blank=True, null=True, db_comment='Website meta description')
    website_meta_keywords = models.JSONField(blank=True, null=True, db_comment='Website meta keywords')
    seo_name = models.JSONField(blank=True, null=True, db_comment='Seo name')
    name = models.JSONField(db_comment='Name')
    website_description = models.JSONField(blank=True, null=True, db_comment='Category Description')
    website_footer = models.JSONField(blank=True, null=True, db_comment='Category Footer')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'product_public_category'
        db_table_comment = 'Website Product Category'


class ProductPublicCategoryProductTemplateRel(models.Model):
    pk = models.CompositePrimaryKey('product_public_category_id', 'product_template_id')
    product_public_category = models.ForeignKey(ProductPublicCategory, models.DO_NOTHING)
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_public_category_product_template_rel'
        db_table_comment = 'RELATION BETWEEN product_public_category AND product_template'


class ProductRemoval(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productremoval_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    method = models.JSONField(db_comment='Method')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'product_removal'
        db_table_comment = 'Removal Strategy'


class ProductReplenish(models.Model):
    route = models.ForeignKey('StockRoute', models.DO_NOTHING, blank=True, null=True, db_comment='Preferred Route')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, db_comment='Product Template')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Unity of measure')
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, db_comment='Warehouse')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productreplenish_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    product_has_variants = models.BooleanField(db_comment='Has variants')
    date_planned = models.DateTimeField(db_comment='Scheduled Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    quantity = models.FloatField(db_comment='Quantity')
    supplier = models.ForeignKey('ProductSupplierinfo', models.DO_NOTHING, blank=True, null=True, db_comment='Vendor')
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, blank=True, null=True, db_comment='Bill of Material')

    class Meta:
        managed = False
        db_table = 'product_replenish'
        db_table_comment = 'Product Replenish'


class ProductRibbon(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productribbon_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    bg_color = models.CharField(db_comment='Background Color')
    text_color = models.CharField(db_comment='Text Color')
    position = models.CharField(db_comment='Position')
    name = models.JSONField(db_comment='Ribbon Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'product_ribbon'
        db_table_comment = 'Product ribbon'


class ProductSupplierTaxesRel(models.Model):
    pk = models.CompositePrimaryKey('prod_id', 'tax_id')
    prod = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_supplier_taxes_rel'
        db_table_comment = 'RELATION BETWEEN product_template AND account_tax'


class ProductSupplierinfo(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Vendor')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, db_comment='Currency')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Product Variant')
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='Product Template')
    delay = models.IntegerField(db_comment='Delivery Lead Time')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='productsupplierinfo_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    product_name = models.CharField(blank=True, null=True, db_comment='Vendor Product Name')
    product_code = models.CharField(blank=True, null=True, db_comment='Vendor Product Code')
    date_start = models.DateField(blank=True, null=True, db_comment='Start Date')
    date_end = models.DateField(blank=True, null=True, db_comment='End Date')
    min_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    price = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Price')
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Discount (%)')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'product_supplierinfo'
        db_table_comment = 'Supplier Pricelist'


class ProductSupplierinfoStockReplenishmentInfoRel(models.Model):
    pk = models.CompositePrimaryKey('stock_replenishment_info_id', 'product_supplierinfo_id')
    stock_replenishment_info = models.ForeignKey('StockReplenishmentInfo', models.DO_NOTHING)
    product_supplierinfo = models.ForeignKey(ProductSupplierinfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_supplierinfo_stock_replenishment_info_rel'
        db_table_comment = 'RELATION BETWEEN stock_replenishment_info AND product_supplierinfo'


class ProductTag(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='producttag_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    color = models.CharField(blank=True, null=True, db_comment='Color')
    name = models.JSONField(unique=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    visible_on_ecommerce = models.BooleanField(blank=True, null=True, db_comment='Visible on eCommerce')

    class Meta:
        managed = False
        db_table = 'product_tag'
        db_table_comment = 'Product Tag'


class ProductTagDeliveryCarrierExcludedRel(models.Model):
    pk = models.CompositePrimaryKey('delivery_carrier_id', 'product_tag_id')
    delivery_carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING)
    product_tag = models.ForeignKey(ProductTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_tag_delivery_carrier_excluded_rel'
        db_table_comment = 'RELATION BETWEEN delivery_carrier AND product_tag'


class ProductTagDeliveryCarrierMustHaveRel(models.Model):
    pk = models.CompositePrimaryKey('delivery_carrier_id', 'product_tag_id')
    delivery_carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING)
    product_tag = models.ForeignKey(ProductTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_tag_delivery_carrier_must_have_rel'
        db_table_comment = 'RELATION BETWEEN delivery_carrier AND product_tag'


class ProductTagProductProductRel(models.Model):
    pk = models.CompositePrimaryKey('product_product_id', 'product_tag_id')
    product_product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_tag = models.ForeignKey(ProductTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_tag_product_product_rel'
        db_table_comment = 'RELATION BETWEEN product_product AND product_tag'


class ProductTagProductTemplateRel(models.Model):
    pk = models.CompositePrimaryKey('product_template_id', 'product_tag_id')
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    product_tag = models.ForeignKey(ProductTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_tag_product_template_rel'
        db_table_comment = 'RELATION BETWEEN product_template AND product_tag'


class ProductTaxesRel(models.Model):
    pk = models.CompositePrimaryKey('prod_id', 'tax_id')
    prod = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_taxes_rel'
        db_table_comment = 'RELATION BETWEEN product_template AND account_tax'


class ProductTemplate(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING, db_comment='Product Category')
    uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Unit of Measure')
    uom_po = models.ForeignKey('UomUom', models.DO_NOTHING, related_name='producttemplate_uom_po_set', db_comment='Purchase Unit')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='producttemplate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    type = models.CharField(db_comment='Product Type')
    service_tracking = models.CharField(db_comment='Create on Order')
    default_code = models.CharField(blank=True, null=True, db_comment='Internal Reference')
    name = models.JSONField(db_comment='Name')
    description = models.JSONField(blank=True, null=True, db_comment='Description')
    description_purchase = models.JSONField(blank=True, null=True, db_comment='Purchase Description')
    description_sale = models.JSONField(blank=True, null=True, db_comment='Sales Description')
    product_properties = models.JSONField(blank=True, null=True, db_comment='Properties')
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Sales Price')
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Volume')
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Weight')
    sale_ok = models.BooleanField(blank=True, null=True, db_comment='Sales')
    purchase_ok = models.BooleanField(blank=True, null=True, db_comment='Purchase')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    can_image_1024_be_zoomed = models.BooleanField(blank=True, null=True, db_comment='Can Image 1024 be zoomed')
    has_configurable_attributes = models.BooleanField(blank=True, null=True, db_comment='Is a configurable product')
    is_favorite = models.BooleanField(blank=True, null=True, db_comment='Favorite')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    property_account_income_id = models.JSONField(blank=True, null=True, db_comment='Income Account')
    property_account_expense_id = models.JSONField(blank=True, null=True, db_comment='Expense Account')
    l10n_in_hsn_code = models.CharField(blank=True, null=True, db_comment='HSN/SAC Code')
    service_type = models.CharField(blank=True, null=True, db_comment='Track Service')
    sale_line_warn = models.CharField(db_comment='Sales Order Line')
    expense_policy = models.CharField(blank=True, null=True, db_comment='Re-Invoice Costs')
    invoice_policy = models.CharField(blank=True, null=True, db_comment='Invoicing Policy')
    sale_line_warn_msg = models.TextField(blank=True, null=True, db_comment='Message for Sales Order Line')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    website_size_x = models.IntegerField(blank=True, null=True, db_comment='Size X')
    website_size_y = models.IntegerField(blank=True, null=True, db_comment='Size Y')
    website_ribbon = models.ForeignKey(ProductRibbon, models.DO_NOTHING, blank=True, null=True, db_comment='Ribbon')
    website_sequence = models.IntegerField(blank=True, null=True, db_comment='Website Sequence')
    base_unit = models.ForeignKey('WebsiteBaseUnit', models.DO_NOTHING, blank=True, null=True, db_comment='Custom Unit of Measure')
    website_meta_og_img = models.CharField(blank=True, null=True, db_comment='Website opengraph image')
    website_meta_title = models.JSONField(blank=True, null=True, db_comment='Website meta title')
    website_meta_description = models.JSONField(blank=True, null=True, db_comment='Website meta description')
    website_meta_keywords = models.JSONField(blank=True, null=True, db_comment='Website meta keywords')
    seo_name = models.JSONField(blank=True, null=True, db_comment='Seo name')
    website_description = models.JSONField(blank=True, null=True, db_comment='Description for the website')
    description_ecommerce = models.JSONField(blank=True, null=True, db_comment='eCommerce Description')
    compare_list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Compare to Price')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')
    rating_last_value = models.FloatField(blank=True, null=True, db_comment='Rating Last Value')
    base_unit_count = models.FloatField(db_comment='Base Unit Count')
    sale_delay = models.IntegerField(blank=True, null=True, db_comment='Customer Lead Time')
    tracking = models.CharField(db_comment='Tracking')
    responsible_id = models.JSONField(blank=True, null=True, db_comment='Responsible')
    property_stock_production = models.JSONField(blank=True, null=True, db_comment='Production Location')
    property_stock_inventory = models.JSONField(blank=True, null=True, db_comment='Inventory Location')
    description_picking = models.JSONField(blank=True, null=True, db_comment='Description on Picking')
    description_pickingout = models.JSONField(blank=True, null=True, db_comment='Description on Delivery Orders')
    description_pickingin = models.JSONField(blank=True, null=True, db_comment='Description on Receptions')
    is_storable = models.BooleanField(blank=True, null=True, db_comment='Track Inventory')
    lot_valuated = models.BooleanField(blank=True, null=True, db_comment='Valuation by Lot/Serial number')
    country_of_origin = models.ForeignKey('ResCountry', models.DO_NOTHING, db_column='country_of_origin', blank=True, null=True, db_comment='Origin of Goods')
    hs_code = models.CharField(blank=True, null=True, db_comment='HS Code')
    out_of_stock_message = models.JSONField(blank=True, null=True, db_comment='Out-of-Stock Message')
    allow_out_of_stock_order = models.BooleanField(blank=True, null=True, db_comment='Continue selling when out-of-stock')
    show_availability = models.BooleanField(blank=True, null=True, db_comment='Show availability Qty')
    available_threshold = models.FloatField(blank=True, null=True, db_comment='Show Threshold')
    public_description = models.JSONField(blank=True, null=True, db_comment='Product Description')
    available_in_pos = models.BooleanField(blank=True, null=True, db_comment='Available in POS')
    to_weight = models.BooleanField(blank=True, null=True, db_comment='To Weigh With Scale')
    asset_category_id = models.JSONField(blank=True, null=True, db_comment='Asset Type')
    deferred_revenue_category_id = models.JSONField(blank=True, null=True, db_comment='Deferred Revenue Type')
    purchase_method = models.CharField(blank=True, null=True, db_comment='Control Policy')
    purchase_line_warn = models.CharField(db_comment='Purchase Order Line Warning')
    purchase_line_warn_msg = models.TextField(blank=True, null=True, db_comment='Message for Purchase Order Line')
    property_account_creditor_price_difference = models.JSONField(blank=True, null=True, db_comment='Price Difference Account')
    service_to_purchase = models.JSONField(blank=True, null=True, db_comment='Subcontract Service')
    can_be_expensed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template'
        db_table_comment = 'Product'


class ProductTemplateAttributeExclusion(models.Model):
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING, blank=True, null=True, db_comment='Attribute Value')
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING, db_comment='Product Template')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='producttemplateattributeexclusion_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'product_template_attribute_exclusion'
        db_table_comment = 'Product Template Attribute Exclusion'


class ProductTemplateAttributeLine(models.Model):
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING, db_comment='Product Template')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING, db_comment='Attribute')
    value_count = models.IntegerField(blank=True, null=True, db_comment='Value Count')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='producttemplateattributeline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'product_template_attribute_line'
        db_table_comment = 'Product Template Attribute Line'


class ProductTemplateAttributeValue(models.Model):
    product_attribute_value = models.ForeignKey(ProductAttributeValue, models.DO_NOTHING, db_comment='Attribute Value')
    attribute_line = models.ForeignKey(ProductTemplateAttributeLine, models.DO_NOTHING, db_comment='Attribute Line')
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING, blank=True, null=True, db_comment='Product Template')
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING, blank=True, null=True, db_comment='Attribute')
    color = models.IntegerField(blank=True, null=True, db_comment='Color')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='producttemplateattributevalue_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    price_extra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Extra Price')
    ptav_active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'product_template_attribute_value'
        unique_together = (('attribute_line', 'product_attribute_value'),)
        db_table_comment = 'Product Template Attribute Value'


class ProductTemplateAttributeValuePurchaseOrderLineRel(models.Model):
    pk = models.CompositePrimaryKey('purchase_order_line_id', 'product_template_attribute_value_id')
    purchase_order_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING)
    product_template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_value_purchase_order_line_rel'
        db_table_comment = 'RELATION BETWEEN purchase_order_line AND product_template_attribute_value'


class ProductTemplateAttributeValueSaleOrderLineRel(models.Model):
    pk = models.CompositePrimaryKey('sale_order_line_id', 'product_template_attribute_value_id')
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING)
    product_template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_value_sale_order_line_rel'
        db_table_comment = 'RELATION BETWEEN sale_order_line AND product_template_attribute_value'


class ProductVariantCombination(models.Model):
    pk = models.CompositePrimaryKey('product_product_id', 'product_template_attribute_value_id')
    product_product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_variant_combination'
        db_table_comment = 'RELATION BETWEEN product_product AND product_template_attribute_value'


class PurchaseOrder(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, db_comment='Vendor')
    dest_address = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='purchaseorder_dest_address_set', blank=True, null=True, db_comment='Dropship Address')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, db_comment='Currency')
    invoice_count = models.IntegerField(blank=True, null=True, db_comment='Bill Count')
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True, db_comment='Fiscal Position')
    payment_term = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING, blank=True, null=True, db_comment='Payment Terms')
    incoterm = models.ForeignKey(AccountIncoterms, models.DO_NOTHING, blank=True, null=True, db_comment='Incoterm')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Buyer')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='purchaseorder_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='purchaseorder_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    access_token = models.CharField(blank=True, null=True, db_comment='Security Token')
    name = models.CharField(db_comment='Order Reference')
    priority = models.CharField(blank=True, null=True, db_comment='Priority')
    origin = models.CharField(blank=True, null=True, db_comment='Source Document')
    partner_ref = models.CharField(blank=True, null=True, db_comment='Vendor Reference')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    invoice_status = models.CharField(blank=True, null=True, db_comment='Billing Status')
    notes = models.TextField(blank=True, null=True, db_comment='Terms and Conditions')
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Untaxed Amount')
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Taxes')
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total')
    amount_total_cc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Company Total')
    currency_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Currency Rate')
    mail_reminder_confirmed = models.BooleanField(blank=True, null=True, db_comment='Reminder Confirmed')
    mail_reception_confirmed = models.BooleanField(blank=True, null=True, db_comment='Reception Confirmed')
    mail_reception_declined = models.BooleanField(blank=True, null=True, db_comment='Reception Declined')
    date_order = models.DateTimeField(db_comment='Order Deadline')
    date_approve = models.DateTimeField(blank=True, null=True, db_comment='Confirmation Date')
    date_planned = models.DateTimeField(blank=True, null=True, db_comment='Expected Arrival')
    date_calendar_start = models.DateTimeField(blank=True, null=True, db_comment='Date Calendar Start')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, db_comment='Deliver To')
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True, db_comment='Procurement Group')
    incoterm_location = models.CharField(blank=True, null=True, db_comment='Incoterm Location')
    receipt_status = models.CharField(blank=True, null=True, db_comment='Receipt Status')
    effective_date = models.DateTimeField(blank=True, null=True, db_comment='Arrival')
    l10n_in_gst_treatment = models.CharField(blank=True, null=True, db_comment='GST Treatment')

    class Meta:
        managed = False
        db_table = 'purchase_order'
        db_table_comment = 'Purchase Order'


class PurchaseOrderLine(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_column='product_uom', blank=True, null=True, db_comment='Unit of Measure')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    order = models.ForeignKey(PurchaseOrder, models.DO_NOTHING, db_comment='Order Reference')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    product_packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, blank=True, null=True, db_comment='Packaging')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='purchaseorderline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    qty_received_method = models.CharField(blank=True, null=True, db_comment='Received Qty Method')
    display_type = models.CharField(blank=True, null=True, db_comment='Display Type')
    analytic_distribution = models.JSONField(blank=True, null=True, db_comment='Analytic Distribution')
    name = models.TextField(db_comment='Description')
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Discount (%)')
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Unit Price')
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Subtotal')
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total')
    qty_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Billed Qty')
    qty_received = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Received Qty')
    qty_received_manual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Manual Received Qty')
    qty_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='To Invoice Quantity')
    is_downpayment = models.BooleanField(blank=True, null=True, db_comment='Is Downpayment')
    date_planned = models.DateTimeField(blank=True, null=True, db_comment='Expected Arrival')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    product_uom_qty = models.FloatField(blank=True, null=True, db_comment='Total Quantity')
    price_tax = models.FloatField(blank=True, null=True, db_comment='Tax')
    product_packaging_qty = models.FloatField(blank=True, null=True, db_comment='Packaging Quantity')
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING, blank=True, null=True, db_comment='Orderpoint')
    location_final = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True, db_comment='Location from procurement')
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True, db_comment='Procurement group that generated this line')
    product_description_variants = models.CharField(blank=True, null=True, db_comment='Custom Description')
    propagate_cancel = models.BooleanField(blank=True, null=True, db_comment='Propagate cancellation')
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True, db_comment='Sale Order')
    sale_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True, db_comment='Origin Sale Item')

    class Meta:
        managed = False
        db_table = 'purchase_order_line'
        db_table_comment = 'Purchase Order Line'


class PurchaseOrderStockPickingRel(models.Model):
    pk = models.CompositePrimaryKey('purchase_order_id', 'stock_picking_id')
    purchase_order = models.ForeignKey(PurchaseOrder, models.DO_NOTHING)
    stock_picking = models.ForeignKey('StockPicking', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'purchase_order_stock_picking_rel'
        db_table_comment = 'RELATION BETWEEN purchase_order AND stock_picking'


class QuotationDocument(models.Model):
    ir_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, db_comment='Related attachment')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='quotationdocument_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    document_type = models.CharField(db_comment='Document Type')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'quotation_document'
        db_table_comment = "Quotation's Headers & Footers"


class QuotationDocumentSaleOrderRel(models.Model):
    pk = models.CompositePrimaryKey('sale_order_id', 'quotation_document_id')
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING)
    quotation_document = models.ForeignKey(QuotationDocument, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quotation_document_sale_order_rel'
        db_table_comment = 'RELATION BETWEEN sale_order AND quotation_document'


class QuotationDocumentSalePdfFormFieldRel(models.Model):
    pk = models.CompositePrimaryKey('quotation_document_id', 'sale_pdf_form_field_id')
    quotation_document = models.ForeignKey(QuotationDocument, models.DO_NOTHING)
    sale_pdf_form_field = models.ForeignKey('SalePdfFormField', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quotation_document_sale_pdf_form_field_rel'
        db_table_comment = 'RELATION BETWEEN quotation_document AND sale_pdf_form_field'


class RatingRating(models.Model):
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True, db_comment='Related Document Model')
    res_id = models.IntegerField(db_comment='Document')
    parent_res_model = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='ratingrating_parent_res_model_set', blank=True, null=True, db_comment='Parent Related Document Model')
    parent_res_id = models.IntegerField(blank=True, null=True, db_comment='Parent Document')
    rated_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, db_comment='Rated Operator')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='ratingrating_partner_set', blank=True, null=True, db_comment='Customer')
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True, db_comment='Message')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='ratingrating_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    res_name = models.CharField(blank=True, null=True, db_comment='Resource name')
    res_model_0 = models.CharField(db_column='res_model', blank=True, null=True, db_comment='Document Model')  # Field renamed because of name conflict.
    parent_res_name = models.CharField(blank=True, null=True, db_comment='Parent Document Name')
    parent_res_model_0 = models.CharField(db_column='parent_res_model', blank=True, null=True, db_comment='Parent Document Model')  # Field renamed because of name conflict.
    rating_text = models.CharField(blank=True, null=True, db_comment='Rating')
    access_token = models.CharField(blank=True, null=True, db_comment='Security Token')
    feedback = models.TextField(blank=True, null=True, db_comment='Comment')
    is_internal = models.BooleanField(blank=True, null=True, db_comment='Visible Internally Only')
    consumed = models.BooleanField(blank=True, null=True, db_comment='Filled Rating')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Submitted on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    rating = models.FloatField(blank=True, null=True, db_comment='Rating Value')
    publisher = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='ratingrating_publisher_set', blank=True, null=True, db_comment='Commented by')
    publisher_comment = models.TextField(blank=True, null=True, db_comment='Publisher comment')
    publisher_datetime = models.DateTimeField(blank=True, null=True, db_comment='Commented on')

    class Meta:
        managed = False
        db_table = 'rating_rating'
        db_table_comment = 'Rating'


class RefundedInvoices(models.Model):
    pk = models.CompositePrimaryKey('refund_account_move', 'original_account_move')
    refund_account_move = models.ForeignKey(AccountMove, models.DO_NOTHING, db_column='refund_account_move')
    original_account_move = models.ForeignKey(AccountMove, models.DO_NOTHING, db_column='original_account_move', related_name='refundedinvoices_original_account_move_set')

    class Meta:
        managed = False
        db_table = 'refunded_invoices'
        db_table_comment = 'RELATION BETWEEN account_move AND account_move'


class RegistrationEditor(models.Model):
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, db_comment='Sales Order')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='registrationeditor_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'registration_editor'
        db_table_comment = 'Edit Attendee Details on Sales Confirmation'


class RegistrationEditorLine(models.Model):
    editor = models.ForeignKey(RegistrationEditor, models.DO_NOTHING, blank=True, null=True, db_comment='Editor')
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True, db_comment='Sales Order Line')
    event = models.ForeignKey(EventEvent, models.DO_NOTHING, db_comment='Event')
    registration = models.ForeignKey(EventRegistration, models.DO_NOTHING, blank=True, null=True, db_comment='Original Registration')
    event_ticket = models.ForeignKey(EventEventTicket, models.DO_NOTHING, blank=True, null=True, db_comment='Event Ticket')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='registrationeditorline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    email = models.CharField(blank=True, null=True, db_comment='Email')
    phone = models.CharField(blank=True, null=True, db_comment='Phone')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'registration_editor_line'
        db_table_comment = 'Edit Attendee Line on Sales Confirmation'


class RelModulesLangexport(models.Model):
    pk = models.CompositePrimaryKey('wiz_id', 'module_id')
    wiz = models.ForeignKey(BaseLanguageExport, models.DO_NOTHING)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_modules_langexport'
        db_table_comment = 'RELATION BETWEEN base_language_export AND ir_module_module'


class RelServerActions(models.Model):
    pk = models.CompositePrimaryKey('server_id', 'action_id')
    server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    action = models.ForeignKey(IrActServer, models.DO_NOTHING, related_name='relserveractions_action_set')

    class Meta:
        managed = False
        db_table = 'rel_server_actions'
        db_table_comment = 'RELATION BETWEEN ir_act_server AND ir_act_server'


class ReportLayout(models.Model):
    view = models.ForeignKey(IrUiView, models.DO_NOTHING, db_comment='Document Template')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='reportlayout_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    image = models.CharField(blank=True, null=True, db_comment='Preview image src')
    pdf = models.CharField(blank=True, null=True, db_comment='Preview pdf src')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'report_layout'
        db_table_comment = 'Report Layout'


class ReportPaperformat(models.Model):
    page_height = models.IntegerField(blank=True, null=True, db_comment='Page height (mm)')
    page_width = models.IntegerField(blank=True, null=True, db_comment='Page width (mm)')
    header_spacing = models.IntegerField(blank=True, null=True, db_comment='Header spacing')
    dpi = models.IntegerField(db_comment='Output DPI')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='reportpaperformat_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    format = models.CharField(blank=True, null=True, db_comment='Paper size')
    orientation = models.CharField(blank=True, null=True, db_comment='Orientation')
    default = models.BooleanField(blank=True, null=True, db_comment='Default paper format?')
    header_line = models.BooleanField(blank=True, null=True, db_comment='Display a header line')
    disable_shrinking = models.BooleanField(blank=True, null=True, db_comment='Disable smart shrinking')
    css_margins = models.BooleanField(blank=True, null=True, db_comment='Use css margins')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    margin_top = models.FloatField(blank=True, null=True, db_comment='Top Margin (mm)')
    margin_bottom = models.FloatField(blank=True, null=True, db_comment='Bottom Margin (mm)')
    margin_left = models.FloatField(blank=True, null=True, db_comment='Left Margin (mm)')
    margin_right = models.FloatField(blank=True, null=True, db_comment='Right Margin (mm)')

    class Meta:
        managed = False
        db_table = 'report_paperformat'
        db_table_comment = 'Paper Format Config'


class ResBank(models.Model):
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, db_column='state', blank=True, null=True, db_comment='Fed. State')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, db_column='country', blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='resbank_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    street = models.CharField(blank=True, null=True, db_comment='Street')
    street2 = models.CharField(blank=True, null=True, db_comment='Street2')
    zip = models.CharField(blank=True, null=True, db_comment='Zip')
    city = models.CharField(blank=True, null=True, db_comment='City')
    email = models.CharField(blank=True, null=True, db_comment='Email')
    phone = models.CharField(blank=True, null=True, db_comment='Phone')
    bic = models.CharField(blank=True, null=True, db_comment='Bank Identifier Code')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_bank'
        db_table_comment = 'Bank'


class ResCompany(models.Model):
    name = models.CharField(unique=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    parent_path = models.CharField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Company')
    paperformat = models.ForeignKey(ReportPaperformat, models.DO_NOTHING, blank=True, null=True, db_comment='Paper format')
    external_report_layout = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True, db_comment='Document Template')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='rescompany_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    email = models.CharField(blank=True, null=True, db_comment='Email')
    phone = models.CharField(blank=True, null=True, db_comment='Phone')
    mobile = models.CharField(blank=True, null=True, db_comment='Mobile')
    font = models.CharField(blank=True, null=True, db_comment='Font')
    primary_color = models.CharField(blank=True, null=True, db_comment='Primary Color')
    secondary_color = models.CharField(blank=True, null=True, db_comment='Secondary Color')
    layout_background = models.CharField(db_comment='Layout Background')
    report_header = models.JSONField(blank=True, null=True, db_comment='Company Tagline')
    report_footer = models.JSONField(blank=True, null=True, db_comment='Report Footer')
    company_details = models.JSONField(blank=True, null=True, db_comment='Company Details')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    uses_default_logo = models.BooleanField(blank=True, null=True, db_comment='Uses Default Logo')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    logo_web = models.BinaryField(blank=True, null=True, db_comment='Logo Web')
    social_twitter = models.CharField(blank=True, null=True, db_comment='X Account')
    social_facebook = models.CharField(blank=True, null=True, db_comment='Facebook Account')
    social_github = models.CharField(blank=True, null=True, db_comment='GitHub Account')
    social_linkedin = models.CharField(blank=True, null=True, db_comment='LinkedIn Account')
    social_youtube = models.CharField(blank=True, null=True, db_comment='Youtube Account')
    social_instagram = models.CharField(blank=True, null=True, db_comment='Instagram Account')
    social_tiktok = models.CharField(blank=True, null=True, db_comment='TikTok Account')
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True, db_comment='Default Working Hours')
    alias_domain = models.ForeignKey(MailAliasDomain, models.DO_NOTHING, blank=True, null=True, db_comment='Email Domain')
    alias_domain_name = models.CharField(blank=True, null=True, db_comment='Alias Domain Name')
    email_primary_color = models.CharField(blank=True, null=True, db_comment='Email Header Color')
    email_secondary_color = models.CharField(blank=True, null=True, db_comment='Email Button Color')
    partner_gid = models.IntegerField(blank=True, null=True, db_comment='Company database ID')
    iap_enrich_auto_done = models.BooleanField(blank=True, null=True, db_comment='Enrich Done')
    snailmail_color = models.BooleanField(blank=True, null=True, db_comment='Snailmail Color')
    snailmail_cover = models.BooleanField(blank=True, null=True, db_comment='Add a Cover Page')
    snailmail_duplex = models.BooleanField(blank=True, null=True, db_comment='Both sides')
    payment_onboarding_payment_method = models.CharField(blank=True, null=True, db_comment='Selected onboarding payment method')
    fiscalyear_last_day = models.IntegerField(db_comment='Fiscalyear Last Day')
    transfer_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Inter-Banks Transfer Account')
    default_cash_difference_income_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_default_cash_difference_income_account_set', blank=True, null=True, db_comment='Cash Difference Income')
    default_cash_difference_expense_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_default_cash_difference_expense_account_set', blank=True, null=True, db_comment='Cash Difference Expense')
    account_journal_suspense_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_account_journal_suspense_account_set', blank=True, null=True, db_comment='Journal Suspense Account')
    account_journal_early_pay_discount_gain_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_account_journal_early_pay_discount_gain_account_set', blank=True, null=True, db_comment='Cash Discount Write-Off Gain Account')
    account_journal_early_pay_discount_loss_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_account_journal_early_pay_discount_loss_account_set', blank=True, null=True, db_comment='Cash Discount Write-Off Loss Account')
    account_sale_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True, db_comment='Default Sale Tax')
    account_purchase_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, related_name='rescompany_account_purchase_tax_set', blank=True, null=True, db_comment='Default Purchase Tax')
    currency_exchange_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Exchange Gain or Loss Journal')
    income_currency_exchange_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_income_currency_exchange_account_set', blank=True, null=True, db_comment='Gain Exchange Rate Account')
    expense_currency_exchange_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_expense_currency_exchange_account_set', blank=True, null=True, db_comment='Loss Exchange Rate Account')
    incoterm = models.ForeignKey(AccountIncoterms, models.DO_NOTHING, blank=True, null=True, db_comment='Default incoterm')
    batch_payment_sequence = models.ForeignKey(IrSequence, models.DO_NOTHING, blank=True, null=True, db_comment='Batch Payment Sequence')
    account_opening_move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True, db_comment='Opening Journal Entry')
    account_default_pos_receivable_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_account_default_pos_receivable_account_set', blank=True, null=True, db_comment='Default PoS Receivable Account')
    expense_accrual_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_expense_accrual_account_set', blank=True, null=True, db_comment='Expense Accrual Account')
    revenue_accrual_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_revenue_accrual_account_set', blank=True, null=True, db_comment='Revenue Accrual Account')
    automatic_entry_default_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, related_name='rescompany_automatic_entry_default_journal_set', blank=True, null=True, db_comment='Automatic Entry Default Journal')
    account_fiscal_country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True, db_comment='Fiscal Country')
    tax_cash_basis_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, related_name='rescompany_tax_cash_basis_journal_set', blank=True, null=True, db_comment='Cash Basis Journal')
    account_cash_basis_base_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_account_cash_basis_base_account_set', blank=True, null=True, db_comment='Base Tax Received Account')
    account_discount_income_allocation = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_account_discount_income_allocation_set', blank=True, null=True, db_comment='Separate account for income discount')
    account_discount_expense_allocation = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_account_discount_expense_allocation_set', blank=True, null=True, db_comment='Separate account for expense discount')
    fiscalyear_last_month = models.CharField(db_comment='Fiscalyear Last Month')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart Template')
    bank_account_code_prefix = models.CharField(blank=True, null=True, db_comment='Prefix of the bank accounts')
    cash_account_code_prefix = models.CharField(blank=True, null=True, db_comment='Prefix of the cash accounts')
    transfer_account_code_prefix = models.CharField(blank=True, null=True, db_comment='Prefix of the transfer accounts')
    tax_calculation_rounding_method = models.CharField(blank=True, null=True, db_comment='Tax Calculation Rounding Method')
    terms_type = models.CharField(blank=True, null=True, db_comment='Terms & Conditions format')
    quick_edit_mode = models.CharField(blank=True, null=True, db_comment='Quick encoding')
    account_price_include = models.CharField(db_comment='Default Sales Price Include')
    fiscalyear_lock_date = models.DateField(blank=True, null=True, db_comment='Global Lock Date')
    tax_lock_date = models.DateField(blank=True, null=True, db_comment='Tax Return Lock Date')
    sale_lock_date = models.DateField(blank=True, null=True, db_comment='Sales Lock Date')
    purchase_lock_date = models.DateField(blank=True, null=True, db_comment='Purchase Lock date')
    hard_lock_date = models.DateField(blank=True, null=True, db_comment='Hard Lock Date')
    account_opening_date = models.DateField(db_comment='Opening Entry')
    invoice_terms = models.JSONField(blank=True, null=True, db_comment='Default Terms and Conditions')
    invoice_terms_html = models.JSONField(blank=True, null=True, db_comment='Default Terms and Conditions as a Web page')
    expects_chart_of_accounts = models.BooleanField(blank=True, null=True, db_comment='Expects a Chart of Accounts')
    anglo_saxon_accounting = models.BooleanField(blank=True, null=True, db_comment='Use anglo-saxon accounting')
    qr_code = models.BooleanField(blank=True, null=True, db_comment='Display QR-code on invoices')
    display_invoice_amount_total_words = models.BooleanField(blank=True, null=True, db_comment='Total amount of invoice in letters')
    display_invoice_tax_company_currency = models.BooleanField(blank=True, null=True, db_comment='Taxes in company currency')
    account_use_credit_limit = models.BooleanField(blank=True, null=True, db_comment='Sales Credit Limit')
    tax_exigibility = models.BooleanField(blank=True, null=True, db_comment='Use Cash Basis')
    account_storno = models.BooleanField(blank=True, null=True, db_comment='Storno accounting')
    check_account_audit_trail = models.BooleanField(blank=True, null=True, db_comment='Audit Trail')
    autopost_bills = models.BooleanField(blank=True, null=True, db_comment='Auto-validate bills')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    vat_check_vies = models.BooleanField(blank=True, null=True, db_comment='Verify VAT Numbers')
    l10n_in_upi_id = models.CharField(blank=True, null=True, db_comment='UPI Id')
    l10n_in_hsn_code_digit = models.CharField(blank=True, null=True, db_comment='HSN Code Digit')
    l10n_in_pan = models.CharField(blank=True, null=True, db_comment='PAN')
    l10n_in_edi_production_env = models.BooleanField(blank=True, null=True, db_comment='Indian Production Environment')
    quotation_validity_days = models.IntegerField(blank=True, null=True, db_comment='Default Quotation Validity')
    sale_discount_product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Discount Product')
    sale_onboarding_payment_method = models.CharField(blank=True, null=True, db_comment='Sale onboarding selected payment method')
    portal_confirmation_sign = models.BooleanField(blank=True, null=True, db_comment='Online Signature')
    portal_confirmation_pay = models.BooleanField(blank=True, null=True, db_comment='Online Payment')
    prepayment_percent = models.FloatField(blank=True, null=True, db_comment='Prepayment percentage')
    nomenclature = models.ForeignKey(BarcodeNomenclature, models.DO_NOTHING, blank=True, null=True, db_comment='Nomenclature')
    internal_transit_location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True, db_comment='Internal Transit Location')
    stock_mail_confirmation_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True, db_comment='Email Template confirmation picking')
    annual_inventory_day = models.IntegerField(blank=True, null=True, db_comment='Day of the month')
    annual_inventory_month = models.CharField(blank=True, null=True, db_comment='Annual Inventory Month')
    stock_move_email_validation = models.BooleanField(blank=True, null=True, db_comment='Email Confirmation picking')
    account_production_wip_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_account_production_wip_account_set', blank=True, null=True, db_comment='Production WIP Account')
    account_production_wip_overhead_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_account_production_wip_overhead_account_set', blank=True, null=True, db_comment='Production WIP Overhead Account')
    stock_sms_confirmation_template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='SMS Template')
    stock_move_sms_validation = models.BooleanField(blank=True, null=True, db_comment='SMS Confirmation')
    has_received_warning_stock_sms = models.BooleanField(blank=True, null=True, db_comment='Has Received Warning Stock Sms')
    security_lead = models.FloatField(db_comment='Sales Safety Days')
    point_of_sale_update_stock_quantities = models.CharField(blank=True, null=True, db_comment='Update quantities in stock')
    point_of_sale_ticket_portal_url_display_mode = models.CharField(db_comment='Print')
    point_of_sale_use_ticket_qr_code = models.BooleanField(blank=True, null=True, db_comment='Self-service invoicing')
    point_of_sale_ticket_unique_code = models.BooleanField(blank=True, null=True, db_comment='Generate a code on ticket')
    account_check_printing_layout = models.CharField(blank=True, null=True, db_comment='Check Layout')
    account_check_printing_date_label = models.BooleanField(blank=True, null=True, db_comment='Print Date Label')
    account_check_printing_multi_stub = models.BooleanField(blank=True, null=True, db_comment='Multi-Pages Check Stub')
    account_check_printing_margin_top = models.FloatField(blank=True, null=True, db_comment='Check Top Margin')
    account_check_printing_margin_left = models.FloatField(blank=True, null=True, db_comment='Check Left Margin')
    account_check_printing_margin_right = models.FloatField(blank=True, null=True, db_comment='Right Margin')
    sale_order_template = models.ForeignKey('SaleOrderTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='Default Sale Template')
    po_lock = models.CharField(blank=True, null=True, db_comment='Purchase Order Modification')
    po_double_validation = models.CharField(blank=True, null=True, db_comment='Levels of Approvals')
    po_double_validation_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Double validation amount')
    po_lead = models.FloatField(db_comment='Purchase Lead Time')
    days_to_purchase = models.FloatField(blank=True, null=True, db_comment='Days to Purchase')
    hr_presence_control_email_amount = models.IntegerField(blank=True, null=True, db_comment='# emails to send')
    hr_presence_control_ip_list = models.CharField(blank=True, null=True, db_comment='Valid IP addresses')
    employee_properties_definition = models.JSONField(blank=True, null=True, db_comment='Employee Properties')
    hr_presence_control_login = models.BooleanField(blank=True, null=True, db_comment='Based on user status in system')
    hr_presence_control_email = models.BooleanField(blank=True, null=True, db_comment='Based on number of emails sent')
    hr_presence_control_ip = models.BooleanField(blank=True, null=True, db_comment='Based on IP Address')
    hr_presence_control_attendance = models.BooleanField(blank=True, null=True, db_comment='Based on attendances')
    expense_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, related_name='rescompany_expense_journal_set', blank=True, null=True, db_comment='Default Expense Journal')
    expense_outstanding_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='rescompany_expense_outstanding_account_set', blank=True, null=True, db_comment='Outstanding Account')
    manufacturing_lead = models.FloatField(db_comment='Manufacturing Lead Time')
    l10n_in_edi_username = models.CharField(blank=True, null=True, db_comment='E-invoice (IN) Username')
    l10n_in_edi_password = models.CharField(blank=True, null=True, db_comment='E-invoice (IN) Password')
    l10n_in_edi_token = models.CharField(blank=True, null=True, db_comment='E-invoice (IN) Token')
    l10n_in_edi_token_validity = models.DateTimeField(blank=True, null=True, db_comment='E-invoice (IN) Valid Until')

    class Meta:
        managed = False
        db_table = 'res_company'


class ResCompanyUsersRel(models.Model):
    pk = models.CompositePrimaryKey('cid', 'user_id')
    cid = models.ForeignKey(ResCompany, models.DO_NOTHING, db_column='cid')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_company_users_rel'
        db_table_comment = 'RELATION BETWEEN res_company AND res_users'


class ResConfig(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='resconfig_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_config'
        db_table_comment = 'Config'


class ResConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='resconfigsettings_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    web_app_name = models.CharField(blank=True, null=True, db_comment='Web App Name')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    user_default_rights = models.BooleanField(blank=True, null=True, db_comment='Default Access Rights')
    module_base_import = models.BooleanField(blank=True, null=True, db_comment='Allow users to import data from CSV/XLS/XLSX/ODS files')
    module_google_calendar = models.BooleanField(blank=True, null=True, db_comment='Allow the users to synchronize their calendar  with Google Calendar')
    module_microsoft_calendar = models.BooleanField(blank=True, null=True, db_comment='Allow the users to synchronize their calendar with Outlook Calendar')
    module_mail_plugin = models.BooleanField(blank=True, null=True, db_comment='Allow integration with the mail plugins')
    module_auth_oauth = models.BooleanField(blank=True, null=True, db_comment='Use external authentication providers (OAuth)')
    module_auth_ldap = models.BooleanField(blank=True, null=True, db_comment='LDAP Authentication')
    module_account_inter_company_rules = models.BooleanField(blank=True, null=True, db_comment='Manage Inter Company')
    module_voip = models.BooleanField(blank=True, null=True, db_comment='VoIP')
    module_web_unsplash = models.BooleanField(blank=True, null=True, db_comment='Unsplash Image Library')
    module_sms = models.BooleanField(blank=True, null=True, db_comment='SMS')
    module_partner_autocomplete = models.BooleanField(blank=True, null=True, db_comment='Partner Autocomplete')
    module_base_geolocalize = models.BooleanField(blank=True, null=True, db_comment='GeoLocalize')
    module_google_recaptcha = models.BooleanField(blank=True, null=True, db_comment='reCAPTCHA')
    module_website_cf_turnstile = models.BooleanField(blank=True, null=True, db_comment='Cloudflare Turnstile')
    group_multi_currency = models.BooleanField(blank=True, null=True, db_comment='Multi-Currencies')
    show_effect = models.BooleanField(blank=True, null=True, db_comment='Show Effect')
    module_product_images = models.BooleanField(blank=True, null=True, db_comment='Get product pictures using barcode')
    profiling_enabled_until = models.DateTimeField(blank=True, null=True, db_comment='Profiling enabled until')
    unsplash_access_key = models.CharField(blank=True, null=True, db_comment='Access Key')
    unsplash_app_id = models.CharField(blank=True, null=True, db_comment='Application ID')
    recaptcha_public_key = models.CharField(blank=True, null=True, db_comment='Site Key')
    recaptcha_private_key = models.CharField(blank=True, null=True, db_comment='Secret Key')
    recaptcha_min_score = models.FloatField(blank=True, null=True, db_comment='Minimum score')
    tenor_gif_limit = models.IntegerField(blank=True, null=True, db_comment='Tenor Gif Limit')
    twilio_account_sid = models.CharField(blank=True, null=True, db_comment='Twilio Account SID')
    twilio_account_token = models.CharField(blank=True, null=True, db_comment='Twilio Account Auth Token')
    sfu_server_url = models.CharField(blank=True, null=True, db_comment='SFU Server URL')
    sfu_server_key = models.CharField(blank=True, null=True, db_comment='SFU Server key')
    tenor_api_key = models.CharField(blank=True, null=True, db_comment='Tenor API key')
    tenor_content_filter = models.CharField(blank=True, null=True, db_comment='Tenor content filter')
    google_translate_api_key = models.CharField(blank=True, null=True, db_comment='Message Translation API Key')
    external_email_server_default = models.BooleanField(blank=True, null=True, db_comment='Use Custom Email Servers')
    module_google_gmail = models.BooleanField(blank=True, null=True, db_comment='Support Gmail Authentication')
    module_microsoft_outlook = models.BooleanField(blank=True, null=True, db_comment='Support Outlook Authentication')
    restrict_template_rendering = models.BooleanField(blank=True, null=True, db_comment='Restrict Template Rendering')
    use_twilio_rtc_servers = models.BooleanField(blank=True, null=True, db_comment='Use Twilio ICE servers')
    group_analytic_accounting = models.BooleanField(blank=True, null=True, db_comment='Analytic Accounting')
    auth_signup_template_user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='resconfigsettings_auth_signup_template_user_set', blank=True, null=True, db_comment='Template user for new users created through signup')
    auth_signup_uninvited = models.CharField(blank=True, null=True, db_comment='Customer Account')
    auth_signup_reset_password = models.BooleanField(blank=True, null=True, db_comment='Enable password reset from Login page')
    google_gmail_client_identifier = models.CharField(blank=True, null=True, db_comment='Gmail Client Id')
    google_gmail_client_secret = models.CharField(blank=True, null=True, db_comment='Gmail Client Secret')
    product_weight_in_lbs = models.CharField(blank=True, null=True, db_comment='Weight unit of measure')
    product_volume_volume_in_cubic_feet = models.CharField(blank=True, null=True, db_comment='Volume unit of measure')
    group_uom = models.BooleanField(blank=True, null=True, db_comment='Units of Measure')
    group_product_variant = models.BooleanField(blank=True, null=True, db_comment='Variants')
    module_loyalty = models.BooleanField(blank=True, null=True, db_comment='Promotions, Coupons, Gift Card & Loyalty Program')
    group_stock_packaging = models.BooleanField(blank=True, null=True, db_comment='Product Packagings')
    group_product_pricelist = models.BooleanField(blank=True, null=True, db_comment='Pricelists')
    digest = models.ForeignKey(DigestDigest, models.DO_NOTHING, blank=True, null=True, db_comment='Digest Email')
    digest_emails = models.BooleanField(blank=True, null=True, db_comment='Digest Emails')
    chart_template = models.CharField(blank=True, null=True, db_comment='Chart Template')
    module_account_accountant = models.BooleanField(blank=True, null=True, db_comment='Accounting')
    group_warning_account = models.BooleanField(blank=True, null=True, db_comment='Warnings in Invoices')
    group_cash_rounding = models.BooleanField(blank=True, null=True, db_comment='Cash Rounding')
    group_show_sale_receipts = models.BooleanField(blank=True, null=True, db_comment='Sale Receipt')
    group_show_purchase_receipts = models.BooleanField(blank=True, null=True, db_comment='Purchase Receipt')
    module_account_budget = models.BooleanField(blank=True, null=True, db_comment='Budget Management')
    module_account_payment = models.BooleanField(blank=True, null=True, db_comment='Invoice Online Payment')
    module_account_reports = models.BooleanField(blank=True, null=True, db_comment='Dynamic Reports')
    module_account_check_printing = models.BooleanField(blank=True, null=True, db_comment='Allow check printing and deposits')
    module_account_batch_payment = models.BooleanField(blank=True, null=True, db_comment='Use batch payments')
    module_account_iso20022 = models.BooleanField(blank=True, null=True, db_comment='SEPA Credit Transfer / ISO20022')
    module_account_sepa_direct_debit = models.BooleanField(blank=True, null=True, db_comment='Use SEPA Direct Debit')
    module_account_bank_statement_import_qif = models.BooleanField(blank=True, null=True, db_comment='Import .qif files')
    module_account_bank_statement_import_ofx = models.BooleanField(blank=True, null=True, db_comment='Import in .ofx format')
    module_account_bank_statement_import_csv = models.BooleanField(blank=True, null=True, db_comment='Import in .csv, .xls, and .xlsx format')
    module_account_bank_statement_import_camt = models.BooleanField(blank=True, null=True, db_comment='Import in CAMT.053 format')
    module_currency_rate_live = models.BooleanField(blank=True, null=True, db_comment='Automatic Currency Rates')
    module_account_intrastat = models.BooleanField(blank=True, null=True, db_comment='Intrastat')
    module_product_margin = models.BooleanField(blank=True, null=True, db_comment='Allow Product Margin')
    module_l10n_eu_oss = models.BooleanField(blank=True, null=True, db_comment='EU Intra-community Distance Selling')
    module_account_extract = models.BooleanField(blank=True, null=True, db_comment='Document Digitization')
    module_account_invoice_extract = models.BooleanField(blank=True, null=True, db_comment='Invoice Digitization')
    module_account_bank_statement_extract = models.BooleanField(blank=True, null=True, db_comment='Bank Statement Digitization')
    module_snailmail_account = models.BooleanField(blank=True, null=True, db_comment='Snailmail')
    module_account_peppol = models.BooleanField(blank=True, null=True, db_comment='PEPPOL Invoicing')
    use_invoice_terms = models.BooleanField(blank=True, null=True, db_comment='Default Terms & Conditions')
    group_sale_delivery_address = models.BooleanField(blank=True, null=True, db_comment='Customer Addresses')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='website')
    group_multi_website = models.BooleanField(blank=True, null=True, db_comment='Multi-website')
    module_website_livechat = models.BooleanField(blank=True, null=True, db_comment='Module Website Livechat')
    module_marketing_automation = models.BooleanField(blank=True, null=True, db_comment='Module Marketing Automation')
    pay_invoices_online = models.BooleanField(blank=True, null=True, db_comment='Pay Invoices Online')
    group_l10n_in_reseller = models.BooleanField(blank=True, null=True, db_comment='Manage Reseller(E-Commerce)')
    module_l10n_in_edi = models.BooleanField(blank=True, null=True, db_comment='Indian Electronic Invoicing')
    module_l10n_in_edi_ewaybill = models.BooleanField(blank=True, null=True, db_comment='Indian Electronic Waybill')
    module_l10n_in_gstin_status = models.BooleanField(blank=True, null=True, db_comment='Check GST Number Status')
    module_l10n_in_withholding = models.BooleanField(blank=True, null=True, db_comment='Indian TDS and TCS')
    module_l10n_in_enet_batch_payment = models.BooleanField(blank=True, null=True, db_comment='Vendor Payment')
    invoice_mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True, db_comment='Invoice Email Template')
    default_invoice_policy = models.CharField(blank=True, null=True, db_comment='Invoicing Policy')
    group_auto_done_setting = models.BooleanField(blank=True, null=True, db_comment='Lock Confirmed Sales')
    group_discount_per_so_line = models.BooleanField(blank=True, null=True, db_comment='Discounts')
    group_proforma_sales = models.BooleanField(blank=True, null=True, db_comment='Pro-Forma Invoice')
    group_warning_sale = models.BooleanField(blank=True, null=True, db_comment='Sale Order Warnings')
    automatic_invoice = models.BooleanField(blank=True, null=True, db_comment='Automatic Invoice')
    module_delivery = models.BooleanField(blank=True, null=True, db_comment='Delivery Methods')
    module_delivery_bpost = models.BooleanField(blank=True, null=True, db_comment='bpost Connector')
    module_delivery_dhl = models.BooleanField(blank=True, null=True, db_comment='DHL Express Connector')
    module_delivery_easypost = models.BooleanField(blank=True, null=True, db_comment='Easypost Connector')
    module_delivery_fedex = models.BooleanField(blank=True, null=True, db_comment='FedEx Connector')
    module_delivery_sendcloud = models.BooleanField(blank=True, null=True, db_comment='Sendcloud Connector')
    module_delivery_shiprocket = models.BooleanField(blank=True, null=True, db_comment='Shiprocket Connector')
    module_delivery_ups = models.BooleanField(blank=True, null=True, db_comment='UPS Connector')
    module_delivery_usps = models.BooleanField(blank=True, null=True, db_comment='USPS Connector')
    module_delivery_starshipit = models.BooleanField(blank=True, null=True, db_comment='Starshipit Connector')
    module_product_email_template = models.BooleanField(blank=True, null=True, db_comment='Specific Email')
    module_sale_amazon = models.BooleanField(blank=True, null=True, db_comment='Amazon Sync')
    module_sale_loyalty = models.BooleanField(blank=True, null=True, db_comment='Coupons & Loyalty')
    module_sale_margin = models.BooleanField(blank=True, null=True, db_comment='Margins')
    module_sale_product_matrix = models.BooleanField(blank=True, null=True, db_comment='Sales Grid Entry')
    module_sale_pdf_quote_builder = models.BooleanField(blank=True, null=True, db_comment='PDF Quote builder')
    module_sale_commission = models.BooleanField(blank=True, null=True, db_comment='Commissions')
    group_delivery_invoice_address = models.BooleanField(blank=True, null=True, db_comment='Shipping Address')
    group_show_uom_price = models.BooleanField(blank=True, null=True, db_comment='Base Unit Price')
    group_product_price_comparison = models.BooleanField(blank=True, null=True, db_comment='Comparison Price')
    module_account = models.BooleanField(blank=True, null=True, db_comment='Invoicing')
    module_delivery_mondialrelay = models.BooleanField(blank=True, null=True, db_comment='Mondial Relay Connector')
    module_website_sale_autocomplete = models.BooleanField(blank=True, null=True, db_comment='Address Autocomplete')
    module_website_sale_comparison = models.BooleanField(blank=True, null=True, db_comment='Product Comparison Tool')
    module_website_sale_collect = models.BooleanField(blank=True, null=True, db_comment='Click & Collect')
    module_website_sale_wishlist = models.BooleanField(blank=True, null=True, db_comment='Wishlists')
    enabled_extra_checkout_step = models.BooleanField(blank=True, null=True, db_comment='Extra Step During Checkout')
    enabled_buy_now_button = models.BooleanField(blank=True, null=True, db_comment='Buy Now')
    barcode_separator = models.CharField(blank=True, null=True, db_comment='Separator')
    module_product_expiry = models.BooleanField(blank=True, null=True, db_comment='Expiration Dates')
    group_stock_production_lot = models.BooleanField(blank=True, null=True, db_comment='Lots & Serial Numbers')
    group_stock_lot_print_gs1 = models.BooleanField(blank=True, null=True, db_comment='Print GS1 Barcodes for Lots & Serial Numbers')
    group_lot_on_delivery_slip = models.BooleanField(blank=True, null=True, db_comment='Display Lots & Serial Numbers on Delivery Slips')
    group_stock_tracking_lot = models.BooleanField(blank=True, null=True, db_comment='Packages')
    group_stock_tracking_owner = models.BooleanField(blank=True, null=True, db_comment='Consignment')
    group_stock_adv_location = models.BooleanField(blank=True, null=True, db_comment='Multi-Step Routes')
    group_warning_stock = models.BooleanField(blank=True, null=True, db_comment='Warnings for Stock')
    group_stock_sign_delivery = models.BooleanField(blank=True, null=True, db_comment='Signature')
    module_stock_picking_batch = models.BooleanField(blank=True, null=True, db_comment='Batch, Wave & Cluster Transfers')
    module_stock_barcode = models.BooleanField(blank=True, null=True, db_comment='Barcode Scanner')
    module_stock_barcode_barcodelookup = models.BooleanField(blank=True, null=True, db_comment='Stock Barcode Database')
    module_stock_sms = models.BooleanField(blank=True, null=True, db_comment='SMS Confirmation')
    module_quality_control = models.BooleanField(blank=True, null=True, db_comment='Quality')
    module_quality_control_worksheet = models.BooleanField(blank=True, null=True, db_comment='Quality Worksheet')
    group_stock_multi_locations = models.BooleanField(blank=True, null=True, db_comment='Storage Locations')
    group_stock_reception_report = models.BooleanField(blank=True, null=True, db_comment='Reception Report')
    module_stock_dropshipping = models.BooleanField(blank=True, null=True, db_comment='Dropshipping')
    module_stock_fleet = models.BooleanField(blank=True, null=True, db_comment='Dispatch Management System')
    module_stock_landed_costs = models.BooleanField(blank=True, null=True, db_comment='Landed Costs')
    group_lot_on_invoice = models.BooleanField(blank=True, null=True, db_comment='Display Lots & Serial Numbers on Invoices')
    group_stock_accounting_automatic = models.BooleanField(blank=True, null=True, db_comment='Automatic Stock Accounting')
    default_picking_policy = models.CharField(db_comment='Picking Policy')
    use_security_lead = models.BooleanField(blank=True, null=True, db_comment='Security Lead Time for Sales')
    allow_out_of_stock_order = models.BooleanField(blank=True, null=True, db_comment='Continue selling when out-of-stock')
    show_availability = models.BooleanField(blank=True, null=True, db_comment='Show availability Qty')
    available_threshold = models.FloatField(blank=True, null=True, db_comment='Show Threshold')
    pos_config = models.ForeignKey(PosConfig, models.DO_NOTHING, blank=True, null=True, db_comment='Point of Sale')
    pos_default_fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True, db_comment='Default Fiscal Position')
    pos_pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING, blank=True, null=True, db_comment='Default Pricelist')
    pos_tip_product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Tip Product')
    pos_receipt_footer = models.TextField(blank=True, null=True, db_comment='Receipt Footer')
    pos_receipt_header = models.TextField(blank=True, null=True, db_comment='Receipt Header')
    module_pos_adyen = models.BooleanField(blank=True, null=True, db_comment='Adyen Payment Terminal')
    module_pos_stripe = models.BooleanField(blank=True, null=True, db_comment='Stripe Payment Terminal')
    module_pos_six = models.BooleanField(blank=True, null=True, db_comment='Six Payment Terminal')
    module_pos_viva_wallet = models.BooleanField(blank=True, null=True, db_comment='Viva Wallet Payment Terminal')
    module_pos_paytm = models.BooleanField(blank=True, null=True, db_comment='PayTM Payment Terminal')
    module_pos_razorpay = models.BooleanField(blank=True, null=True, db_comment='Razorpay Payment Terminal')
    module_pos_mercado_pago = models.BooleanField(blank=True, null=True, db_comment='Mercado Pago Payment Terminal')
    module_pos_preparation_display = models.BooleanField(blank=True, null=True, db_comment='Preparation Display')
    module_pos_pricer = models.BooleanField(blank=True, null=True, db_comment='Pricer electronic price tags')
    is_kiosk_mode = models.BooleanField(blank=True, null=True, db_comment='Is Kiosk Mode')
    pos_is_order_printer = models.BooleanField(blank=True, null=True, db_comment='Pos Is Order Printer')
    pos_iface_cashdrawer = models.BooleanField(blank=True, null=True, db_comment='Cashdrawer')
    pos_iface_electronic_scale = models.BooleanField(blank=True, null=True, db_comment='Electronic Scale')
    pos_iface_print_via_proxy = models.BooleanField(blank=True, null=True, db_comment='Print via Proxy')
    pos_iface_scan_via_proxy = models.BooleanField(blank=True, null=True, db_comment='Scan via Proxy')
    pos_epson_printer_ip = models.CharField(blank=True, null=True, db_comment='Pos Epson Printer Ip')
    customer_credit_limit = models.BooleanField(blank=True, null=True, db_comment='Customer Credit Limit')
    group_sale_order_template = models.BooleanField(blank=True, null=True, db_comment='Quotation Templates')
    mass_mailing_mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True, db_comment='Mail Server')
    group_mass_mailing_campaign = models.BooleanField(blank=True, null=True, db_comment='Mailing Campaigns')
    mass_mailing_outgoing_mail_server = models.BooleanField(blank=True, null=True, db_comment='Dedicated Server')
    show_blacklist_buttons = models.BooleanField(blank=True, null=True, db_comment='Blacklist Option when Unsubscribing')
    mass_mailing_reports = models.BooleanField(blank=True, null=True, db_comment='24H Stat Mailing Reports')
    mass_mailing_split_contact_name = models.BooleanField(blank=True, null=True, db_comment='Split First and Last Name')
    is_newsletter_enabled = models.BooleanField(blank=True, null=True, db_comment='Is Newsletter Enabled')
    default_purchase_method = models.CharField(blank=True, null=True, db_comment='Bill Control')
    lock_confirmed_po = models.BooleanField(blank=True, null=True, db_comment='Lock Confirmed Orders')
    po_order_approval = models.BooleanField(blank=True, null=True, db_comment='Purchase Order Approval')
    group_warning_purchase = models.BooleanField(blank=True, null=True, db_comment='Purchase Warnings')
    module_account_3way_match = models.BooleanField(blank=True, null=True, db_comment='3-way matching: purchases, receptions and bills')
    module_purchase_requisition = models.BooleanField(blank=True, null=True, db_comment='Purchase Agreements')
    module_purchase_product_matrix = models.BooleanField(blank=True, null=True, db_comment='Purchase Grid Entry')
    use_po_lead = models.BooleanField(blank=True, null=True, db_comment='Security Lead Time for Purchase')
    group_send_reminder = models.BooleanField(blank=True, null=True, db_comment='Receipt Reminder')
    is_installed_sale = models.BooleanField(blank=True, null=True, db_comment='Is the Sale Module Installed')
    module_hr_presence = models.BooleanField(blank=True, null=True, db_comment='Advanced Presence Control')
    module_hr_skills = models.BooleanField(blank=True, null=True, db_comment='Skills Management')
    module_hr_homeworking = models.BooleanField(blank=True, null=True, db_comment='Remote Work')
    hr_employee_self_edit = models.BooleanField(blank=True, null=True, db_comment='Employee Editing')
    hr_expense_alias_prefix = models.CharField(blank=True, null=True, db_comment='Default Alias Name for Expenses')
    hr_expense_use_mailgateway = models.BooleanField(blank=True, null=True, db_comment='Let your employees record expenses by email')
    module_hr_payroll_expense = models.BooleanField(blank=True, null=True, db_comment='Reimburse Expenses in Payslip')
    module_hr_expense_extract = models.BooleanField(blank=True, null=True, db_comment='Send bills to OCR to generate expenses')
    use_manufacturing_lead = models.BooleanField(blank=True, null=True, db_comment='Default Manufacturing Lead Time')
    group_mrp_byproducts = models.BooleanField(blank=True, null=True, db_comment='By-Products')
    module_mrp_mps = models.BooleanField(blank=True, null=True, db_comment='Master Production Schedule')
    module_mrp_plm = models.BooleanField(blank=True, null=True, db_comment='Product Lifecycle Management (PLM)')
    module_mrp_subcontracting = models.BooleanField(blank=True, null=True, db_comment='Subcontracting')
    group_mrp_routings = models.BooleanField(blank=True, null=True, db_comment='MRP Work Orders')
    group_unlocked_by_default = models.BooleanField(blank=True, null=True, db_comment='Unlock Manufacturing Orders')
    group_mrp_reception_report = models.BooleanField(blank=True, null=True, db_comment='Allocation Report for Manufacturing Orders')
    group_mrp_workorder_dependencies = models.BooleanField(blank=True, null=True, db_comment='Work Order Dependencies')
    google_maps_static_api_key = models.CharField(blank=True, null=True, db_comment='Google Maps API key')
    google_maps_static_api_secret = models.CharField(blank=True, null=True, db_comment='Google Maps API secret')
    module_event_sale = models.BooleanField(blank=True, null=True, db_comment='Tickets with Sale')
    module_pos_event = models.BooleanField(blank=True, null=True, db_comment='Tickets with PoS')
    module_website_event_meet = models.BooleanField(blank=True, null=True, db_comment='Discussion Rooms')
    module_website_event_track = models.BooleanField(blank=True, null=True, db_comment='Tracks and Agenda')
    module_website_event_track_live = models.BooleanField(blank=True, null=True, db_comment='Live Mode')
    module_website_event_track_quiz = models.BooleanField(blank=True, null=True, db_comment='Quiz on Tracks')
    module_website_event_exhibitor = models.BooleanField(blank=True, null=True, db_comment='Advanced Sponsors')
    use_event_barcode = models.BooleanField(blank=True, null=True, db_comment='Use Event Barcode')
    module_website_event_sale = models.BooleanField(blank=True, null=True, db_comment='Online Ticketing')
    module_event_booth = models.BooleanField(blank=True, null=True, db_comment='Booth Management')
    use_google_maps_static_api = models.BooleanField(blank=True, null=True, db_comment='Google Maps static API')

    class Meta:
        managed = False
        db_table = 'res_config_settings'
        db_table_comment = 'Config Settings'


class ResCountry(models.Model):
    address_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True, db_comment='Input View')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    phone_code = models.IntegerField(blank=True, null=True, db_comment='Country Calling Code')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='rescountry_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    code = models.CharField(unique=True, max_length=2, db_comment='Country Code')
    name_position = models.CharField(blank=True, null=True, db_comment='Customer Name Position')
    name = models.JSONField(unique=True, db_comment='Country Name')
    vat_label = models.JSONField(blank=True, null=True, db_comment='Vat Label')
    address_format = models.TextField(blank=True, null=True, db_comment='Layout in Reports')
    state_required = models.BooleanField(blank=True, null=True, db_comment='State Required')
    zip_required = models.BooleanField(blank=True, null=True, db_comment='Zip Required')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_country'
        db_table_comment = 'Country'


class ResCountryGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='rescountrygroup_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_country_group'
        db_table_comment = 'Country Group'


class ResCountryGroupPricelistRel(models.Model):
    pk = models.CompositePrimaryKey('pricelist_id', 'res_country_group_id')
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING)
    res_country_group = models.ForeignKey(ResCountryGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_group_pricelist_rel'
        db_table_comment = 'RELATION BETWEEN product_pricelist AND res_country_group'


class ResCountryResCountryGroupRel(models.Model):
    pk = models.CompositePrimaryKey('res_country_id', 'res_country_group_id')
    res_country = models.ForeignKey(ResCountry, models.DO_NOTHING)
    res_country_group = models.ForeignKey(ResCountryGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_res_country_group_rel'
        db_table_comment = 'RELATION BETWEEN res_country AND res_country_group'


class ResCountryState(models.Model):
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, db_comment='Country')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='rescountrystate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='State Name')
    code = models.CharField(db_comment='State Code')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    l10n_in_tin = models.CharField(max_length=2, blank=True, null=True, db_comment='TIN Number')

    class Meta:
        managed = False
        db_table = 'res_country_state'
        unique_together = (('country', 'code'),)
        db_table_comment = 'Country state'


class ResCurrency(models.Model):
    name = models.CharField(unique=True)
    symbol = models.CharField()
    iso_numeric = models.IntegerField(blank=True, null=True, db_comment='Currency numeric code.')
    decimal_places = models.IntegerField(blank=True, null=True, db_comment='Decimal Places')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='rescurrency_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    full_name = models.CharField(blank=True, null=True, db_comment='Name')
    position = models.CharField(blank=True, null=True, db_comment='Symbol Position')
    currency_unit_label = models.JSONField(blank=True, null=True, db_comment='Currency Unit')
    currency_subunit_label = models.JSONField(blank=True, null=True, db_comment='Currency Subunit')
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Rounding Factor')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_currency'


class ResCurrencyRate(models.Model):
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, db_comment='Currency')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='rescurrencyrate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.DateField(db_comment='Date')
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Technical Rate')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_currency_rate'
        unique_together = (('name', 'currency', 'company'),)
        db_table_comment = 'Currency Rate'


class ResDeviceLog(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='User')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='resdevicelog_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='resdevicelog_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    session_identifier = models.CharField(db_comment='Session Identifier')
    platform = models.CharField(blank=True, null=True, db_comment='Platform')
    browser = models.CharField(blank=True, null=True, db_comment='Browser')
    ip_address = models.CharField(blank=True, null=True, db_comment='IP Address')
    country = models.CharField(blank=True, null=True, db_comment='Country')
    city = models.CharField(blank=True, null=True, db_comment='City')
    device_type = models.CharField(blank=True, null=True, db_comment='Device Type')
    revoked = models.BooleanField(blank=True, null=True, db_comment='Revoked')
    first_activity = models.DateTimeField(blank=True, null=True, db_comment='First Activity')
    last_activity = models.DateTimeField(blank=True, null=True, db_comment='Last Activity')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_device_log'
        db_table_comment = 'Device Log'


class ResGroups(models.Model):
    name = models.JSONField()
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, blank=True, null=True, db_comment='Application')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='resgroups_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    comment = models.JSONField(blank=True, null=True, db_comment='Comment')
    share = models.BooleanField(blank=True, null=True, db_comment='Share Group')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    api_key_duration = models.FloatField(blank=True, null=True, db_comment='API Keys maximum duration days')

    class Meta:
        managed = False
        db_table = 'res_groups'
        unique_together = (('category', 'name'),)


class ResGroupsImpliedRel(models.Model):
    pk = models.CompositePrimaryKey('gid', 'hid')
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')
    hid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='hid', related_name='resgroupsimpliedrel_hid_set')

    class Meta:
        managed = False
        db_table = 'res_groups_implied_rel'
        db_table_comment = 'RELATION BETWEEN res_groups AND res_groups'


class ResGroupsReportRel(models.Model):
    pk = models.CompositePrimaryKey('uid', 'gid')
    uid = models.ForeignKey(IrActReportXml, models.DO_NOTHING, db_column='uid')
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_report_rel'
        db_table_comment = 'RELATION BETWEEN ir_act_report_xml AND res_groups'


class ResGroupsSpreadsheetDashboardRel(models.Model):
    pk = models.CompositePrimaryKey('spreadsheet_dashboard_id', 'res_groups_id')
    spreadsheet_dashboard = models.ForeignKey('SpreadsheetDashboard', models.DO_NOTHING)
    res_groups = models.ForeignKey(ResGroups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_groups_spreadsheet_dashboard_rel'
        db_table_comment = 'RELATION BETWEEN spreadsheet_dashboard AND res_groups'


class ResGroupsUsersRel(models.Model):
    pk = models.CompositePrimaryKey('gid', 'uid')
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')
    uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'res_groups_users_rel'
        db_table_comment = 'RELATION BETWEEN res_groups AND res_users'


class ResGroupsWebsiteMenuRel(models.Model):
    pk = models.CompositePrimaryKey('website_menu_id', 'res_groups_id')
    website_menu = models.ForeignKey('WebsiteMenu', models.DO_NOTHING)
    res_groups = models.ForeignKey(ResGroups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_groups_website_menu_rel'
        db_table_comment = 'RELATION BETWEEN website_menu AND res_groups'


class ResLang(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='reslang_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(unique=True, db_comment='Name')
    code = models.CharField(unique=True, db_comment='Locale Code')
    iso_code = models.CharField(blank=True, null=True, db_comment='ISO code')
    url_code = models.CharField(unique=True, db_comment='URL Code')
    direction = models.CharField(db_comment='Direction')
    date_format = models.CharField(db_comment='Date Format')
    time_format = models.CharField(db_comment='Time Format')
    short_time_format = models.CharField(db_comment='Short Time Format')
    week_start = models.CharField(db_comment='First Day of Week')
    grouping = models.CharField(db_comment='Separator Format')
    decimal_point = models.CharField(db_comment='Decimal Separator')
    thousands_sep = models.CharField(blank=True, null=True, db_comment='Thousands Separator')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_lang'
        db_table_comment = 'Languages'


class ResLangInstallRel(models.Model):
    pk = models.CompositePrimaryKey('language_wizard_id', 'lang_id')
    language_wizard = models.ForeignKey(BaseLanguageInstall, models.DO_NOTHING)
    lang = models.ForeignKey(ResLang, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_lang_install_rel'
        db_table_comment = 'RELATION BETWEEN base_language_install AND res_lang'


class ResLangResUsersSettingsRel(models.Model):
    pk = models.CompositePrimaryKey('res_users_settings_id', 'res_lang_id')
    res_users_settings = models.ForeignKey('ResUsersSettings', models.DO_NOTHING)
    res_lang = models.ForeignKey(ResLang, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_lang_res_users_settings_rel'
        db_table_comment = 'RELATION BETWEEN res_users_settings AND res_lang'


class ResPartner(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, db_column='title', blank=True, null=True, db_comment='Title')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Related Company')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, db_comment='Salesperson')
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, blank=True, null=True, db_comment='State')
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    industry = models.ForeignKey('ResPartnerIndustry', models.DO_NOTHING, blank=True, null=True, db_comment='Industry')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    commercial_partner = models.ForeignKey('self', models.DO_NOTHING, related_name='respartner_commercial_partner_set', blank=True, null=True, db_comment='Commercial Entity')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', related_name='respartner_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='respartner_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    complete_name = models.CharField(blank=True, null=True, db_comment='Complete Name')
    ref = models.CharField(blank=True, null=True, db_comment='Reference')
    lang = models.CharField(blank=True, null=True, db_comment='Language')
    tz = models.CharField(blank=True, null=True, db_comment='Timezone')
    vat = models.CharField(blank=True, null=True, db_comment='Tax ID')
    company_registry = models.CharField(blank=True, null=True, db_comment='Company ID')
    website = models.CharField(blank=True, null=True, db_comment='Website Link')
    function = models.CharField(blank=True, null=True, db_comment='Job Position')
    type = models.CharField(blank=True, null=True, db_comment='Address Type')
    street = models.CharField(blank=True, null=True, db_comment='Street')
    street2 = models.CharField(blank=True, null=True, db_comment='Street2')
    zip = models.CharField(blank=True, null=True, db_comment='Zip')
    city = models.CharField(blank=True, null=True, db_comment='City')
    email = models.CharField(blank=True, null=True, db_comment='Email')
    phone = models.CharField(blank=True, null=True, db_comment='Phone')
    mobile = models.CharField(blank=True, null=True, db_comment='Mobile')
    commercial_company_name = models.CharField(blank=True, null=True, db_comment='Company Name Entity')
    company_name = models.CharField(blank=True, null=True, db_comment='Company Name')
    barcode = models.JSONField(blank=True, null=True, db_comment='Barcode')
    comment = models.TextField(blank=True, null=True, db_comment='Notes')
    partner_latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Geo Latitude')
    partner_longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Geo Longitude')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    employee = models.BooleanField(blank=True, null=True, db_comment='Employee')
    is_company = models.BooleanField(blank=True, null=True, db_comment='Is a Company')
    partner_share = models.BooleanField(blank=True, null=True, db_comment='Share Partner')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    message_bounce = models.IntegerField(blank=True, null=True, db_comment='Bounce')
    email_normalized = models.CharField(blank=True, null=True, db_comment='Normalized Email')
    signup_type = models.CharField(blank=True, null=True, db_comment='Signup Token Type')
    specific_property_product_pricelist = models.JSONField(blank=True, null=True, db_comment='Specific Property Product Pricelist')
    partner_gid = models.IntegerField(blank=True, null=True, db_comment='Company database ID')
    additional_info = models.CharField(blank=True, null=True, db_comment='Additional info')
    phone_sanitized = models.CharField(blank=True, null=True, db_comment='Sanitized Number')
    invoice_template_pdf_report = models.ForeignKey(IrActReportXml, models.DO_NOTHING, blank=True, null=True, db_comment='Invoice template')
    supplier_rank = models.IntegerField(blank=True, null=True, db_comment='Supplier Rank')
    customer_rank = models.IntegerField(blank=True, null=True, db_comment='Customer Rank')
    invoice_warn = models.CharField(blank=True, null=True, db_comment='Invoice')
    autopost_bills = models.CharField(db_comment='Auto-post bills')
    credit_limit = models.JSONField(blank=True, null=True, db_comment='Credit Limit')
    property_account_payable_id = models.JSONField(blank=True, null=True, db_comment='Account Payable')
    property_account_receivable_id = models.JSONField(blank=True, null=True, db_comment='Account Receivable')
    property_account_position_id = models.JSONField(blank=True, null=True, db_comment='Fiscal Position')
    property_payment_term_id = models.JSONField(blank=True, null=True, db_comment='Customer Payment Terms')
    property_supplier_payment_term_id = models.JSONField(blank=True, null=True, db_comment='Vendor Payment Terms')
    trust = models.JSONField(blank=True, null=True, db_comment='Degree of trust you have in this debtor')
    ignore_abnormal_invoice_date = models.JSONField(blank=True, null=True, db_comment='Ignore Abnormal Invoice Date')
    ignore_abnormal_invoice_amount = models.JSONField(blank=True, null=True, db_comment='Ignore Abnormal Invoice Amount')
    invoice_sending_method = models.JSONField(blank=True, null=True, db_comment='Invoice sending')
    invoice_edi_format_store = models.JSONField(blank=True, null=True, db_comment='Invoice Edi Format Store')
    property_outbound_payment_method_line_id = models.JSONField(blank=True, null=True, db_comment='Property Outbound Payment Method Line')
    property_inbound_payment_method_line_id = models.JSONField(blank=True, null=True, db_comment='Property Inbound Payment Method Line')
    invoice_warn_msg = models.TextField(blank=True, null=True, db_comment='Message for Invoice')
    debit_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Payable Limit')
    website_0 = models.ForeignKey('Website', models.DO_NOTHING, db_column='website_id', blank=True, null=True, db_comment='Website')  # Field renamed because of name conflict.
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')
    peppol_endpoint = models.CharField(blank=True, null=True, db_comment='Peppol Endpoint')
    peppol_eas = models.CharField(blank=True, null=True, db_comment='Peppol e-address (EAS)')
    vies_valid = models.BooleanField(blank=True, null=True, db_comment='Intra-Community Valid')
    l10n_in_gst_treatment = models.CharField(blank=True, null=True, db_comment='GST Treatment')
    l10n_in_pan = models.CharField(blank=True, null=True, db_comment='PAN')
    sale_warn = models.CharField(blank=True, null=True, db_comment='Sales Warnings')
    sale_warn_msg = models.TextField(blank=True, null=True, db_comment='Message for Sales Order')
    property_delivery_carrier_id = models.JSONField(blank=True, null=True, db_comment='Delivery Method')
    picking_warn = models.CharField(blank=True, null=True, db_comment='Stock Picking')
    property_stock_customer = models.JSONField(blank=True, null=True, db_comment='Customer Location')
    property_stock_supplier = models.JSONField(blank=True, null=True, db_comment='Vendor Location')
    picking_warn_msg = models.TextField(blank=True, null=True, db_comment='Message for Stock Picking')
    followup_status = models.CharField(blank=True, null=True, db_comment='Followup status')
    active_limit = models.BooleanField(blank=True, null=True, db_comment='Active Credit Limit')
    warning_stage = models.FloatField(blank=True, null=True, db_comment='Warning Amount')
    blocking_stage = models.FloatField(blank=True, null=True, db_comment='Blocking Amount')
    buyer = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='respartner_buyer_set', blank=True, null=True, db_comment='Buyer')
    purchase_warn = models.CharField(blank=True, null=True, db_comment='Purchase Order Warning')
    property_purchase_currency_id = models.JSONField(blank=True, null=True, db_comment='Supplier Currency')
    receipt_reminder_email = models.JSONField(blank=True, null=True, db_comment='Receipt Reminder')
    reminder_date_before_receipt = models.JSONField(blank=True, null=True, db_comment='Days Before Receipt')
    purchase_warn_msg = models.TextField(blank=True, null=True, db_comment='Message for Purchase Order')
    website_meta_og_img = models.CharField(blank=True, null=True, db_comment='Website opengraph image')
    website_meta_title = models.JSONField(blank=True, null=True, db_comment='Website meta title')
    website_meta_description = models.JSONField(blank=True, null=True, db_comment='Website meta description')
    website_meta_keywords = models.JSONField(blank=True, null=True, db_comment='Website meta keywords')
    seo_name = models.JSONField(blank=True, null=True, db_comment='Seo name')
    website_description = models.JSONField(blank=True, null=True, db_comment='Website Partner Full Description')
    website_short_description = models.JSONField(blank=True, null=True, db_comment='Website Partner Short Description')

    class Meta:
        managed = False
        db_table = 'res_partner'


class ResPartnerAutocompleteSync(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='respartnerautocompletesync_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    synched = models.BooleanField(blank=True, null=True, db_comment='Is synched')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_partner_autocomplete_sync'
        db_table_comment = 'Partner Autocomplete Sync'


class ResPartnerBank(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, db_comment='Account Holder')
    bank = models.ForeignKey(ResBank, models.DO_NOTHING, blank=True, null=True, db_comment='Bank')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='respartnerbank_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    acc_number = models.CharField(db_comment='Account Number')
    sanitized_acc_number = models.CharField(blank=True, null=True, db_comment='Sanitized Account Number')
    acc_holder_name = models.CharField(blank=True, null=True, db_comment='Account Holder Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    allow_out_payment = models.BooleanField(blank=True, null=True, db_comment='Send Money')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    has_iban_warning = models.BooleanField(blank=True, null=True, db_comment='Has Iban Warning')
    has_money_transfer_warning = models.BooleanField(blank=True, null=True, db_comment='Has Money Transfer Warning')

    class Meta:
        managed = False
        db_table = 'res_partner_bank'
        unique_together = (('sanitized_acc_number', 'partner'),)
        db_table_comment = 'Bank Accounts'


class ResPartnerCategory(models.Model):
    color = models.IntegerField(blank=True, null=True, db_comment='Color')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Category')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='respartnercategory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    parent_path = models.CharField(blank=True, null=True, db_comment='Parent Path')
    name = models.JSONField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_partner_category'
        db_table_comment = 'Partner Tags'


class ResPartnerIndustry(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='respartnerindustry_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(blank=True, null=True, db_comment='Name')
    full_name = models.JSONField(blank=True, null=True, db_comment='Full Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_partner_industry'
        db_table_comment = 'Industry'


class ResPartnerResPartnerCategoryRel(models.Model):
    pk = models.CompositePrimaryKey('category_id', 'partner_id')
    category = models.ForeignKey(ResPartnerCategory, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_res_partner_category_rel'
        db_table_comment = 'RELATION BETWEEN res_partner_category AND res_partner'


class ResPartnerTitle(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', related_name='respartnertitle_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Title')
    shortcut = models.JSONField(blank=True, null=True, db_comment='Abbreviation')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_partner_title'
        db_table_comment = 'Partner Title'


class ResUsers(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    login = models.CharField()
    password = models.CharField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True, db_comment='Home Action')
    create_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='write_uid', related_name='resusers_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    signature = models.TextField(blank=True, null=True, db_comment='Email Signature')
    share = models.BooleanField(blank=True, null=True, db_comment='Share User')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    totp_secret = models.CharField(blank=True, null=True)
    tour_enabled = models.BooleanField(blank=True, null=True, db_comment='Onboarding')
    notification_type = models.CharField(db_comment='Notification')
    odoobot_state = models.CharField(blank=True, null=True, db_comment='OdooBot Status')
    odoobot_failed = models.BooleanField(blank=True, null=True, db_comment='Odoobot Failed')
    sale_team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True, db_comment='User Sales Team')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    property_warehouse_id = models.JSONField(blank=True, null=True, db_comment='Default Warehouse')

    class Meta:
        managed = False
        db_table = 'res_users'
        unique_together = (('login', 'website'),)


class ResUsersApikeys(models.Model):
    name = models.CharField()
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)
    scope = models.CharField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    index = models.CharField(max_length=8, blank=True, null=True)
    key = models.CharField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_apikeys'


class ResUsersApikeysDescription(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resusersapikeysdescription_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Description')
    duration = models.CharField(db_comment='Duration')
    expiration_date = models.DateTimeField(blank=True, null=True, db_comment='Expiration Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_users_apikeys_description'
        db_table_comment = 'API Key Description'


class ResUsersDeletion(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True, db_comment='User')
    user_id_int = models.IntegerField(blank=True, null=True, db_comment='User Id')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='resusersdeletion_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resusersdeletion_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    state = models.CharField(db_comment='State')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_users_deletion'
        db_table_comment = 'Users Deletion Request'


class ResUsersIdentitycheck(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resusersidentitycheck_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    request = models.CharField(blank=True, null=True, db_comment='Request')
    auth_method = models.CharField(blank=True, null=True, db_comment='Auth Method')
    password = models.CharField(blank=True, null=True, db_comment='Password')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_users_identitycheck'
        db_table_comment = 'Password Check Wizard'


class ResUsersLog(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resuserslog_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'res_users_log'
        db_table_comment = 'Users Log'


class ResUsersSettings(models.Model):
    user = models.OneToOneField(ResUsers, models.DO_NOTHING, db_comment='User')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='resuserssettings_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resuserssettings_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    voice_active_duration = models.IntegerField(blank=True, null=True, db_comment='Duration of voice activity in ms')
    push_to_talk_key = models.CharField(blank=True, null=True, db_comment='Push-To-Talk shortcut')
    channel_notifications = models.CharField(blank=True, null=True, db_comment='Channel Notifications')
    is_discuss_sidebar_category_channel_open = models.BooleanField(blank=True, null=True, db_comment='Is discuss sidebar category channel open?')
    is_discuss_sidebar_category_chat_open = models.BooleanField(blank=True, null=True, db_comment='Is discuss sidebar category chat open?')
    use_push_to_talk = models.BooleanField(blank=True, null=True, db_comment='Use the push to talk feature')
    mute_until_dt = models.DateTimeField(blank=True, null=True, db_comment='Mute notifications until')
    livechat_username = models.CharField(blank=True, null=True, db_comment='Livechat Username')

    class Meta:
        managed = False
        db_table = 'res_users_settings'
        db_table_comment = 'User Settings'


class ResUsersSettingsVolumes(models.Model):
    user_setting = models.ForeignKey(ResUsersSettings, models.DO_NOTHING, db_comment='User Setting')
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    guest = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='resuserssettingsvolumes_guest_set', blank=True, null=True, db_comment='Guest')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resuserssettingsvolumes_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    volume = models.FloatField(blank=True, null=True, db_comment='Volume')

    class Meta:
        managed = False
        db_table = 'res_users_settings_volumes'
        unique_together = (('user_setting', 'guest'), ('user_setting', 'partner'),)
        db_table_comment = 'User Settings Volumes'


class ResUsersWebTourTourRel(models.Model):
    pk = models.CompositePrimaryKey('web_tour_tour_id', 'res_users_id')
    web_tour_tour = models.ForeignKey('WebTourTour', models.DO_NOTHING)
    res_users = models.ForeignKey(ResUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_users_web_tour_tour_rel'
        db_table_comment = 'RELATION BETWEEN web_tour_tour AND res_users'


class ResetViewArchWizard(models.Model):
    view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True, db_comment='View')
    compare_view = models.ForeignKey(IrUiView, models.DO_NOTHING, related_name='resetviewarchwizard_compare_view_set', blank=True, null=True, db_comment='Compare To View')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resetviewarchwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    reset_mode = models.CharField(db_comment='Reset Mode')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'reset_view_arch_wizard'
        db_table_comment = 'Reset View Architecture Wizard'


class ResourceCalendar(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resourcecalendar_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    tz = models.CharField(db_comment='Timezone')
    hours_per_day = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Average Hour per Day')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    two_weeks_calendar = models.BooleanField(blank=True, null=True, db_comment='Calendar in 2 weeks mode')
    flexible_hours = models.BooleanField(blank=True, null=True, db_comment='Flexible Hours')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    full_time_required_hours = models.FloatField(blank=True, null=True, db_comment='Company Full Time')

    class Meta:
        managed = False
        db_table = 'resource_calendar'
        db_table_comment = 'Resource Working Time'


class ResourceCalendarAttendance(models.Model):
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING, db_comment="Resource's Calendar")
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, blank=True, null=True, db_comment='Resource')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resourcecalendarattendance_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    dayofweek = models.CharField(db_comment='Day of Week')
    day_period = models.CharField(db_comment='Day Period')
    week_type = models.CharField(blank=True, null=True, db_comment='Week Number')
    display_type = models.CharField(blank=True, null=True, db_comment='Display Type')
    date_from = models.DateField(blank=True, null=True, db_comment='Starting Date')
    date_to = models.DateField(blank=True, null=True, db_comment='End Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    hour_from = models.FloatField(db_comment='Work from')
    hour_to = models.FloatField(db_comment='Work to')
    duration_days = models.FloatField(blank=True, null=True, db_comment='Duration (days)')

    class Meta:
        managed = False
        db_table = 'resource_calendar_attendance'
        db_table_comment = 'Work Detail'


class ResourceCalendarLeaves(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING, blank=True, null=True, db_comment='Working Hours')
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, blank=True, null=True, db_comment='Resource')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resourcecalendarleaves_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Reason')
    time_type = models.CharField(blank=True, null=True, db_comment='Time Type')
    date_from = models.DateTimeField(db_comment='Start Date')
    date_to = models.DateTimeField(db_comment='End Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'resource_calendar_leaves'
        db_table_comment = 'Resource Time Off Detail'


class ResourceResource(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True, db_comment='User')
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING, blank=True, null=True, db_comment='Working Time')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='resourceresource_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='resourceresource_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    resource_type = models.CharField(db_comment='Type')
    tz = models.CharField(db_comment='Timezone')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    time_efficiency = models.FloatField(db_comment='Efficiency Factor')

    class Meta:
        managed = False
        db_table = 'resource_resource'
        db_table_comment = 'Resources'


class RuleGroupRel(models.Model):
    pk = models.CompositePrimaryKey('rule_group_id', 'group_id')
    rule_group = models.ForeignKey(IrRule, models.DO_NOTHING)
    group = models.ForeignKey(ResGroups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rule_group_rel'
        db_table_comment = 'RELATION BETWEEN ir_rule AND res_groups'


class SaleAdvancePaymentInv(models.Model):
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='saleadvancepaymentinv_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    advance_payment_method = models.CharField(db_comment='Create Invoice')
    fixed_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Down Payment Amount (Fixed)')
    deduct_down_payments = models.BooleanField(blank=True, null=True, db_comment='Deduct down payments')
    consolidated_billing = models.BooleanField(blank=True, null=True, db_comment='Consolidated Billing')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    amount = models.FloatField(blank=True, null=True, db_comment='Down Payment')

    class Meta:
        managed = False
        db_table = 'sale_advance_payment_inv'
        db_table_comment = 'Sales Advance Payment Invoice'


class SaleAdvancePaymentInvSaleOrderRel(models.Model):
    pk = models.CompositePrimaryKey('sale_advance_payment_inv_id', 'sale_order_id')
    sale_advance_payment_inv = models.ForeignKey(SaleAdvancePaymentInv, models.DO_NOTHING)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_advance_payment_inv_sale_order_rel'
        db_table_comment = 'RELATION BETWEEN sale_advance_payment_inv AND sale_order'


class SaleMassCancelOrders(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='salemasscancelorders_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sale_mass_cancel_orders'
        db_table_comment = 'Cancel multiple quotations'


class SaleOrder(models.Model):
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True, db_comment='Campaign')
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True, db_comment='Source')
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True, db_comment='Medium')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, db_comment='Customer')
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Invoicing Journal')
    partner_invoice = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='saleorder_partner_invoice_set', db_comment='Invoice Address')
    partner_shipping = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='saleorder_partner_shipping_set', db_comment='Delivery Address')
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True, db_comment='Fiscal Position')
    payment_term = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING, blank=True, null=True, db_comment='Payment Terms')
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING, blank=True, null=True, db_comment='Pricelist')
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True, db_comment='Salesperson')
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True, db_comment='Sales Team')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='saleorder_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='saleorder_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    access_token = models.CharField(blank=True, null=True, db_comment='Security Token')
    name = models.CharField(db_comment='Order Reference')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    client_order_ref = models.CharField(blank=True, null=True, db_comment='Customer Reference')
    origin = models.CharField(blank=True, null=True, db_comment='Source Document')
    reference = models.CharField(blank=True, null=True, db_comment='Payment Ref.')
    signed_by = models.CharField(blank=True, null=True, db_comment='Signed By')
    invoice_status = models.CharField(blank=True, null=True, db_comment='Invoice Status')
    validity_date = models.DateField(blank=True, null=True, db_comment='Expiration')
    note = models.TextField(blank=True, null=True, db_comment='Terms and conditions')
    currency_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Currency Rate')
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Untaxed Amount')
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Taxes')
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total')
    locked = models.BooleanField(blank=True, null=True, db_comment='Locked')
    require_signature = models.BooleanField(blank=True, null=True, db_comment='Online signature')
    require_payment = models.BooleanField(blank=True, null=True, db_comment='Online payment')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Creation Date')
    commitment_date = models.DateTimeField(blank=True, null=True, db_comment='Delivery Date')
    date_order = models.DateTimeField(db_comment='Order Date')
    signed_on = models.DateTimeField(blank=True, null=True, db_comment='Signed On')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    prepayment_percent = models.FloatField(blank=True, null=True, db_comment='Prepayment percentage')
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING, blank=True, null=True, db_comment='Delivery Method')
    delivery_message = models.CharField(blank=True, null=True, db_comment='Delivery Message')
    pickup_location_data = models.JSONField(blank=True, null=True, db_comment='Pickup Location Data')
    recompute_delivery_price = models.BooleanField(blank=True, null=True, db_comment='Delivery cost should be recomputed')
    shipping_weight = models.FloatField(blank=True, null=True, db_comment='Shipping Weight')
    l10n_in_reseller_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='saleorder_l10n_in_reseller_partner_set', blank=True, null=True, db_comment='Reseller')
    l10n_in_gst_treatment = models.CharField(blank=True, null=True, db_comment='GST Treatment')
    pending_email_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True, db_comment='Pending Email Template')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    shop_warning = models.CharField(blank=True, null=True, db_comment='Warning')
    cart_recovery_email_sent = models.BooleanField(blank=True, null=True, db_comment='Cart recovery email already sent')
    incoterm = models.ForeignKey(AccountIncoterms, models.DO_NOTHING, db_column='incoterm', blank=True, null=True, db_comment='Incoterm')
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True, db_comment='Warehouse')
    procurement_group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True, db_comment='Procurement Group')
    incoterm_location = models.CharField(blank=True, null=True, db_comment='Incoterm Location')
    picking_policy = models.CharField(db_comment='Shipping Policy')
    delivery_status = models.CharField(blank=True, null=True, db_comment='Delivery Status')
    effective_date = models.DateTimeField(blank=True, null=True, db_comment='Effective Date')
    has_due = models.BooleanField(blank=True, null=True, db_comment='Has due')
    is_warning = models.BooleanField(blank=True, null=True, db_comment='Is warning')
    sale_order_template = models.ForeignKey('SaleOrderTemplate', models.DO_NOTHING, blank=True, null=True)
    amount_unpaid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount To Pay In POS')
    customizable_pdf_form_fields = models.JSONField(blank=True, null=True, db_comment='Customizable PDF Form Fields')

    class Meta:
        managed = False
        db_table = 'sale_order'
        db_table_comment = 'Sales Order'


class SaleOrderCancel(models.Model):
    template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True, db_comment='Mail Template')
    author = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Author')
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING, db_comment='Sale Order')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='saleordercancel_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    lang = models.CharField(blank=True, null=True, db_comment='Language')
    subject = models.CharField(blank=True, null=True, db_comment='Subject')
    body = models.TextField(blank=True, null=True, db_comment='Contents')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sale_order_cancel'
        db_table_comment = 'Sales Order Cancel'


class SaleOrderDiscount(models.Model):
    sale_order = models.ForeignKey(SaleOrder, models.DO_NOTHING, db_comment='Sale Order')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='saleorderdiscount_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    discount_type = models.CharField(blank=True, null=True, db_comment='Discount Type')
    discount_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Amount')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    discount_percentage = models.FloatField(blank=True, null=True, db_comment='Percentage')

    class Meta:
        managed = False
        db_table = 'sale_order_discount'
        db_table_comment = 'Discount Wizard'


class SaleOrderLine(models.Model):
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING, db_comment='Order Reference')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True, db_comment='Currency')
    order_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Customer')
    salesman = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True, db_comment='Salesperson')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_column='product_uom', blank=True, null=True, db_comment='Unit of Measure')
    linked_line = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Linked Order Line')
    combo_item = models.ForeignKey(ProductComboItem, models.DO_NOTHING, blank=True, null=True, db_comment='Combo Item')
    product_packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, blank=True, null=True, db_comment='Packaging')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='saleorderline_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='saleorderline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    state = models.CharField(blank=True, null=True, db_comment='Order Status')
    display_type = models.CharField(blank=True, null=True, db_comment='Display Type')
    virtual_id = models.CharField(blank=True, null=True, db_comment='Virtual')
    linked_virtual_id = models.CharField(blank=True, null=True, db_comment='Linked Virtual')
    qty_delivered_method = models.CharField(blank=True, null=True, db_comment='Method to update delivered qty')
    invoice_status = models.CharField(blank=True, null=True, db_comment='Invoice Status')
    analytic_distribution = models.JSONField(blank=True, null=True, db_comment='Analytic Distribution')
    name = models.TextField(db_comment='Description')
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Unit Price')
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Discount (%)')
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Subtotal')
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total')
    price_reduce_taxexcl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Price Reduce Tax excl')
    price_reduce_taxinc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Price Reduce Tax incl')
    qty_delivered = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Delivery Quantity')
    qty_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Invoiced Quantity')
    qty_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Quantity To Invoice')
    untaxed_amount_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Untaxed Invoiced Amount')
    untaxed_amount_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Untaxed Amount To Invoice')
    is_downpayment = models.BooleanField(blank=True, null=True, db_comment='Is a down payment')
    is_expense = models.BooleanField(blank=True, null=True, db_comment='Is expense')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    technical_price_unit = models.FloatField(blank=True, null=True, db_comment='Technical Price Unit')
    price_tax = models.FloatField(blank=True, null=True, db_comment='Total Tax')
    product_packaging_qty = models.FloatField(blank=True, null=True, db_comment='Packaging Quantity')
    customer_lead = models.FloatField(db_comment='Lead Time')
    is_delivery = models.BooleanField(blank=True, null=True, db_comment='Is a Delivery')
    shop_warning = models.CharField(blank=True, null=True, db_comment='Warning')
    route = models.ForeignKey('StockRoute', models.DO_NOTHING, blank=True, null=True, db_comment='Route')
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True, db_comment='Warehouse')
    event = models.ForeignKey(EventEvent, models.DO_NOTHING, blank=True, null=True, db_comment='Event')
    event_ticket = models.ForeignKey(EventEventTicket, models.DO_NOTHING, blank=True, null=True, db_comment='Ticket Type')

    class Meta:
        managed = False
        db_table = 'sale_order_line'
        db_table_comment = 'Sales Order Line'


class SaleOrderLineInvoiceRel(models.Model):
    pk = models.CompositePrimaryKey('invoice_line_id', 'order_line_id')
    invoice_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)
    order_line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_line_invoice_rel'
        db_table_comment = 'RELATION BETWEEN account_move_line AND sale_order_line'


class SaleOrderLineProductDocumentRel(models.Model):
    pk = models.CompositePrimaryKey('sale_order_line_id', 'product_document_id')
    sale_order_line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING)
    product_document = models.ForeignKey(ProductDocument, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_line_product_document_rel'
        db_table_comment = 'RELATION BETWEEN sale_order_line AND product_document'


class SaleOrderMassCancelWizardRel(models.Model):
    pk = models.CompositePrimaryKey('sale_mass_cancel_orders_id', 'sale_order_id')
    sale_mass_cancel_orders = models.ForeignKey(SaleMassCancelOrders, models.DO_NOTHING)
    sale_order = models.ForeignKey(SaleOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_mass_cancel_wizard_rel'
        db_table_comment = 'RELATION BETWEEN sale_mass_cancel_orders AND sale_order'


class SaleOrderOption(models.Model):
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING, blank=True, null=True, db_comment='Sales Order Reference')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING, blank=True, null=True, db_comment='Line')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Unit of Measure')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='saleorderoption_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.TextField(db_comment='Description')
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Unit Price')
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Discount (%)')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sale_order_option'
        db_table_comment = 'Sale Options'


class SaleOrderTagRel(models.Model):
    pk = models.CompositePrimaryKey('order_id', 'tag_id')
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING)
    tag = models.ForeignKey(CrmTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_tag_rel'
        db_table_comment = 'RELATION BETWEEN sale_order AND crm_tag'


class SaleOrderTemplate(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True, db_comment='Confirmation Mail')
    number_of_days = models.IntegerField(blank=True, null=True, db_comment='Quotation Duration')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='saleordertemplate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Quotation Template')
    note = models.JSONField(blank=True, null=True, db_comment='Terms and conditions')
    journal_id = models.JSONField(blank=True, null=True, db_comment='Invoicing Journal')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    require_signature = models.BooleanField(blank=True, null=True, db_comment='Online Signature')
    require_payment = models.BooleanField(blank=True, null=True, db_comment='Online Payment')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    prepayment_percent = models.FloatField(blank=True, null=True, db_comment='Prepayment percentage')

    class Meta:
        managed = False
        db_table = 'sale_order_template'
        db_table_comment = 'Quotation Template'


class SaleOrderTemplateLine(models.Model):
    sale_order_template = models.ForeignKey(SaleOrderTemplate, models.DO_NOTHING, db_comment='Quotation Template Reference')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True, db_comment='Unit of Measure')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='saleordertemplateline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    display_type = models.CharField(blank=True, null=True, db_comment='Display Type')
    name = models.JSONField(blank=True, null=True, db_comment='Description')
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sale_order_template_line'
        db_table_comment = 'Quotation Template Line'


class SaleOrderTemplateOption(models.Model):
    sale_order_template = models.ForeignKey(SaleOrderTemplate, models.DO_NOTHING, db_comment='Quotation Template Reference')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Unit of Measure')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='saleordertemplateoption_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Description')
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sale_order_template_option'
        db_table_comment = 'Quotation Template Option'


class SaleOrderTransactionRel(models.Model):
    pk = models.CompositePrimaryKey('transaction_id', 'sale_order_id')
    transaction = models.ForeignKey(PaymentTransaction, models.DO_NOTHING)
    sale_order = models.ForeignKey(SaleOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_transaction_rel'
        db_table_comment = 'RELATION BETWEEN payment_transaction AND sale_order'


class SalePaymentProviderOnboardingWizard(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='salepaymentprovideronboardingwizard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    payment_method = models.CharField(blank=True, null=True, db_comment='Payment Method')
    paypal_email_account = models.CharField(blank=True, null=True, db_comment='Email')
    manual_name = models.CharField(blank=True, null=True, db_comment='Method')
    journal_name = models.CharField(blank=True, null=True, db_comment='Bank Name')
    acc_number = models.CharField(blank=True, null=True, db_comment='Account Number')
    manual_post_msg = models.TextField(blank=True, null=True, db_comment='Payment Instructions')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sale_payment_provider_onboarding_wizard'
        db_table_comment = 'Sale Payment provider onboarding wizard'


class SalePdfFormField(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='salepdfformfield_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Form Field Name')
    document_type = models.CharField(db_comment='Document Type')
    path = models.CharField(blank=True, null=True, db_comment='Path')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sale_pdf_form_field'
        unique_together = (('name', 'document_type'),)
        db_table_comment = 'Form fields of inside quotation documents.'


class ScheduledMessageAttachmentRel(models.Model):
    pk = models.CompositePrimaryKey('scheduled_message_id', 'attachment_id')
    scheduled_message = models.ForeignKey(MailScheduledMessage, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scheduled_message_attachment_rel'
        db_table_comment = 'RELATION BETWEEN mail_scheduled_message AND ir_attachment'


class SmsAccountCode(models.Model):
    account = models.ForeignKey(IapAccount, models.DO_NOTHING, db_comment='Account')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smsaccountcode_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    verification_code = models.CharField(db_comment='Verification Code')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_account_code'
        db_table_comment = 'SMS Account Verification Code Wizard'


class SmsAccountPhone(models.Model):
    account = models.ForeignKey(IapAccount, models.DO_NOTHING, db_comment='Account')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smsaccountphone_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    phone_number = models.CharField(db_comment='Phone Number')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_account_phone'
        db_table_comment = 'SMS Account Registration Phone Number Wizard'


class SmsAccountSender(models.Model):
    account = models.ForeignKey(IapAccount, models.DO_NOTHING, db_comment='Account')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smsaccountsender_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    sender_name = models.CharField(blank=True, null=True, db_comment='Sender Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_account_sender'
        db_table_comment = 'SMS Account Sender Name Wizard'


class SmsComposer(models.Model):
    res_id = models.IntegerField(blank=True, null=True, db_comment='Document ID')
    template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True, db_comment='Use Template')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smscomposer_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    composition_mode = models.CharField(db_comment='Composition Mode')
    res_model = models.CharField(blank=True, null=True, db_comment='Document Model Name')
    res_ids = models.CharField(blank=True, null=True, db_comment='Document IDs')
    recipient_single_number_itf = models.CharField(blank=True, null=True, db_comment='Recipient Number')
    number_field_name = models.CharField(blank=True, null=True, db_comment='Number Field')
    numbers = models.CharField(blank=True, null=True, db_comment='Recipients (Numbers)')
    body = models.TextField(db_comment='Message')
    mass_keep_log = models.BooleanField(blank=True, null=True, db_comment='Keep a note on document')
    mass_force_send = models.BooleanField(blank=True, null=True, db_comment='Send directly')
    mass_use_blacklist = models.BooleanField(blank=True, null=True, db_comment='Use blacklist')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_composer'
        db_table_comment = 'Send SMS Wizard'


class SmsResend(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, db_comment='Message')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smsresend_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_resend'
        db_table_comment = 'SMS Resend'


class SmsResendRecipient(models.Model):
    sms_resend = models.ForeignKey(SmsResend, models.DO_NOTHING, db_comment='Sms Resend')
    notification = models.ForeignKey(MailNotification, models.DO_NOTHING, db_comment='Notification')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smsresendrecipient_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    partner_name = models.CharField(blank=True, null=True, db_comment='Recipient Name')
    sms_number = models.CharField(blank=True, null=True, db_comment='Phone Number')
    resend = models.BooleanField(blank=True, null=True, db_comment='Try Again')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_resend_recipient'
        db_table_comment = 'Resend Notification'


class SmsSms(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Customer')
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True, db_comment='Mail Message')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smssms_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    uuid = models.CharField(unique=True, blank=True, null=True, db_comment='UUID')
    number = models.CharField(blank=True, null=True, db_comment='Number')
    state = models.CharField(db_comment='SMS Status')
    failure_type = models.CharField(blank=True, null=True, db_comment='Failure Type')
    body = models.TextField(blank=True, null=True, db_comment='Body')
    to_delete = models.BooleanField(blank=True, null=True, db_comment='Marked for deletion')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_sms'
        db_table_comment = 'Outgoing SMS'


class SmsTemplate(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_comment='Applies to')
    sidebar_action = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True, db_comment='Sidebar action')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smstemplate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    template_fs = models.CharField(blank=True, null=True, db_comment='Template Filename')
    lang = models.CharField(blank=True, null=True, db_comment='Language')
    model_0 = models.CharField(db_column='model', blank=True, null=True, db_comment='Related Document Model')  # Field renamed because of name conflict.
    name = models.JSONField(blank=True, null=True, db_comment='Name')
    body = models.JSONField(db_comment='Body')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_template'
        db_table_comment = 'SMS Templates'


class SmsTemplatePreview(models.Model):
    sms_template = models.ForeignKey(SmsTemplate, models.DO_NOTHING, db_comment='Sms Template')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smstemplatepreview_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    lang = models.CharField(blank=True, null=True, db_comment='Template Preview Language')
    resource_ref = models.CharField(blank=True, null=True, db_comment='Record reference')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_template_preview'
        db_table_comment = 'SMS Template Preview'


class SmsTemplateReset(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smstemplatereset_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_template_reset'
        db_table_comment = 'SMS Template Reset'


class SmsTemplateSmsTemplateResetRel(models.Model):
    pk = models.CompositePrimaryKey('sms_template_reset_id', 'sms_template_id')
    sms_template_reset = models.ForeignKey(SmsTemplateReset, models.DO_NOTHING)
    sms_template = models.ForeignKey(SmsTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sms_template_sms_template_reset_rel'
        db_table_comment = 'RELATION BETWEEN sms_template_reset AND sms_template'


class SmsTracker(models.Model):
    mail_notification = models.ForeignKey(MailNotification, models.DO_NOTHING, blank=True, null=True, db_comment='Mail Notification')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='smstracker_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    sms_uuid = models.CharField(unique=True, db_comment='SMS uuid')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'sms_tracker'
        db_table_comment = 'Link SMS to mailing/sms tracking models'


class SnailmailLetter(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True, db_comment='Sent by')
    res_id = models.IntegerField(db_comment='Document ID')
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, db_comment='Recipient')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    report_template = models.ForeignKey(IrActReportXml, models.DO_NOTHING, db_column='report_template', blank=True, null=True, db_comment='Optional report to print and attach')
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True, db_comment='Attachment')
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True, db_comment='Snailmail Status Message')
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, blank=True, null=True, db_comment='State')
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='snailmailletter_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='snailmailletter_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    model = models.CharField(db_comment='Model')
    state_0 = models.CharField(db_column='state', db_comment='Status')  # Field renamed because of name conflict.
    error_code = models.CharField(blank=True, null=True, db_comment='Error')
    street = models.CharField(blank=True, null=True, db_comment='Street')
    street2 = models.CharField(blank=True, null=True, db_comment='Street2')
    zip = models.CharField(blank=True, null=True, db_comment='Zip')
    city = models.CharField(blank=True, null=True, db_comment='City')
    info_msg = models.TextField(blank=True, null=True, db_comment='Information')
    color = models.BooleanField(blank=True, null=True, db_comment='Color')
    cover = models.BooleanField(blank=True, null=True, db_comment='Cover Page')
    duplex = models.BooleanField(blank=True, null=True, db_comment='Both side')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'snailmail_letter'
        db_table_comment = 'Snailmail Letter'


class SnailmailLetterFormatError(models.Model):
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True, db_comment='Message')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='snailmailletterformaterror_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    snailmail_cover = models.BooleanField(blank=True, null=True, db_comment='Add a Cover Page')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'snailmail_letter_format_error'
        db_table_comment = 'Format Error Sending a Snailmail Letter'


class SnailmailLetterMissingRequiredFields(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Partner')
    letter = models.ForeignKey(SnailmailLetter, models.DO_NOTHING, blank=True, null=True, db_comment='Letter')
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, blank=True, null=True, db_comment='State')
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='snailmaillettermissingrequiredfields_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    street = models.CharField(blank=True, null=True, db_comment='Street')
    street2 = models.CharField(blank=True, null=True, db_comment='Street2')
    zip = models.CharField(blank=True, null=True, db_comment='Zip')
    city = models.CharField(blank=True, null=True, db_comment='City')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'snailmail_letter_missing_required_fields'
        db_table_comment = 'Update address of partner'


class SpreadsheetDashboard(models.Model):
    dashboard_group = models.ForeignKey('SpreadsheetDashboardGroup', models.DO_NOTHING, db_comment='Dashboard Group')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='spreadsheetdashboard_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    sample_dashboard_file_path = models.CharField(blank=True, null=True, db_comment='Sample Dashboard File Path')
    name = models.JSONField(db_comment='Name')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'spreadsheet_dashboard'
        db_table_comment = 'Spreadsheet Dashboard'


class SpreadsheetDashboardGroup(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='spreadsheetdashboardgroup_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'spreadsheet_dashboard_group'
        db_table_comment = 'Group of dashboards'


class SpreadsheetDashboardShare(models.Model):
    dashboard = models.ForeignKey(SpreadsheetDashboard, models.DO_NOTHING, db_comment='Dashboard')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='spreadsheetdashboardshare_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    access_token = models.CharField(db_comment='Access Token')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'spreadsheet_dashboard_share'
        db_table_comment = 'Copy of a shared dashboard'


class StockBackorderConfirmation(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockbackorderconfirmation_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    show_transfers = models.BooleanField(blank=True, null=True, db_comment='Show Transfers')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_backorder_confirmation'
        db_table_comment = 'Backorder Confirmation'


class StockBackorderConfirmationLine(models.Model):
    backorder_confirmation = models.ForeignKey(StockBackorderConfirmation, models.DO_NOTHING, blank=True, null=True, db_comment='Immediate Transfer')
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True, db_comment='Transfer')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockbackorderconfirmationline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    to_backorder = models.BooleanField(blank=True, null=True, db_comment='To Backorder')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_backorder_confirmation_line'
        db_table_comment = 'Backorder Confirmation Line'


class StockChangeProductQty(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING, db_comment='Template')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockchangeproductqty_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    new_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='New Quantity on Hand')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_change_product_qty'
        db_table_comment = 'Change Product Quantity'


class StockConflictQuantRel(models.Model):
    pk = models.CompositePrimaryKey('stock_inventory_conflict_id', 'stock_quant_id')
    stock_inventory_conflict = models.ForeignKey('StockInventoryConflict', models.DO_NOTHING)
    stock_quant = models.ForeignKey('StockQuant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_conflict_quant_rel'
        db_table_comment = 'RELATION BETWEEN stock_inventory_conflict AND stock_quant'


class StockInventoryAdjustmentName(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockinventoryadjustmentname_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    inventory_adjustment_name = models.CharField(blank=True, null=True, db_comment='Inventory Reason')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_inventory_adjustment_name'
        db_table_comment = 'Inventory Adjustment Reference / Reason'


class StockInventoryAdjustmentNameStockQuantRel(models.Model):
    pk = models.CompositePrimaryKey('stock_inventory_adjustment_name_id', 'stock_quant_id')
    stock_inventory_adjustment_name = models.ForeignKey(StockInventoryAdjustmentName, models.DO_NOTHING)
    stock_quant = models.ForeignKey('StockQuant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_adjustment_name_stock_quant_rel'
        db_table_comment = 'RELATION BETWEEN stock_inventory_adjustment_name AND stock_quant'


class StockInventoryConflict(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockinventoryconflict_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_inventory_conflict'
        db_table_comment = 'Conflict in Inventory'


class StockInventoryConflictStockQuantRel(models.Model):
    pk = models.CompositePrimaryKey('stock_inventory_conflict_id', 'stock_quant_id')
    stock_inventory_conflict = models.ForeignKey(StockInventoryConflict, models.DO_NOTHING)
    stock_quant = models.ForeignKey('StockQuant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_conflict_stock_quant_rel'
        db_table_comment = 'RELATION BETWEEN stock_inventory_conflict AND stock_quant'


class StockInventoryWarning(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockinventorywarning_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_inventory_warning'
        db_table_comment = 'Inventory Adjustment Warning'


class StockInventoryWarningStockQuantRel(models.Model):
    pk = models.CompositePrimaryKey('stock_inventory_warning_id', 'stock_quant_id')
    stock_inventory_warning = models.ForeignKey(StockInventoryWarning, models.DO_NOTHING)
    stock_quant = models.ForeignKey('StockQuant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_warning_stock_quant_rel'
        db_table_comment = 'RELATION BETWEEN stock_inventory_warning AND stock_quant'


class StockLocation(models.Model):
    location = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Location')
    posx = models.IntegerField(blank=True, null=True, db_comment='Corridor (X)')
    posy = models.IntegerField(blank=True, null=True, db_comment='Shelves (Y)')
    posz = models.IntegerField(blank=True, null=True, db_comment='Height (Z)')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    removal_strategy = models.ForeignKey(ProductRemoval, models.DO_NOTHING, blank=True, null=True, db_comment='Removal Strategy')
    cyclic_inventory_frequency = models.IntegerField(blank=True, null=True, db_comment='Inventory Frequency')
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True, db_comment='Warehouse')
    storage_category = models.ForeignKey('StockStorageCategory', models.DO_NOTHING, blank=True, null=True, db_comment='Storage Category')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stocklocation_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Location Name')
    complete_name = models.CharField(blank=True, null=True, db_comment='Full Location Name')
    usage = models.CharField(db_comment='Location Type')
    parent_path = models.CharField(blank=True, null=True, db_comment='Parent Path')
    barcode = models.CharField(blank=True, null=True, db_comment='Barcode')
    last_inventory_date = models.DateField(blank=True, null=True, db_comment='Last Inventory')
    next_inventory_date = models.DateField(blank=True, null=True, db_comment='Next Expected')
    comment = models.TextField(blank=True, null=True, db_comment='Additional Information')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    scrap_location = models.BooleanField(blank=True, null=True, db_comment='Is a Scrap Location?')
    replenish_location = models.BooleanField(blank=True, null=True, db_comment='Replenish Location')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    valuation_in_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Stock Valuation Account (Incoming)')
    valuation_out_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='stocklocation_valuation_out_account_set', blank=True, null=True, db_comment='Stock Valuation Account (Outgoing)')

    class Meta:
        managed = False
        db_table = 'stock_location'
        unique_together = (('barcode', 'company'),)
        db_table_comment = 'Inventory Locations'


class StockLot(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True, db_comment='Unit of Measure')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, db_comment='Location')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stocklot_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Lot/Serial Number')
    ref = models.CharField(blank=True, null=True, db_comment='Internal Reference')
    lot_properties = models.JSONField(blank=True, null=True, db_comment='Properties')
    note = models.TextField(blank=True, null=True, db_comment='Description')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    standard_price = models.JSONField(blank=True, null=True, db_comment='Cost')

    class Meta:
        managed = False
        db_table = 'stock_lot'
        db_table_comment = 'Lot/Serial'


class StockMove(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_column='product_uom', db_comment='UoM')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='Source Location')
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockmove_location_dest_set', db_comment='Intermediate Location')
    location_final = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockmove_location_final_set', blank=True, null=True, db_comment='Final Location')
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Destination Address ')
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True, db_comment='Transfer')
    scrap = models.ForeignKey('StockScrap', models.DO_NOTHING, blank=True, null=True, db_comment='Scrap operation')
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True, db_comment='Procurement Group')
    rule = models.ForeignKey('StockRule', models.DO_NOTHING, blank=True, null=True, db_comment='Stock Rule')
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True, db_comment='Operation Type')
    origin_returned_move = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Origin return move')
    restrict_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='stockmove_restrict_partner_set', blank=True, null=True, db_comment='Owner ')
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True, db_comment='Warehouse')
    package_level = models.ForeignKey('StockPackageLevel', models.DO_NOTHING, blank=True, null=True, db_comment='Package Level')
    next_serial_count = models.IntegerField(blank=True, null=True, db_comment='Number of SN/Lots')
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING, blank=True, null=True, db_comment='Original Reordering Rule')
    product_packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, blank=True, null=True, db_comment='Packaging')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockmove_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Description')
    priority = models.CharField(blank=True, null=True, db_comment='Priority')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    origin = models.CharField(blank=True, null=True, db_comment='Source Document')
    procure_method = models.CharField(db_comment='Supply Method')
    reference = models.CharField(blank=True, null=True, db_comment='Reference')
    next_serial = models.CharField(blank=True, null=True, db_comment='First SN/Lot')
    reservation_date = models.DateField(blank=True, null=True, db_comment='Date to Reserve')
    description_picking = models.TextField(blank=True, null=True, db_comment='Description of Picking')
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Real Quantity')
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Demand')
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Quantity')
    picked = models.BooleanField(blank=True, null=True, db_comment='Picked')
    scrapped = models.BooleanField(blank=True, null=True, db_comment='Scrapped')
    propagate_cancel = models.BooleanField(blank=True, null=True, db_comment='Propagate cancel and split')
    is_inventory = models.BooleanField(blank=True, null=True, db_comment='Inventory')
    additional = models.BooleanField(blank=True, null=True, db_comment="Whether the move was added after the picking's confirmation")
    date = models.DateTimeField(db_comment='Date Scheduled')
    date_deadline = models.DateTimeField(blank=True, null=True, db_comment='Deadline')
    delay_alert_date = models.DateTimeField(blank=True, null=True, db_comment='Delay Alert Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    price_unit = models.FloatField(blank=True, null=True, db_comment='Unit Price')
    to_refund = models.BooleanField(blank=True, null=True, db_comment='Update quantities on SO/PO')
    sale_line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING, blank=True, null=True, db_comment='Sale Line')
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    purchase_line = models.ForeignKey(PurchaseOrderLine, models.DO_NOTHING, blank=True, null=True, db_comment='Purchase Order Line')
    is_done = models.BooleanField(blank=True, null=True)
    unit_factor = models.FloatField(blank=True, null=True)
    created_production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True, db_comment='Created Production Order')
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING, related_name='stockmove_production_set', blank=True, null=True, db_comment='Production Order for finished products')
    raw_material_production = models.ForeignKey(MrpProduction, models.DO_NOTHING, related_name='stockmove_raw_material_production_set', blank=True, null=True, db_comment='Production Order for components')
    unbuild = models.ForeignKey(MrpUnbuild, models.DO_NOTHING, blank=True, null=True, db_comment='Disassembly Order')
    consume_unbuild = models.ForeignKey(MrpUnbuild, models.DO_NOTHING, related_name='stockmove_consume_unbuild_set', blank=True, null=True, db_comment='Consumed Disassembly Order')
    operation = models.ForeignKey(MrpRoutingWorkcenter, models.DO_NOTHING, blank=True, null=True, db_comment='Operation To Consume')
    workorder = models.ForeignKey(MrpWorkorder, models.DO_NOTHING, blank=True, null=True, db_comment='Work Order To Consume')
    bom_line = models.ForeignKey(MrpBomLine, models.DO_NOTHING, blank=True, null=True, db_comment='BoM Line')
    byproduct = models.ForeignKey(MrpBomByproduct, models.DO_NOTHING, blank=True, null=True, db_comment='By-products')
    order_finished_lot = models.ForeignKey(StockLot, models.DO_NOTHING, blank=True, null=True, db_comment='Finished Lot/Serial Number')
    cost_share = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Cost Share (%)')
    manual_consumption = models.BooleanField(blank=True, null=True, db_comment='Manual Consumption')

    class Meta:
        managed = False
        db_table = 'stock_move'
        db_table_comment = 'Stock Move'


class StockMoveCreatedPurchaseLineRel(models.Model):
    pk = models.CompositePrimaryKey('created_purchase_line_id', 'move_id')
    created_purchase_line = models.ForeignKey(PurchaseOrderLine, models.DO_NOTHING)
    move = models.ForeignKey(StockMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_move_created_purchase_line_rel'
        db_table_comment = 'RELATION BETWEEN purchase_order_line AND stock_move'


class StockMoveLine(models.Model):
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True, db_comment='Transfer')
    move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True, db_comment='Stock Operation')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Unit of Measure')
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True, db_comment='Source Package')
    package_level = models.ForeignKey('StockPackageLevel', models.DO_NOTHING, blank=True, null=True, db_comment='Package Level')
    lot = models.ForeignKey(StockLot, models.DO_NOTHING, blank=True, null=True, db_comment='Lot/Serial Number')
    result_package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, related_name='stockmoveline_result_package_set', blank=True, null=True, db_comment='Destination Package')
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='From Owner')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='From')
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockmoveline_location_dest_set', db_comment='To')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockmoveline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    lot_name = models.CharField(blank=True, null=True, db_comment='Lot/Serial Number Name')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    reference = models.CharField(blank=True, null=True, db_comment='Reference')
    description_picking = models.TextField(blank=True, null=True, db_comment='Description picking')
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Quantity')
    quantity_product_uom = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Quantity in Product UoM')
    picked = models.BooleanField(blank=True, null=True, db_comment='Picked')
    date = models.DateTimeField(db_comment='Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING, blank=True, null=True, db_comment='Carrier')
    workorder = models.ForeignKey(MrpWorkorder, models.DO_NOTHING, blank=True, null=True, db_comment='Work Order')
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True, db_comment='Production Order')

    class Meta:
        managed = False
        db_table = 'stock_move_line'
        db_table_comment = 'Product Moves (Stock Move Line)'


class StockMoveLineConsumeRel(models.Model):
    pk = models.CompositePrimaryKey('consume_line_id', 'produce_line_id')
    consume_line = models.ForeignKey(StockMoveLine, models.DO_NOTHING)
    produce_line = models.ForeignKey(StockMoveLine, models.DO_NOTHING, related_name='stockmovelineconsumerel_produce_line_set')

    class Meta:
        managed = False
        db_table = 'stock_move_line_consume_rel'
        db_table_comment = 'RELATION BETWEEN stock_move_line AND stock_move_line'


class StockMoveMoveRel(models.Model):
    pk = models.CompositePrimaryKey('move_orig_id', 'move_dest_id')
    move_orig = models.ForeignKey(StockMove, models.DO_NOTHING)
    move_dest = models.ForeignKey(StockMove, models.DO_NOTHING, related_name='stockmovemoverel_move_dest_set')

    class Meta:
        managed = False
        db_table = 'stock_move_move_rel'
        db_table_comment = 'RELATION BETWEEN stock_move AND stock_move'


class StockNotificationProductPartnerRel(models.Model):
    pk = models.CompositePrimaryKey('product_product_id', 'res_partner_id')
    product_product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    res_partner = models.ForeignKey(ResPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_notification_product_partner_rel'
        db_table_comment = 'RELATION BETWEEN product_product AND res_partner'


class StockOrderpointSnooze(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockorderpointsnooze_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    predefined_date = models.CharField(blank=True, null=True, db_comment='Snooze for')
    snoozed_until = models.DateField(blank=True, null=True, db_comment='Snooze Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_orderpoint_snooze'
        db_table_comment = 'Snooze Orderpoint'


class StockOrderpointSnoozeStockWarehouseOrderpointRel(models.Model):
    pk = models.CompositePrimaryKey('stock_orderpoint_snooze_id', 'stock_warehouse_orderpoint_id')
    stock_orderpoint_snooze = models.ForeignKey(StockOrderpointSnooze, models.DO_NOTHING)
    stock_warehouse_orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_orderpoint_snooze_stock_warehouse_orderpoint_rel'
        db_table_comment = 'RELATION BETWEEN stock_orderpoint_snooze AND stock_warehouse_orderpoint'


class StockPackageDestination(models.Model):
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, db_comment='Picking')
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='Destination location')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockpackagedestination_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_package_destination'
        db_table_comment = 'Stock Package Destination'


class StockPackageLevel(models.Model):
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, db_comment='Package')
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True, db_comment='Picking')
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, db_comment='To')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockpackagelevel_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_package_level'
        db_table_comment = 'Stock Package Level'


class StockPackageType(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockpackagetype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Package Type')
    barcode = models.CharField(unique=True, blank=True, null=True, db_comment='Barcode')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    height = models.FloatField(blank=True, null=True, db_comment='Height')
    width = models.FloatField(blank=True, null=True, db_comment='Width')
    packaging_length = models.FloatField(blank=True, null=True, db_comment='Length')
    base_weight = models.FloatField(blank=True, null=True, db_comment='Weight')
    max_weight = models.FloatField(blank=True, null=True, db_comment='Max Weight')
    shipper_package_code = models.CharField(blank=True, null=True, db_comment='Carrier Code')
    package_carrier_type = models.CharField(blank=True, null=True, db_comment='Carrier')

    class Meta:
        managed = False
        db_table = 'stock_package_type'
        db_table_comment = 'Stock package type'


class StockPackageTypeStockPutawayRuleRel(models.Model):
    pk = models.CompositePrimaryKey('stock_putaway_rule_id', 'stock_package_type_id')
    stock_putaway_rule = models.ForeignKey('StockPutawayRule', models.DO_NOTHING)
    stock_package_type = models.ForeignKey(StockPackageType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_package_type_stock_putaway_rule_rel'
        db_table_comment = 'RELATION BETWEEN stock_putaway_rule AND stock_package_type'


class StockPicking(models.Model):
    backorder = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Back Order of')
    return_field = models.ForeignKey('self', models.DO_NOTHING, db_column='return_id', related_name='stockpicking_return_field_set', blank=True, null=True, db_comment='Return of')  # Field renamed because it was a Python reserved word.
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True, db_comment='Procurement Group')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='Source Location')
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockpicking_location_dest_set', db_comment='Destination Location')
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, db_comment='Operation Type')
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Contact')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True, db_comment='Responsible')
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='stockpicking_owner_set', blank=True, null=True, db_comment='Assign Owner')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='stockpicking_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockpicking_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Reference')
    origin = models.CharField(blank=True, null=True, db_comment='Source Document')
    move_type = models.CharField(db_comment='Shipping Policy')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    priority = models.CharField(blank=True, null=True, db_comment='Priority')
    picking_properties = models.JSONField(blank=True, null=True, db_comment='Properties')
    note = models.TextField(blank=True, null=True, db_comment='Notes')
    has_deadline_issue = models.BooleanField(blank=True, null=True, db_comment='Is late')
    printed = models.BooleanField(blank=True, null=True, db_comment='Printed')
    is_locked = models.BooleanField(blank=True, null=True, db_comment='Is Locked')
    scheduled_date = models.DateTimeField(blank=True, null=True, db_comment='Scheduled Date')
    date_deadline = models.DateTimeField(blank=True, null=True, db_comment='Deadline')
    date = models.DateTimeField(blank=True, null=True, db_comment='Creation Date')
    date_done = models.DateTimeField(blank=True, null=True, db_comment='Date of Transfer')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    sale = models.ForeignKey(SaleOrder, models.DO_NOTHING, blank=True, null=True)
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING, blank=True, null=True, db_comment='Carrier')
    carrier_tracking_ref = models.CharField(blank=True, null=True, db_comment='Tracking Reference')
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Weight')
    carrier_price = models.FloatField(blank=True, null=True, db_comment='Shipping Cost')
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    pos_session = models.ForeignKey(PosSession, models.DO_NOTHING, blank=True, null=True, db_comment='Pos Session')
    pos_order = models.ForeignKey(PosOrder, models.DO_NOTHING, blank=True, null=True, db_comment='Pos Order')

    class Meta:
        managed = False
        db_table = 'stock_picking'
        unique_together = (('name', 'company'),)
        db_table_comment = 'Transfer'


class StockPickingBackorderRel(models.Model):
    pk = models.CompositePrimaryKey('stock_backorder_confirmation_id', 'stock_picking_id')
    stock_backorder_confirmation = models.ForeignKey(StockBackorderConfirmation, models.DO_NOTHING)
    stock_picking = models.ForeignKey(StockPicking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_backorder_rel'
        db_table_comment = 'RELATION BETWEEN stock_backorder_confirmation AND stock_picking'


class StockPickingSmsRel(models.Model):
    pk = models.CompositePrimaryKey('confirm_stock_sms_id', 'stock_picking_id')
    confirm_stock_sms = models.ForeignKey(ConfirmStockSms, models.DO_NOTHING)
    stock_picking = models.ForeignKey(StockPicking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_sms_rel'
        db_table_comment = 'RELATION BETWEEN confirm_stock_sms AND stock_picking'


class StockPickingType(models.Model):
    color = models.IntegerField(blank=True, null=True, db_comment='Color')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    sequence_0 = models.ForeignKey(IrSequence, models.DO_NOTHING, db_column='sequence_id', blank=True, null=True, db_comment='Reference Sequence')  # Field renamed because of name conflict.
    default_location_src = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='Source Location')
    default_location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockpickingtype_default_location_dest_set', db_comment='Destination Location')
    return_picking_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Operation Type for Returns')
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True, db_comment='Warehouse')
    reservation_days_before = models.IntegerField(blank=True, null=True, db_comment='Days')
    reservation_days_before_priority = models.IntegerField(blank=True, null=True, db_comment='Days when starred')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockpickingtype_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    sequence_code = models.CharField(db_comment='Sequence Prefix')
    code = models.CharField(db_comment='Type of Operation')
    reservation_method = models.CharField(db_comment='Reservation Method')
    product_label_format = models.CharField(blank=True, null=True, db_comment='Product Label Format to auto-print')
    lot_label_format = models.CharField(blank=True, null=True, db_comment='Lot Label Format to auto-print')
    package_label_to_print = models.CharField(blank=True, null=True, db_comment='Package Label to Print')
    barcode = models.CharField(blank=True, null=True, db_comment='Barcode')
    create_backorder = models.CharField(db_comment='Create Backorder')
    move_type = models.CharField(db_comment='Shipping Policy')
    name = models.JSONField(db_comment='Operation Type')
    picking_properties_definition = models.JSONField(blank=True, null=True, db_comment='Picking Properties')
    show_entire_packs = models.BooleanField(blank=True, null=True, db_comment='Move Entire Packages')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    use_create_lots = models.BooleanField(blank=True, null=True, db_comment='Create New Lots/Serial Numbers')
    use_existing_lots = models.BooleanField(blank=True, null=True, db_comment='Use Existing Lots/Serial Numbers')
    print_label = models.BooleanField(blank=True, null=True, db_comment='Generate Shipping Labels')
    show_operations = models.BooleanField(blank=True, null=True, db_comment='Show Detailed Operations')
    auto_show_reception_report = models.BooleanField(blank=True, null=True, db_comment='Show Reception Report at Validation')
    auto_print_delivery_slip = models.BooleanField(blank=True, null=True, db_comment='Auto Print Delivery Slip')
    auto_print_return_slip = models.BooleanField(blank=True, null=True, db_comment='Auto Print Return Slip')
    auto_print_product_labels = models.BooleanField(blank=True, null=True, db_comment='Auto Print Product Labels')
    auto_print_lot_labels = models.BooleanField(blank=True, null=True, db_comment='Auto Print Lot/SN Labels')
    auto_print_reception_report = models.BooleanField(blank=True, null=True, db_comment='Auto Print Reception Report')
    auto_print_reception_report_labels = models.BooleanField(blank=True, null=True, db_comment='Auto Print Reception Report Labels')
    auto_print_packages = models.BooleanField(blank=True, null=True, db_comment='Auto Print Packages')
    auto_print_package_label = models.BooleanField(blank=True, null=True, db_comment='Auto Print Package Label')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    mrp_product_label_to_print = models.CharField(blank=True, null=True, db_comment='Product Label to Print')
    done_mrp_lot_label_to_print = models.CharField(blank=True, null=True, db_comment='Lot/SN Label to Print')
    generated_mrp_lot_label_to_print = models.CharField(blank=True, null=True, db_comment='Generated Lot/SN Label to Print')
    use_create_components_lots = models.BooleanField(blank=True, null=True, db_comment='Create New Lots/Serial Numbers for Components')
    auto_print_done_production_order = models.BooleanField(blank=True, null=True, db_comment='Auto Print Done Production Order')
    auto_print_done_mrp_product_labels = models.BooleanField(blank=True, null=True, db_comment='Auto Print Produced Product Labels')
    auto_print_done_mrp_lot = models.BooleanField(blank=True, null=True, db_comment='Auto Print Produced Lot Label')
    auto_print_mrp_reception_report = models.BooleanField(blank=True, null=True, db_comment='Auto Print Allocation Report')
    auto_print_mrp_reception_report_labels = models.BooleanField(blank=True, null=True, db_comment='Auto Print Allocation Report Labels')
    auto_print_generated_mrp_lot = models.BooleanField(blank=True, null=True, db_comment='Auto Print Generated Lot/SN Label')

    class Meta:
        managed = False
        db_table = 'stock_picking_type'
        db_table_comment = 'Picking Type'


class StockPutawayRule(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True, db_comment='Product Category')
    location_in = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='When product arrives in')
    location_out = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockputawayrule_location_out_set', db_comment='Store to sublocation')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Priority')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    storage_category = models.ForeignKey('StockStorageCategory', models.DO_NOTHING, blank=True, null=True, db_comment='Storage Category')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockputawayrule_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    sublocation = models.CharField(blank=True, null=True, db_comment='Sublocation')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_putaway_rule'
        db_table_comment = 'Putaway Rule'


class StockQuant(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='Location')
    storage_category = models.ForeignKey('StockStorageCategory', models.DO_NOTHING, blank=True, null=True, db_comment='Storage Category')
    lot = models.ForeignKey(StockLot, models.DO_NOTHING, blank=True, null=True, db_comment='Lot/Serial Number')
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True, db_comment='Package')
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Owner')
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True, db_comment='Assigned To')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='stockquant_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockquant_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    inventory_date = models.DateField(blank=True, null=True, db_comment='Scheduled Date')
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Quantity')
    reserved_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Reserved Quantity')
    inventory_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Counted Quantity')
    inventory_diff_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Difference')
    inventory_quantity_set = models.BooleanField(blank=True, null=True, db_comment='Inventory Quantity Set')
    in_date = models.DateTimeField(db_comment='Incoming Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    accounting_date = models.DateField(blank=True, null=True, db_comment='Accounting Date')

    class Meta:
        managed = False
        db_table = 'stock_quant'
        db_table_comment = 'Quants'


class StockQuantPackage(models.Model):
    package_type = models.ForeignKey(StockPackageType, models.DO_NOTHING, blank=True, null=True, db_comment='Package Type')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, db_comment='Location')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockquantpackage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Package Reference')
    package_use = models.CharField(db_comment='Package Use')
    pack_date = models.DateField(blank=True, null=True, db_comment='Pack Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    shipping_weight = models.FloatField(blank=True, null=True, db_comment='Shipping Weight')

    class Meta:
        managed = False
        db_table = 'stock_quant_package'
        db_table_comment = 'Packages'


class StockQuantRelocate(models.Model):
    dest_location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, db_comment='Dest Location')
    dest_package = models.ForeignKey(StockQuantPackage, models.DO_NOTHING, blank=True, null=True, db_comment='Dest Package')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockquantrelocate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    message = models.TextField(blank=True, null=True, db_comment='Reason for relocation')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_quant_relocate'
        db_table_comment = 'Stock Quantity Relocation'


class StockQuantStockQuantRelocateRel(models.Model):
    pk = models.CompositePrimaryKey('stock_quant_relocate_id', 'stock_quant_id')
    stock_quant_relocate = models.ForeignKey(StockQuantRelocate, models.DO_NOTHING)
    stock_quant = models.ForeignKey(StockQuant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_quant_stock_quant_relocate_rel'
        db_table_comment = 'RELATION BETWEEN stock_quant_relocate AND stock_quant'


class StockQuantStockRequestCountRel(models.Model):
    pk = models.CompositePrimaryKey('stock_request_count_id', 'stock_quant_id')
    stock_request_count = models.ForeignKey('StockRequestCount', models.DO_NOTHING)
    stock_quant = models.ForeignKey(StockQuant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_quant_stock_request_count_rel'
        db_table_comment = 'RELATION BETWEEN stock_request_count AND stock_quant'


class StockQuantStockTrackConfirmationRel(models.Model):
    pk = models.CompositePrimaryKey('stock_track_confirmation_id', 'stock_quant_id')
    stock_track_confirmation = models.ForeignKey('StockTrackConfirmation', models.DO_NOTHING)
    stock_quant = models.ForeignKey(StockQuant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_quant_stock_track_confirmation_rel'
        db_table_comment = 'RELATION BETWEEN stock_track_confirmation AND stock_quant'


class StockQuantityHistory(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockquantityhistory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    inventory_datetime = models.DateTimeField(blank=True, null=True, db_comment='Inventory at Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_quantity_history'
        db_table_comment = 'Stock Quantity History'


class StockReplenishmentInfo(models.Model):
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING, blank=True, null=True, db_comment='Orderpoint')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockreplenishmentinfo_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_replenishment_info'
        db_table_comment = 'Stock supplier replenishment information'


class StockReplenishmentOption(models.Model):
    route = models.ForeignKey('StockRoute', models.DO_NOTHING, blank=True, null=True, db_comment='Route')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    replenishment_info = models.ForeignKey(StockReplenishmentInfo, models.DO_NOTHING, blank=True, null=True, db_comment='Replenishment Info')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockreplenishmentoption_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_replenishment_option'
        db_table_comment = 'Stock warehouse replenishment option'


class StockRequestCount(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True, db_comment='User')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='stockrequestcount_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockrequestcount_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    set_count = models.CharField(blank=True, null=True, db_comment='Count')
    inventory_date = models.DateField(db_comment='Inventory Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    accounting_date = models.DateField(blank=True, null=True, db_comment='Accounting Date')

    class Meta:
        managed = False
        db_table = 'stock_request_count'
        db_table_comment = 'Stock Request an Inventory Count'


class StockReturnPicking(models.Model):
    picking = models.ForeignKey(StockPicking, models.DO_NOTHING, blank=True, null=True, db_comment='Picking')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockreturnpicking_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_return_picking'
        db_table_comment = 'Return Picking'


class StockReturnPickingLine(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    wizard = models.ForeignKey(StockReturnPicking, models.DO_NOTHING, blank=True, null=True, db_comment='Wizard')
    move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True, db_comment='Move')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockreturnpickingline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    to_refund = models.BooleanField(blank=True, null=True, db_comment='Update quantities on SO/PO')

    class Meta:
        managed = False
        db_table = 'stock_return_picking_line'
        db_table_comment = 'Return Picking Line'


class StockRoute(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    supplied_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True, db_comment='Supplied Warehouse')
    supplier_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name='stockroute_supplier_wh_set', blank=True, null=True, db_comment='Supplying Warehouse')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockroute_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Route')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    product_selectable = models.BooleanField(blank=True, null=True, db_comment='Applicable on Product')
    product_categ_selectable = models.BooleanField(blank=True, null=True, db_comment='Applicable on Product Category')
    warehouse_selectable = models.BooleanField(blank=True, null=True, db_comment='Applicable on Warehouse')
    packaging_selectable = models.BooleanField(blank=True, null=True, db_comment='Applicable on Packaging')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    sale_selectable = models.BooleanField(blank=True, null=True, db_comment='Selectable on Sales Order Line')
    shipping_selectable = models.BooleanField(blank=True, null=True, db_comment='Applicable on Shipping Methods')

    class Meta:
        managed = False
        db_table = 'stock_route'
        db_table_comment = 'Inventory Routes'


class StockRouteCateg(models.Model):
    pk = models.CompositePrimaryKey('route_id', 'categ_id')
    route = models.ForeignKey(StockRoute, models.DO_NOTHING)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_categ'
        db_table_comment = 'RELATION BETWEEN stock_route AND product_category'


class StockRouteMove(models.Model):
    pk = models.CompositePrimaryKey('move_id', 'route_id')
    move = models.ForeignKey(StockMove, models.DO_NOTHING)
    route = models.ForeignKey(StockRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_move'
        db_table_comment = 'RELATION BETWEEN stock_move AND stock_route'


class StockRoutePackaging(models.Model):
    pk = models.CompositePrimaryKey('route_id', 'packaging_id')
    route = models.ForeignKey(StockRoute, models.DO_NOTHING)
    packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_packaging'
        db_table_comment = 'RELATION BETWEEN stock_route AND product_packaging'


class StockRouteProduct(models.Model):
    pk = models.CompositePrimaryKey('route_id', 'product_id')
    route = models.ForeignKey(StockRoute, models.DO_NOTHING)
    product = models.ForeignKey(ProductTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_product'
        db_table_comment = 'RELATION BETWEEN stock_route AND product_template'


class StockRouteShipping(models.Model):
    pk = models.CompositePrimaryKey('shipping_id', 'route_id')
    shipping = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING)
    route = models.ForeignKey(StockRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_shipping'
        db_table_comment = 'RELATION BETWEEN delivery_carrier AND stock_route'


class StockRouteStockRulesReportRel(models.Model):
    pk = models.CompositePrimaryKey('stock_rules_report_id', 'stock_route_id')
    stock_rules_report = models.ForeignKey('StockRulesReport', models.DO_NOTHING)
    stock_route = models.ForeignKey(StockRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_stock_rules_report_rel'
        db_table_comment = 'RELATION BETWEEN stock_rules_report AND stock_route'


class StockRouteWarehouse(models.Model):
    pk = models.CompositePrimaryKey('route_id', 'warehouse_id')
    route = models.ForeignKey(StockRoute, models.DO_NOTHING)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_warehouse'
        db_table_comment = 'RELATION BETWEEN stock_route AND stock_warehouse'


class StockRule(models.Model):
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True, db_comment='Fixed Procurement Group')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='Destination Location')
    location_src = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockrule_location_src_set', blank=True, null=True, db_comment='Source Location')
    route = models.ForeignKey(StockRoute, models.DO_NOTHING, db_comment='Route')
    route_sequence = models.IntegerField(blank=True, null=True, db_comment='Route Sequence')
    picking_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, db_comment='Operation Type')
    delay = models.IntegerField(blank=True, null=True, db_comment='Lead Time')
    partner_address = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Partner Address')
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True, db_comment='Warehouse')
    propagate_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name='stockrule_propagate_warehouse_set', blank=True, null=True, db_comment='Warehouse to Propagate')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockrule_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    group_propagation_option = models.CharField(blank=True, null=True, db_comment='Propagation of Procurement Group')
    action = models.CharField(db_comment='Action')
    procure_method = models.CharField(db_comment='Supply Method')
    auto = models.CharField(db_comment='Automatic Move')
    push_domain = models.CharField(blank=True, null=True, db_comment='Push Applicability')
    name = models.JSONField(db_comment='Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    location_dest_from_rule = models.BooleanField(blank=True, null=True, db_comment='Destination location origin from rule')
    propagate_cancel = models.BooleanField(blank=True, null=True, db_comment='Cancel Next Move')
    propagate_carrier = models.BooleanField(blank=True, null=True, db_comment='Propagation of carrier')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_rule'
        db_table_comment = 'Stock Rule'


class StockRulesReport(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING, db_comment='Product Template')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockrulesreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    product_has_variants = models.BooleanField(db_comment='Has variants')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_rules_report'
        db_table_comment = 'Stock Rules report'


class StockRulesReportStockWarehouseRel(models.Model):
    pk = models.CompositePrimaryKey('stock_rules_report_id', 'stock_warehouse_id')
    stock_rules_report = models.ForeignKey(StockRulesReport, models.DO_NOTHING)
    stock_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_rules_report_stock_warehouse_rel'
        db_table_comment = 'RELATION BETWEEN stock_rules_report AND stock_warehouse'


class StockScrap(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_comment='Unit of Measure')
    lot = models.ForeignKey(StockLot, models.DO_NOTHING, blank=True, null=True, db_comment='Lot/Serial')
    package = models.ForeignKey(StockQuantPackage, models.DO_NOTHING, blank=True, null=True, db_comment='Package')
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Owner')
    picking = models.ForeignKey(StockPicking, models.DO_NOTHING, blank=True, null=True, db_comment='Picking')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='Source Location')
    scrap_location = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockscrap_scrap_location_set', db_comment='Scrap Location')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockscrap_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Reference')
    origin = models.CharField(blank=True, null=True, db_comment='Source Document')
    state = models.CharField(blank=True, null=True, db_comment='Status')
    scrap_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Quantity')
    should_replenish = models.BooleanField(blank=True, null=True, db_comment='Replenish Quantities')
    date_done = models.DateTimeField(blank=True, null=True, db_comment='Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True, db_comment='Manufacturing Order')
    workorder = models.ForeignKey(MrpWorkorder, models.DO_NOTHING, blank=True, null=True, db_comment='Work Order')
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, blank=True, null=True, db_comment='Kit')

    class Meta:
        managed = False
        db_table = 'stock_scrap'
        db_table_comment = 'Scrap'


class StockScrapReasonTag(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockscrapreasontag_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    color = models.CharField(blank=True, null=True, db_comment='Color')
    name = models.JSONField(unique=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_scrap_reason_tag'
        db_table_comment = 'Scrap Reason Tag'


class StockScrapStockScrapReasonTagRel(models.Model):
    pk = models.CompositePrimaryKey('stock_scrap_id', 'stock_scrap_reason_tag_id')
    stock_scrap = models.ForeignKey(StockScrap, models.DO_NOTHING)
    stock_scrap_reason_tag = models.ForeignKey(StockScrapReasonTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_scrap_stock_scrap_reason_tag_rel'
        db_table_comment = 'RELATION BETWEEN stock_scrap AND stock_scrap_reason_tag'


class StockStorageCategory(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockstoragecategory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Storage Category')
    allow_new_product = models.CharField(db_comment='Allow New Product')
    max_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Max Weight')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_storage_category'
        db_table_comment = 'Storage Category'


class StockStorageCategoryCapacity(models.Model):
    storage_category = models.ForeignKey(StockStorageCategory, models.DO_NOTHING, db_comment='Storage Category')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    package_type = models.ForeignKey(StockPackageType, models.DO_NOTHING, blank=True, null=True, db_comment='Package Type')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockstoragecategorycapacity_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    quantity = models.FloatField(db_comment='Quantity')

    class Meta:
        managed = False
        db_table = 'stock_storage_category_capacity'
        unique_together = (('package_type', 'storage_category'), ('product', 'storage_category'),)
        db_table_comment = 'Storage Category Capacity'


class StockTraceabilityReport(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stocktraceabilityreport_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_traceability_report'
        db_table_comment = 'Traceability Report'


class StockTrackConfirmation(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stocktrackconfirmation_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_track_confirmation'
        db_table_comment = 'Stock Track Confirmation'


class StockTrackLine(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Product')
    wizard = models.ForeignKey(StockTrackConfirmation, models.DO_NOTHING, blank=True, null=True, db_comment='Wizard')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stocktrackline_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_track_line'
        db_table_comment = 'Stock Track Line'


class StockValuationLayer(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True, db_comment='Product Category')
    stock_valuation_layer = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Linked To')
    stock_move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True, db_comment='Stock Move')
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True, db_comment='Journal Entry')
    account_move_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, blank=True, null=True, db_comment='Invoice Line')
    lot = models.ForeignKey(StockLot, models.DO_NOTHING, blank=True, null=True, db_comment='Lot/Serial Number')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockvaluationlayer_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    description = models.CharField(blank=True, null=True, db_comment='Description')
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Quantity')
    unit_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Unit Value')
    value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Total Value')
    remaining_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Remaining Qty')
    remaining_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Remaining Value')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    price_diff_value = models.FloatField(blank=True, null=True, db_comment='Invoice value correction with invoice currency')

    class Meta:
        managed = False
        db_table = 'stock_valuation_layer'
        db_table_comment = 'Stock Valuation Layer'


class StockValuationLayerRevaluation(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Related product')
    lot = models.ForeignKey(StockLot, models.DO_NOTHING, blank=True, null=True, db_comment='Related lot/serial number')
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, db_comment='Journal')
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, db_comment='Counterpart Account')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockvaluationlayerrevaluation_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    reason = models.CharField(blank=True, null=True, db_comment='Reason')
    date = models.DateField(blank=True, null=True, db_comment='Accounting Date')
    added_value = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Added value')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'stock_valuation_layer_revaluation'
        db_table_comment = 'Wizard model to reavaluate a stock inventory for a product'


class StockValuationLayerStockValuationLayerRevaluationRel(models.Model):
    pk = models.CompositePrimaryKey('stock_valuation_layer_revaluation_id', 'stock_valuation_layer_id')
    stock_valuation_layer_revaluation = models.ForeignKey(StockValuationLayerRevaluation, models.DO_NOTHING)
    stock_valuation_layer = models.ForeignKey(StockValuationLayer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_valuation_layer_stock_valuation_layer_revaluation_rel'
        db_table_comment = 'RELATION BETWEEN stock_valuation_layer_revaluation AND stock_valuation_layer'


class StockWarehouse(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Address')
    view_location = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='View Location')
    lot_stock = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockwarehouse_lot_stock_set', db_comment='Location Stock')
    wh_input_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockwarehouse_wh_input_stock_loc_set', blank=True, null=True, db_comment='Input Location')
    wh_qc_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockwarehouse_wh_qc_stock_loc_set', blank=True, null=True, db_comment='Quality Control Location')
    wh_output_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockwarehouse_wh_output_stock_loc_set', blank=True, null=True, db_comment='Output Location')
    wh_pack_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockwarehouse_wh_pack_stock_loc_set', blank=True, null=True, db_comment='Packing Location')
    mto_pull = models.ForeignKey(StockRule, models.DO_NOTHING, blank=True, null=True, db_comment='MTO rule')
    pick_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True, db_comment='Pick Type')
    pack_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_pack_type_set', blank=True, null=True, db_comment='Pack Type')
    out_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_out_type_set', blank=True, null=True, db_comment='Out Type')
    in_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_in_type_set', blank=True, null=True, db_comment='In Type')
    int_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_int_type_set', blank=True, null=True, db_comment='Internal Type')
    qc_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_qc_type_set', blank=True, null=True, db_comment='Quality Control Type')
    store_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_store_type_set', blank=True, null=True, db_comment='Storage Type')
    xdock_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_xdock_type_set', blank=True, null=True, db_comment='Cross Dock Type')
    crossdock_route = models.ForeignKey(StockRoute, models.DO_NOTHING, blank=True, null=True, db_comment='Crossdock Route')
    reception_route = models.ForeignKey(StockRoute, models.DO_NOTHING, related_name='stockwarehouse_reception_route_set', blank=True, null=True, db_comment='Receipt Route')
    delivery_route = models.ForeignKey(StockRoute, models.DO_NOTHING, related_name='stockwarehouse_delivery_route_set', blank=True, null=True, db_comment='Delivery Route')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockwarehouse_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Warehouse')
    code = models.CharField(max_length=5, db_comment='Short Name')
    reception_steps = models.CharField(db_comment='Incoming Shipments')
    delivery_steps = models.CharField(db_comment='Outgoing Shipments')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    pos_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_pos_type_set', blank=True, null=True, db_comment='Point of Sale Operation Type')
    buy_pull = models.ForeignKey(StockRule, models.DO_NOTHING, related_name='stockwarehouse_buy_pull_set', blank=True, null=True, db_comment='Buy rule')
    buy_to_resupply = models.BooleanField(blank=True, null=True, db_comment='Buy to Resupply')
    manufacture_pull = models.ForeignKey(StockRule, models.DO_NOTHING, related_name='stockwarehouse_manufacture_pull_set', blank=True, null=True, db_comment='Manufacture Rule')
    manufacture_mto_pull = models.ForeignKey(StockRule, models.DO_NOTHING, related_name='stockwarehouse_manufacture_mto_pull_set', blank=True, null=True, db_comment='Manufacture MTO Rule')
    pbm_mto_pull = models.ForeignKey(StockRule, models.DO_NOTHING, related_name='stockwarehouse_pbm_mto_pull_set', blank=True, null=True, db_comment='Picking Before Manufacturing MTO Rule')
    sam_rule = models.ForeignKey(StockRule, models.DO_NOTHING, related_name='stockwarehouse_sam_rule_set', blank=True, null=True, db_comment='Stock After Manufacturing Rule')
    manu_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_manu_type_set', blank=True, null=True, db_comment='Manufacturing Operation Type')
    pbm_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_pbm_type_set', blank=True, null=True, db_comment='Picking Before Manufacturing Operation Type')
    sam_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, related_name='stockwarehouse_sam_type_set', blank=True, null=True, db_comment='Stock After Manufacturing Operation Type')
    pbm_route = models.ForeignKey(StockRoute, models.DO_NOTHING, related_name='stockwarehouse_pbm_route_set', blank=True, null=True, db_comment='Picking Before Manufacturing Route')
    pbm_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockwarehouse_pbm_loc_set', blank=True, null=True, db_comment='Picking before Manufacturing Location')
    sam_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='stockwarehouse_sam_loc_set', blank=True, null=True, db_comment='Stock after Manufacturing Location')
    manufacture_steps = models.CharField(db_comment='Manufacture')
    manufacture_to_resupply = models.BooleanField(blank=True, null=True, db_comment='Manufacture to Resupply')

    class Meta:
        managed = False
        db_table = 'stock_warehouse'
        unique_together = (('code', 'company'), ('name', 'company'),)
        db_table_comment = 'Warehouse'


class StockWarehouseOrderpoint(models.Model):
    warehouse = models.ForeignKey(StockWarehouse, models.DO_NOTHING, db_comment='Warehouse')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='Location')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True, db_comment='Product Category')
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True, db_comment='Procurement Group')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company')
    route = models.ForeignKey(StockRoute, models.DO_NOTHING, blank=True, null=True, db_comment='Route')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockwarehouseorderpoint_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    trigger = models.CharField(db_comment='Trigger')
    snoozed_until = models.DateField(blank=True, null=True, db_comment='Snoozed')
    product_min_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Min Quantity')
    product_max_qty = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Max Quantity')
    qty_multiple = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Multiple Quantity')
    qty_to_order_manual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='To Order Manual')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    supplier = models.ForeignKey(ProductSupplierinfo, models.DO_NOTHING, blank=True, null=True, db_comment='Supplier')
    vendor = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Vendor')
    product_supplier = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='stockwarehouseorderpoint_product_supplier_set', blank=True, null=True, db_comment='Product Supplier')
    purchase_visibility_days = models.FloatField(blank=True, null=True, db_comment='Purchase Visibility Days')
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, blank=True, null=True, db_comment='Bill of Materials')
    manufacturing_visibility_days = models.FloatField(blank=True, null=True, db_comment='Manufacturing Visibility Days')

    class Meta:
        managed = False
        db_table = 'stock_warehouse_orderpoint'
        unique_together = (('product', 'location', 'company'),)
        db_table_comment = 'Minimum Inventory Rule'


class StockWarnInsufficientQtyScrap(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='Location')
    scrap = models.ForeignKey(StockScrap, models.DO_NOTHING, blank=True, null=True, db_comment='Scrap')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockwarninsufficientqtyscrap_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    product_uom_name = models.CharField(db_comment='Unit of Measure')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    quantity = models.FloatField(db_comment='Quantity')

    class Meta:
        managed = False
        db_table = 'stock_warn_insufficient_qty_scrap'
        db_table_comment = 'Warn Insufficient Scrap Quantity'


class StockWarnInsufficientQtyUnbuild(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_comment='Product')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, db_comment='Location')
    unbuild = models.ForeignKey(MrpUnbuild, models.DO_NOTHING, blank=True, null=True, db_comment='Unbuild')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='stockwarninsufficientqtyunbuild_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    product_uom_name = models.CharField(db_comment='Unit of Measure')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    quantity = models.FloatField(db_comment='Quantity')

    class Meta:
        managed = False
        db_table = 'stock_warn_insufficient_qty_unbuild'
        db_table_comment = 'Warn Insufficient Unbuild Quantity'


class StockWhResupplyTable(models.Model):
    pk = models.CompositePrimaryKey('supplied_wh_id', 'supplier_wh_id')
    supplied_wh = models.ForeignKey(StockWarehouse, models.DO_NOTHING)
    supplier_wh = models.ForeignKey(StockWarehouse, models.DO_NOTHING, related_name='stockwhresupplytable_supplier_wh_set')

    class Meta:
        managed = False
        db_table = 'stock_wh_resupply_table'
        db_table_comment = 'RELATION BETWEEN stock_warehouse AND stock_warehouse'


class TeamFavoriteUserRel(models.Model):
    pk = models.CompositePrimaryKey('team_id', 'user_id')
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_favorite_user_rel'
        db_table_comment = 'RELATION BETWEEN crm_team AND res_users'


class TemplateAttributeValueMrpProductionRel(models.Model):
    pk = models.CompositePrimaryKey('production_id', 'template_attribute_value_id')
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING)
    template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'template_attribute_value_mrp_production_rel'
        db_table_comment = 'RELATION BETWEEN mrp_production AND product_template_attribute_value'


class TemplateAttributeValueStockMoveRel(models.Model):
    pk = models.CompositePrimaryKey('move_id', 'template_attribute_value_id')
    move = models.ForeignKey(StockMove, models.DO_NOTHING)
    template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'template_attribute_value_stock_move_rel'
        db_table_comment = 'RELATION BETWEEN stock_move AND product_template_attribute_value'


class ThemeIrAsset(models.Model):
    sequence = models.IntegerField(db_comment='Sequence')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='themeirasset_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    key = models.CharField(blank=True, null=True, db_comment='Key')
    name = models.CharField(db_comment='Name')
    bundle = models.CharField(db_comment='Bundle')
    directive = models.CharField(blank=True, null=True, db_comment='Directive')
    path = models.CharField(db_comment='Path')
    target = models.CharField(blank=True, null=True, db_comment='Target')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'theme_ir_asset'
        db_table_comment = 'Theme Asset'


class ThemeIrAttachment(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='themeirattachment_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    key = models.CharField(db_comment='Key')
    url = models.CharField(blank=True, null=True, db_comment='Url')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'theme_ir_attachment'
        db_table_comment = 'Theme Attachments'


class ThemeIrUiView(models.Model):
    priority = models.IntegerField(db_comment='Priority')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='themeiruiview_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    key = models.CharField(blank=True, null=True, db_comment='Key')
    type = models.CharField(blank=True, null=True, db_comment='Type')
    mode = models.CharField(blank=True, null=True, db_comment='Mode')
    arch_fs = models.CharField(blank=True, null=True, db_comment='Arch Fs')
    inherit_id = models.CharField(blank=True, null=True, db_comment='Inherit')
    arch = models.JSONField(blank=True, null=True, db_comment='Arch')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    customize_show = models.BooleanField(blank=True, null=True, db_comment='Customize Show')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'theme_ir_ui_view'
        db_table_comment = 'Theme UI View'


class ThemeWebsiteMenu(models.Model):
    page = models.ForeignKey('ThemeWebsitePage', models.DO_NOTHING, blank=True, null=True, db_comment='Page')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='themewebsitemenu_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    url = models.CharField(blank=True, null=True, db_comment='Url')
    mega_menu_classes = models.CharField(blank=True, null=True, db_comment='Mega Menu Classes')
    name = models.JSONField(db_comment='Name')
    mega_menu_content = models.TextField(blank=True, null=True, db_comment='Mega Menu Content')
    new_window = models.BooleanField(blank=True, null=True, db_comment='New Window')
    use_main_menu_as_parent = models.BooleanField(blank=True, null=True, db_comment='Use Main Menu As Parent')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'theme_website_menu'
        db_table_comment = 'Website Theme Menu'


class ThemeWebsitePage(models.Model):
    view = models.ForeignKey(ThemeIrUiView, models.DO_NOTHING, db_comment='View')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='themewebsitepage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    url = models.CharField(blank=True, null=True, db_comment='Url')
    header_color = models.CharField(blank=True, null=True, db_comment='Header Color')
    website_indexed = models.BooleanField(blank=True, null=True, db_comment='Page Indexed')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')
    is_new_page_template = models.BooleanField(blank=True, null=True, db_comment='New Page Template')
    header_overlay = models.BooleanField(blank=True, null=True, db_comment='Header Overlay')
    header_visible = models.BooleanField(blank=True, null=True, db_comment='Header Visible')
    footer_visible = models.BooleanField(blank=True, null=True, db_comment='Footer Visible')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'theme_website_page'
        db_table_comment = 'Website Theme Page'


class UomCategory(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='uomcategory_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Unit of Measure Category')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    is_pos_groupable = models.BooleanField(blank=True, null=True, db_comment='Group Products in POS')

    class Meta:
        managed = False
        db_table = 'uom_category'
        db_table_comment = 'Product UoM Categories'


class UomUom(models.Model):
    category = models.ForeignKey(UomCategory, models.DO_NOTHING, db_comment='Category')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='uomuom_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    uom_type = models.CharField(db_comment='Type')
    name = models.JSONField(db_comment='Unit of Measure')
    factor = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Ratio')
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Rounding Precision')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    l10n_in_code = models.CharField(blank=True, null=True, db_comment='Indian GST UQC')

    class Meta:
        managed = False
        db_table = 'uom_uom'
        db_table_comment = 'Product Unit of Measure'


class UpdateProductAttributeValue(models.Model):
    attribute_value = models.ForeignKey(ProductAttributeValue, models.DO_NOTHING, db_comment='Attribute Value')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='updateproductattributevalue_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    mode = models.CharField(blank=True, null=True, db_comment='Mode')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'update_product_attribute_value'
        db_table_comment = 'Update product attribute value'


class UtmCampaign(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, db_comment='Responsible')
    stage = models.ForeignKey('UtmStage', models.DO_NOTHING, db_comment='Stage')
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='utmcampaign_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='utmcampaign_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(unique=True, db_comment='Campaign Identifier')
    title = models.JSONField(db_comment='Campaign Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    is_auto_campaign = models.BooleanField(blank=True, null=True, db_comment='Automatically Generated Campaign')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True, db_comment='Company')
    ab_testing_winner_mailing = models.ForeignKey(MailingMailing, models.DO_NOTHING, blank=True, null=True, db_comment='A/B Campaign Winner Mailing')
    ab_testing_winner_selection = models.CharField(blank=True, null=True, db_comment='Winner Selection')
    ab_testing_completed = models.BooleanField(blank=True, null=True, db_comment='A/B Testing Campaign Finished')
    ab_testing_schedule_datetime = models.DateTimeField(blank=True, null=True, db_comment='Send Final On')

    class Meta:
        managed = False
        db_table = 'utm_campaign'
        db_table_comment = 'UTM Campaign'


class UtmMedium(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='utmmedium_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(unique=True, db_comment='Medium Name')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'utm_medium'
        db_table_comment = 'UTM Medium'


class UtmSource(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='utmsource_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(unique=True, db_comment='Source Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'utm_source'
        db_table_comment = 'UTM Source'


class UtmStage(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='utmstage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'utm_stage'
        db_table_comment = 'Campaign Stage'


class UtmTag(models.Model):
    color = models.IntegerField(blank=True, null=True, db_comment='Color Index')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='utmtag_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(unique=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'utm_tag'
        db_table_comment = 'UTM Tag'


class UtmTagRel(models.Model):
    pk = models.CompositePrimaryKey('tag_id', 'campaign_id')
    tag = models.ForeignKey(UtmCampaign, models.DO_NOTHING)
    campaign = models.ForeignKey(UtmTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'utm_tag_rel'
        db_table_comment = 'RELATION BETWEEN utm_campaign AND utm_tag'


class ValidateAccountMove(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='validateaccountmove_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    force_post = models.BooleanField(blank=True, null=True, db_comment='Force')
    ignore_abnormal_date = models.BooleanField(blank=True, null=True, db_comment='Ignore Abnormal Date')
    ignore_abnormal_amount = models.BooleanField(blank=True, null=True, db_comment='Ignore Abnormal Amount')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'validate_account_move'
        db_table_comment = 'Validate Account Move'


class WebEditorConverterTest(models.Model):
    integer = models.IntegerField(blank=True, null=True, db_comment='Integer')
    many2one = models.ForeignKey('WebEditorConverterTestSub', models.DO_NOTHING, db_column='many2one', blank=True, null=True, db_comment='Many2One')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='webeditorconvertertest_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    char = models.CharField(blank=True, null=True, db_comment='Char')
    selection_str = models.CharField(blank=True, null=True, db_comment="Lorsqu'un pancake prend l'avion à destination de Toronto et qu'il fait une escale technique à St Claude, on dit:")
    date = models.DateField(blank=True, null=True, db_comment='Date')
    html = models.TextField(blank=True, null=True, db_comment='Html')
    text = models.TextField(blank=True, null=True, db_comment='Text')
    numeric = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Numeric')
    datetime = models.DateTimeField(blank=True, null=True, db_comment='Datetime')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    float = models.FloatField(blank=True, null=True, db_comment='Float')
    binary = models.BinaryField(blank=True, null=True, db_comment='Binary')

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test'
        db_table_comment = 'Web Editor Converter Test'


class WebEditorConverterTestSub(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='webeditorconvertertestsub_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(blank=True, null=True, db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test_sub'
        db_table_comment = 'Web Editor Converter Subtest'


class WebTourTour(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='webtourtour_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(unique=True, db_comment='Name')
    url = models.CharField(blank=True, null=True, db_comment='Starting URL')
    rainbow_man_message = models.JSONField(blank=True, null=True, db_comment='Rainbow Man Message')
    custom = models.BooleanField(blank=True, null=True, db_comment='Custom')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'web_tour_tour'
        db_table_comment = 'Tours'


class WebTourTourStep(models.Model):
    tour = models.ForeignKey(WebTourTour, models.DO_NOTHING, db_comment='Tour')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='webtourtourstep_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    trigger = models.CharField(db_comment='Trigger')
    content = models.CharField(blank=True, null=True, db_comment='Content')
    run = models.CharField(blank=True, null=True, db_comment='Run')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'web_tour_tour_step'
        db_table_comment = "Tour's step"


class Website(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, db_comment='Company',related_name='website_company_set')
    default_lang = models.ForeignKey(ResLang, models.DO_NOTHING, db_comment='Default Language')
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, db_comment='Public User',related_name='website_user_set')
    theme = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True, db_comment='Theme',related_name='website_theme_set')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', related_name='website_create_uid_set', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='website_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Website Name')
    domain = models.CharField(unique=True, blank=True, null=True, db_comment='Website Domain')
    social_twitter = models.CharField(blank=True, null=True, db_comment='X Account')
    social_facebook = models.CharField(blank=True, null=True, db_comment='Facebook Account')
    social_github = models.CharField(blank=True, null=True, db_comment='GitHub Account')
    social_linkedin = models.CharField(blank=True, null=True, db_comment='LinkedIn Account')
    social_youtube = models.CharField(blank=True, null=True, db_comment='Youtube Account')
    social_instagram = models.CharField(blank=True, null=True, db_comment='Instagram Account')
    social_tiktok = models.CharField(blank=True, null=True, db_comment='TikTok Account')
    google_analytics_key = models.CharField(blank=True, null=True, db_comment='Google Analytics Key')
    google_search_console = models.CharField(blank=True, null=True, db_comment='Google Search Console')
    google_maps_api_key = models.CharField(blank=True, null=True, db_comment='Google Maps API Key')
    plausible_shared_key = models.CharField(blank=True, null=True, db_comment='Plausible Shared Key')
    plausible_site = models.CharField(blank=True, null=True, db_comment='Plausible Site')
    cdn_url = models.CharField(blank=True, null=True, db_comment='CDN Base URL')
    homepage_url = models.CharField(blank=True, null=True, db_comment='Homepage Url')
    auth_signup_uninvited = models.CharField(blank=True, null=True, db_comment='Customer Account')
    custom_blocked_third_party_domains = models.TextField(blank=True, null=True, db_comment='User list of blocked 3rd-party domains')
    cdn_filters = models.TextField(blank=True, null=True, db_comment='CDN Filters')
    custom_code_head = models.TextField(blank=True, null=True, db_comment='Custom <head> code')
    custom_code_footer = models.TextField(blank=True, null=True, db_comment='Custom end of <body> code')
    robots_txt = models.TextField(blank=True, null=True, db_comment='Robots.txt')
    auto_redirect_lang = models.BooleanField(blank=True, null=True, db_comment='Autoredirect Language')
    cookies_bar = models.BooleanField(blank=True, null=True, db_comment='Cookies Bar')
    configurator_done = models.BooleanField(blank=True, null=True, db_comment='Configurator Done')
    block_third_party_domains = models.BooleanField(blank=True, null=True, db_comment='Block 3rd-party domains')
    has_social_default_image = models.BooleanField(blank=True, null=True, db_comment='Has Social Default Image')
    cdn_activated = models.BooleanField(blank=True, null=True, db_comment='Content Delivery Network (CDN)')
    specific_user_account = models.BooleanField(blank=True, null=True, db_comment='Specific User Account')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    salesperson = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='website_salesperson_set', blank=True, null=True, db_comment='Salesperson')
    salesteam = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True, db_comment='Sales Team')
    cart_recovery_mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True, db_comment='Cart Recovery Email')
    shop_ppg = models.IntegerField(blank=True, null=True, db_comment='Number of products in the grid on the shop')
    shop_ppr = models.IntegerField(blank=True, null=True, db_comment='Number of grid columns on the shop')
    product_page_grid_columns = models.IntegerField(blank=True, null=True, db_comment='Product Page Grid Columns')
    show_line_subtotals_tax_selection = models.CharField(db_comment='Line Subtotals Tax Display')
    add_to_cart_action = models.CharField(blank=True, null=True, db_comment='Add To Cart Action')
    account_on_checkout = models.CharField(blank=True, null=True, db_comment='Customer Accounts')
    shop_gap = models.CharField(blank=True, null=True, db_comment='Grid-gap on the shop')
    shop_default_sort = models.CharField(db_comment='Shop Default Sort')
    product_page_image_layout = models.CharField(db_comment='Product Page Image Layout')
    product_page_image_width = models.CharField(db_comment='Product Page Image Width')
    product_page_image_spacing = models.CharField(db_comment='Product Page Image Spacing')
    ecommerce_access = models.CharField(db_comment='Ecommerce Access')
    contact_us_button_url = models.JSONField(blank=True, null=True, db_comment='Contact Us Button URL')
    prevent_zero_price_sale_text = models.JSONField(blank=True, null=True, db_comment='Text to show instead of price')
    enabled_portal_reorder_button = models.BooleanField(blank=True, null=True, db_comment='Re-order From Portal')
    send_abandoned_cart_email = models.BooleanField(blank=True, null=True, db_comment='Send email to customers who abandoned their cart.')
    prevent_zero_price_sale = models.BooleanField(blank=True, null=True, db_comment="Hide 'Add To Cart' when price = 0")
    cart_abandoned_delay = models.FloatField(blank=True, null=True, db_comment='Abandoned Delay')
    google_places_api_key = models.CharField(blank=True, null=True, db_comment='Google Places API Key')
    warehouse = models.ForeignKey(StockWarehouse, models.DO_NOTHING, blank=True, null=True, db_comment='Warehouse')
    channel = models.ForeignKey(ImLivechatChannel, models.DO_NOTHING, blank=True, null=True, db_comment='Website Live Chat Channel')
    newsletter = models.ForeignKey(MailingList, models.DO_NOTHING, blank=True, null=True, db_comment='Newsletter List')

    class Meta:
        managed = False
        db_table = 'website'
        db_table_comment = 'Website'


class WebsiteBaseUnit(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websitebaseunit_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.JSONField(db_comment='Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_base_unit'
        db_table_comment = 'Unit of Measure for price per unit on eCommerce products.'


class WebsiteConfiguratorFeature(models.Model):
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    page_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True, db_comment='Page View')
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True, db_comment='Module')
    menu_sequence = models.IntegerField(blank=True, null=True, db_comment='Menu Sequence')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websiteconfiguratorfeature_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    icon = models.CharField(blank=True, null=True, db_comment='Icon')
    iap_page_code = models.CharField(blank=True, null=True, db_comment='Iap Page Code')
    website_config_preselection = models.CharField(blank=True, null=True, db_comment='Website Config Preselection')
    feature_url = models.CharField(blank=True, null=True, db_comment='Feature Url')
    name = models.JSONField(blank=True, null=True, db_comment='Name')
    description = models.JSONField(blank=True, null=True, db_comment='Description')
    menu_company = models.BooleanField(blank=True, null=True, db_comment='Menu Company')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_configurator_feature'
        db_table_comment = 'Website Configurator Feature'


class WebsiteControllerPage(models.Model):
    website = models.ForeignKey(Website, models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    view = models.ForeignKey(IrUiView, models.DO_NOTHING, db_comment='Listing view')
    record_view = models.ForeignKey(IrUiView, models.DO_NOTHING, related_name='websitecontrollerpage_record_view_set', blank=True, null=True, db_comment='Record view')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websitecontrollerpage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='The name is used to generate the URL and is shown in the browser title bar')
    name_slugified = models.CharField(unique=True, blank=True, null=True, db_comment='URL')
    record_domain = models.CharField(blank=True, null=True, db_comment='Domain')
    default_layout = models.CharField(blank=True, null=True, db_comment='Default Layout')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_controller_page'
        db_table_comment = 'Model Page'


class WebsiteCustomBlockedThirdPartyDomains(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websitecustomblockedthirdpartydomains_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    content = models.TextField(blank=True, null=True, db_comment='Content')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_custom_blocked_third_party_domains'
        db_table_comment = 'User list of blocked 3rd-party domains'


class WebsiteEventMenu(models.Model):
    menu = models.ForeignKey('WebsiteMenu', models.DO_NOTHING, blank=True, null=True, db_comment='Menu')
    event = models.ForeignKey(EventEvent, models.DO_NOTHING, blank=True, null=True, db_comment='Event')
    view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True, db_comment='View')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websiteeventmenu_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    menu_type = models.CharField(db_comment='Menu Type')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_event_menu'
        db_table_comment = 'Website Event Menu'


class WebsiteLangRel(models.Model):
    pk = models.CompositePrimaryKey('website_id', 'lang_id')
    website = models.ForeignKey(Website, models.DO_NOTHING)
    lang = models.ForeignKey(ResLang, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'website_lang_rel'
        db_table_comment = 'RELATION BETWEEN website AND res_lang'


class WebsiteMenu(models.Model):
    page = models.ForeignKey('WebsitePage', models.DO_NOTHING, blank=True, null=True, db_comment='Related Page')
    controller_page = models.ForeignKey(WebsiteControllerPage, models.DO_NOTHING, blank=True, null=True, db_comment='Related Model Page')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    website = models.ForeignKey(Website, models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='Parent Menu')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websitemenu_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    theme_template = models.ForeignKey(ThemeWebsiteMenu, models.DO_NOTHING, blank=True, null=True, db_comment='Theme Template')
    url = models.CharField(blank=True, null=True, db_comment='Url')
    parent_path = models.CharField(blank=True, null=True, db_comment='Parent Path')
    mega_menu_classes = models.CharField(blank=True, null=True, db_comment='Mega Menu Classes')
    name = models.JSONField(db_comment='Menu')
    mega_menu_content = models.JSONField(blank=True, null=True, db_comment='Mega Menu Content')
    new_window = models.BooleanField(blank=True, null=True, db_comment='New Window')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_menu'
        db_table_comment = 'Website Menu'


class WebsitePage(models.Model):
    website = models.ForeignKey(Website, models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    view = models.ForeignKey(IrUiView, models.DO_NOTHING, db_comment='View')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websitepage_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    theme_template = models.ForeignKey(ThemeWebsitePage, models.DO_NOTHING, blank=True, null=True, db_comment='Theme Template')
    url = models.CharField(db_comment='Page URL')
    header_color = models.CharField(blank=True, null=True, db_comment='Header Color')
    header_text_color = models.CharField(blank=True, null=True, db_comment='Header Text Color')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')
    website_indexed = models.BooleanField(blank=True, null=True, db_comment='Is Indexed')
    is_new_page_template = models.BooleanField(blank=True, null=True, db_comment='New Page Template')
    header_overlay = models.BooleanField(blank=True, null=True, db_comment='Header Overlay')
    header_visible = models.BooleanField(blank=True, null=True, db_comment='Header Visible')
    footer_visible = models.BooleanField(blank=True, null=True, db_comment='Footer Visible')
    date_publish = models.DateTimeField(blank=True, null=True, db_comment='Publishing Date')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_page'
        db_table_comment = 'Page'


class WebsitePageProperties(models.Model):
    target_model = models.ForeignKey(WebsitePage, models.DO_NOTHING, blank=True, null=True, db_comment='Target Model')
    website = models.ForeignKey(Website, models.DO_NOTHING, db_comment='Website')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websitepageproperties_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    old_url = models.CharField(blank=True, null=True, db_comment='Old Url')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_page_properties'
        db_table_comment = 'Page Properties'


class WebsitePagePropertiesBase(models.Model):
    website = models.ForeignKey(Website, models.DO_NOTHING, db_comment='Website')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websitepagepropertiesbase_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    target_model_id = models.CharField(db_comment='Target Model')
    url = models.CharField(db_comment='Url')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_page_properties_base'
        db_table_comment = 'Page Properties Base'


class WebsiteRewrite(models.Model):
    website = models.ForeignKey(Website, models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    route = models.ForeignKey('WebsiteRoute', models.DO_NOTHING, blank=True, null=True, db_comment='Route')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websiterewrite_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Name')
    url_from = models.CharField(blank=True, null=True, db_comment='URL from')
    url_to = models.CharField(blank=True, null=True, db_comment='URL to')
    redirect_type = models.CharField(blank=True, null=True, db_comment='Action')
    active = models.BooleanField(blank=True, null=True, db_comment='Active')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_rewrite'
        db_table_comment = 'Website rewrite'


class WebsiteRobots(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websiterobots_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    content = models.TextField(blank=True, null=True, db_comment='Content')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_robots'
        db_table_comment = 'Robots.txt Editor'


class WebsiteRoute(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websiteroute_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    path = models.CharField(blank=True, null=True, db_comment='Route')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_route'
        db_table_comment = 'All Website Route'


class WebsiteSaleExtraField(models.Model):
    website = models.ForeignKey(Website, models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    sequence = models.IntegerField(blank=True, null=True, db_comment='Sequence')
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING, db_comment='Field')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websitesaleextrafield_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'website_sale_extra_field'
        db_table_comment = 'E-Commerce Extra Info Shown on product page'


class WebsiteSnippetFilter(models.Model):
    website = models.ForeignKey(Website, models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    action_server = models.ForeignKey(IrActServer, models.DO_NOTHING, blank=True, null=True, db_comment='Server Action')
    filter = models.ForeignKey(IrFilters, models.DO_NOTHING, blank=True, null=True, db_comment='Filter')
    limit = models.IntegerField(db_comment='Limit')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websitesnippetfilter_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    field_names = models.CharField(db_comment='Field Names')
    name = models.JSONField(db_comment='Name')
    is_published = models.BooleanField(blank=True, null=True, db_comment='Is Published')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    product_cross_selling = models.BooleanField(blank=True, null=True, db_comment='About cross selling products')

    class Meta:
        managed = False
        db_table = 'website_snippet_filter'
        db_table_comment = 'Website Snippet Filter'


class WebsiteTrack(models.Model):
    visitor = models.ForeignKey('WebsiteVisitor', models.DO_NOTHING, db_comment='Visitor')
    page = models.ForeignKey(WebsitePage, models.DO_NOTHING, blank=True, null=True, db_comment='Page')
    url = models.TextField(blank=True, null=True, db_comment='Url')
    visit_datetime = models.DateTimeField(db_comment='Visit Date')
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True, db_comment='Product')

    class Meta:
        managed = False
        db_table = 'website_track'
        db_table_comment = 'Visited Pages'


class WebsiteVisitor(models.Model):
    website = models.ForeignKey(Website, models.DO_NOTHING, blank=True, null=True, db_comment='Website')
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, db_comment='Contact')
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True, db_comment='Country')
    lang = models.ForeignKey(ResLang, models.DO_NOTHING, blank=True, null=True, db_comment='Language')
    visit_count = models.IntegerField(blank=True, null=True, db_comment='# Visits')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='websitevisitor_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    access_token = models.CharField(unique=True, db_comment='Access Token')
    timezone = models.CharField(blank=True, null=True, db_comment='Timezone')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='First Connection')
    last_connection_datetime = models.DateTimeField(blank=True, null=True, db_comment='Last Connection')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')
    livechat_operator = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='websitevisitor_livechat_operator_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_visitor'
        db_table_comment = 'Website Visitor'


class WizardIrModelMenuCreate(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING, db_comment='Parent Menu')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, db_comment='Created by')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', related_name='wizardirmodelmenucreate_write_uid_set', blank=True, null=True, db_comment='Last Updated by')
    name = models.CharField(db_comment='Menu Name')
    create_date = models.DateTimeField(blank=True, null=True, db_comment='Created on')
    write_date = models.DateTimeField(blank=True, null=True, db_comment='Last Updated on')

    class Meta:
        managed = False
        db_table = 'wizard_ir_model_menu_create'
        db_table_comment = 'Create Menu Wizard'
