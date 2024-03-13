# returnalyze-kpis
This Python library is designed for the dynamic generation of kpi values for use within dashboard and anaytics team. It facilitates the easy retrieval of KPIs by applying filters such as client identifiers, environment settings, and date ranges. This modular approach not only enhances the insight generation process but also ensures adaptability for future requirements.

## Features
Generate KPI values dynamically 
Reusable across different modules, including insight generation processes.
Supports extensive filtering capabilities (client, environment, dates, etc.).
Designed for easy expansion to accommodate future enhancements.



## Maintaince

Create your own account in [pypi.org](https://pypi.org/) 
@qqzhang72 to add you in pypi collabaror. 

todo: Add more steps here. 


## Install pacakges in other repos
Using version 0.1.1 as example 

1. Append  `kpisQueryGeneration==0.1.1` in either setup.py file or requirement.txt file.

2. Run cmd below in your teminal to install the kpisQueryGeneration
```
pip install kpisQueryGeneration==0.1.1 
```
3. Import library into the file and use it. For instance in returnalyze repo, in `returnalyze/resources/graphql/resolvers/reports/return_summary/kpi_summary.py` we want to use generate_template function from query_templating.query_utils in kpisQueryGeneration pacakge.
```
# Importing a specific utility from the submodule
from kpis_query_generation.query_templating.query_utils import generate_template as test_generate_template

...
def fetch_kpi_data(...):
    # test here
    template = test_generate_template(return_rate_type, kpi_fetch_template, raw_kpi_fetch_template)

```
