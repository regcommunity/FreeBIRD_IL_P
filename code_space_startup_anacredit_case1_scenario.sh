#!/bin/bash
cd birds_nest
pip install --upgrade pip --quiet
python -m pip install django==5.1.3 --quiet
python -m pip install pyecore==0.15.1 --quiet
python -m pip install pytest==8.3.4 --quiet
python -m pip install pytest-xdist==3.6.1 --quiet
python -m pip install ruff==0.9.7 --quiet
python -m pip install unidecode==1.3.8 --quiet
python pybirdai/utils/run_tests.py --uv "False" --reg-tid "F_05_01_REF_FINREP_3_0" --dp-suffix "152589_REF" --dp-value 83491250 --scenario  "loan_and_guarantee_scenario_1"
python manage.py runserver
