from policyengine_us.model_api import *


class ct_withheld_income_tax(Variable):
    value_type = float
    entity = Person
    label = "Connecticut withheld income tax"
    defined_for = StateCode.CT
    unit = USD
    definition_period = YEAR

    def formula(person, period, parameters):
        employment_income = person("irs_employment_income", period)
        p = parameters(period).gov.states.ct.tax.income
        # Since Connecticut does not have a standard deduction, we apply the maximum
        # personal exemption amount
        personal_exemptions = p.exemptions.personal.max_amount["SINGLE"]
        reduced_employment_income = max_(
            employment_income - personal_exemptions, 0
        )
        return p.rates.single.calc(reduced_employment_income)
