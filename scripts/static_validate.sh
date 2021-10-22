#!/usr/bin/env bash

echo 'Running ISort Now..................'
# run isort to make sure imports are formatted
isort --atomic --profile black taskify


echo 'Running Black Now..................'
# run black - make sure everyone uses same python style
black --skip-string-normalization --line-length 120 taskify

black --skip-string-normalization --line-length 120 --check taskify

## run mypy for the configured modules in the src directory
#echo 'Running MyPy Now..................'
#
#cd src
#
#mypy accounts admin app_test assetfinancing banking communication coupons credibuilder credit_scoring customer_support card datawarehouse deviceinfo external freshdesk investor lib lms loan loans marketing payment referrals transaction webapp savings service
#
#cd ..
#
## run bandit - A security linter from OpenStack Security
#echo 'Running Bandit Now..................'
#bandit -r src
#
## python static analysis
#echo 'Running Prospector Now..................'
#prospector --profile-path=. --profile=.prospector.yml --path=src --ignore-patterns=static
