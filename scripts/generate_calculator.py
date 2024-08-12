#!/usr/bin/env python3

"""
Installing requirements:

    pip install -r requirements.txt

or manual with:

    pip install PyYAML
    pip install -U Jinja2

Usage:

Generate a new calculator using the default template "calculator_template.ctpl" using the default configuration file "default.yaml".

    ./generate_calculator.py

Generate a new calculator using the default template "calculator_template.ctpl" using the default configuration file "pharma.yaml".

    ./generate_calculator.py --config pharma.yaml

Generate a new calculator using the default template "dark_template.ctpl" using the default configuration file "papermill.yaml".

    ./generate_calculator.py -c papermill.yaml --template dark_template.ctpl

"""

import argparse
import sys, os

import yaml
from jinja2 import Environment, FileSystemLoader

######################
# Compute risk average
######################
def is_average(v1:float, v2:float, v3:float, v4:float, expected:float = 1):
    result = (v1 + v2 + v3 +v4) / 4
    if result == expected:
        return True
    return False

######################
# Generate Calculator
######################
def main(config_file:str, template_file:str):
    # Setup File Paths that are OS independent
    iacs_dir           = os.path.dirname(os.getcwd())
    iacs_config_dir    = os.path.join(iacs_dir,"config")
    iacs_config_file   = os.path.join(iacs_config_dir,config_file)
    iacs_template_dir  = os.path.join(iacs_dir,"templates")
    iacs_template_file = os.path.join(iacs_template_dir,template_file)
    iacs_out_dir       = os.path.join(iacs_dir,"html")

    '''DEBUGGING
    print(f"[*] Starting Configuration:")
    print(f"    {iacs_config_file}")
    print(f"    {iacs_template_file}")
    '''
    
    # Do not stomp previous calculators
    if not os.path.exists(iacs_config_file):
        print(f"\n[!] Error: {iacs_config_file} does not exist.\n")
        sys.exit()

    # Do not stomp previous calculators
    if not os.path.exists(iacs_template_file):
        print(f"\n[!] Error: {iacs_template_file} does not exist.\n")
        sys.exit()

    # Generate new calculator
    with open(iacs_config_file, 'r') as f:
        
        # Process configuration file
        print(f"[*] Reading config file: {config_file}")

        # Read YAML file
        try:
            config =  yaml.safe_load(f)        
        except yaml.YAMLError as exc:
            print(f"[!] Error: Reading YAML configuration file: {exc}")
            sys.exit()

        outfile_name = config["outfile"]["filename"]
        outfile = os.path.join(iacs_out_dir,outfile_name)

        # Do not stomp previous calculators
        if os.path.exists(outfile):
            print(f"\n[!] Error: {outfile} exists. Please update {iacs_config_file} or move old calculator.\n")
            sys.exit()

        # Prepare calculator from template file
        print(f"[*] Using template file: {template_file}")
        environment = Environment(loader=FileSystemLoader(iacs_template_dir))
        template = environment.get_template(template_file)

        tif_average = is_average(
            config["risk_weight"]["TIF_LC"],
            config["risk_weight"]["TIF_LI"],
            config["risk_weight"]["TIF_LA"], 
            config["risk_weight"]["TIF_LAC"]
        )

        if not tif_average:
            print(f"[!] TIF risk weights must have an average of 1.")
            sys.exit()

        sif_average = is_average(
            config["risk_weight"]["SIF_ED"], 
            config["risk_weight"]["SIF_PD"],
            config["risk_weight"]["SIF_SE"], 
            config["risk_weight"]["SIF_R"]
        )

        if not sif_average:
            print(f"[!] TIF risk weights must have an average of 1.")
            sys.exit()

        context = {
            "option_strings": config["option_strings"],
            "risk_weight": config["risk_weight"],
            "filename": config["outfile"]["filename"]
        }

        with open(outfile, mode="w", encoding="utf-8") as results:
            results.write(template.render(context))
            print(f"[*] Wrote new calculator html file: {outfile}")


        print(f"[*] To start a local web server open a terminal, change to the \'html\' directory, and run \'python3 -m http.server 9000\'")
        print(f"[*] Use new calculator by navigating to http://localhost:9000:/{outfile_name}")


if __name__=="__main__":
    # Command line arguments
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,description="Generate a custom static IACS calculator file from YAML input.")
    parser.add_argument("-c","--config", metavar="FILENAME.yaml", type=str, required=False, default="default.yaml",help='Filename for the YAML configuration file.')
    parser.add_argument("-t","--template", metavar="FILENAME.ctpl", type=str, required=False, default="calculator_template.ctpl",help="Filename for the calculator\'s template file.")
    args = parser.parse_args()

    # Process calculator
    main(config_file=args.config, template_file=args.template)