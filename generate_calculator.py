#!/usr/bin/env python


"""
pip install PyYAML
pip install -U Jinja2

"""


import argparse
import yaml
from jinja2 import Environment, FileSystemLoader


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

            context = {
                "option_strings": config["option_strings"]
            }

            with open(outfile, mode="w", encoding="utf-8") as results:
                results.write(template.render(context))
                print(f"[!] Wrote html file {outfile}")
        except yaml.YAMLError as exc:
            print(exc)




if __name__=="__main__":
    parser = argparse.ArgumentParser(description="File that generates a static calculator file from yaml input")
    parser.add_argument("--config", metavar="FILE", type=str, required=False, default="config/default.yaml")
    parser.add_argument("--template", metavar="FILE", type=str, required=False, default="html/default.yaml")
    args = parser.parse_args()

    main(config_file=args.config, template_file=args.template)