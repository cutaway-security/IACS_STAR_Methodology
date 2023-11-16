#!/usr/bin/env python


"""
Installing requirements:

pip install -r requirements.txt

or manual with:

pip install PyYAML
pip install -U Jinja2

Usage:

./generate_calculator.py

The above command would generate the "iacs_star_calculator.html" in the html folder based on the default config
"default.yaml". Changing the config file is possible using parameter "config". Assuming you have created a config called
pharma.yaml this could be done using the following command.

./generate_calculator.py --config pharma.yaml

"""


import argparse
import sys

import yaml
from jinja2 import Environment, FileSystemLoader


def is_average(v1:float, v2:float, v3:float, v4:float, expected:float = 1):
    result = (v1 + v2 + v3 +v4) / 4
    if result == expected:
        return True
    return False


def main(config_file:str, template_file:str):
    with open(config_file, 'r') as f:

        try:
            config =  yaml.safe_load(f)
            outfile_name = config["outfile"]["filename"]
            outfile = f"html/{outfile_name}"
            print(f"[*] Reading config file {config_file}")

            environment = Environment(loader=FileSystemLoader("templates/"))
            template = environment.get_template("calculator_template.html")

            print(f"[*] Using template file {template_file}")

            tif_average = is_average(config["risk_weight"]["TIF_LC"],config["risk_weight"]["TIF_LI"],
                                     config["risk_weight"]["TIF_LA"], config["risk_weight"]["TIF_LAC"])
            if not tif_average:
                print(f"[!] TIF risk weights must have an average of 1.")
                sys.exit()

            sif_average = is_average(config["risk_weight"]["SIF_ED"], config["risk_weight"]["SIF_PD"],
                                     config["risk_weight"]["SIF_SE"], config["risk_weight"]["SIF_R"])
            if not sif_average:
                print(f"[!] TIF risk weights must have an average of 1.")
                sys.exit()

            context = {
                "option_strings": config["option_strings"],
                "risk_weight": config["risk_weight"]
            }

            with open(outfile, mode="w", encoding="utf-8") as results:
                results.write(template.render(context))
                print(f"[*] Wrote html file {outfile}")

        except yaml.YAMLError as exc:
            print(exc)



if __name__=="__main__":
    parser = argparse.ArgumentParser(description="File that generates a static calculator file from yaml input")
    parser.add_argument("--config", metavar="FILE", type=str, required=False, default="config/default.yaml")
    parser.add_argument("--template", metavar="FILE", type=str, required=False, default="html/default.yaml")
    args = parser.parse_args()

    main(config_file=args.config, template_file=args.template)