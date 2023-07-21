# IACS Risk Rating Methodology (IRRM)
A risk rating calculation methodology that uses the [OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology) as a basis. 

## Contributions

* Author: Don C. Weber
* IACS/OT Contributors: Oscar Delgado, Danielle Jablanski
* IT/Infosec Contributors: Jeff Williams (Author of original OWASP Risk Rating Methodology)

# Introduction

Security assessments and penetration testing of an Industrial and Automation Control Systems (IACS) / Operational Technology (OT) enviornment are two types of vulnerability assessments that feed information into the [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) risk assessment process. The Cyber Security Management System (CSMS) process, detailed in ISA/IEC-62443-2-1 standard, requires a detailed risk assessment which is outlined in full within the ISA/IEC-62443-3-2 standard. The detailed risk assessment requires that a vulnerability assessment is conducted to identify unmitigated risk. These vulnerability assessments required that the assessment findings be qualitatively rated according to the threat, likelihood, and concequences should the vulnerability be exploit and threat actor success realized. 

The IACS Risk Rating Methodology (IRRM) is intended to be a methodology to estimate the severity of identified risks to the IACS/OT environment. This methodology includes the classic qualitative risk calculation elements while adding the consequence considerations necessary for understanding risks to IACS/OT processes and equipment. Having a system in place that addresses IACS/OT concerns for rating risks will save time and eliminate arguing about prioritizations and improve countermeasure selection to quickly reduce risk. 

The authors have tried hard to make this model simple to use, while keeping enough detail for accurate risk estimates to be made. Please reference the section below on customization for more information about tailoring the model for use in a specific organization.

# Overview 

Over the years there has be a lot of debate about how to rate risk within industrial and automation control environments. Rating risk is difficult due to the varying ideas about likelihood, frequency, consequences, and impact ratings. This project is an effort to update the [OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology) to be usable when conducting security assessments and pentration tests within IACS/OT enviornments. It is not designed to replace an organization's risk rating methdodology. It is intended for assessment teams to use when a specific methodology has not been defined or when a quicker method is needed to quickly rate and reduce risk.

For background, there are other more mature, popular, or well established Risk Rating Methodologies that can be followed:

- [ISA/IEC 62443 Series of Standards](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)
- [NIST 800-30 - Guide for Conducting Risk Assessments](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final)
- [National Vulnerability Database (NVD) Common Vulnerability Scoring System Version 3 (CVSSv3) Calculator](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)
- [Government of Canada - Harmonized TRA Methodology](https://cyber.gc.ca/en/guidance/harmonized-tra-methodology-tra-1)
- Mozilla resources:
    - [Risk Assessment Summary](https://infosec.mozilla.org/guidelines/assessing_security_risk)
    - [Rapid Risk Assessment (RRA)](https://infosec.mozilla.org/guidelines/risk/rapid_risk_assessment.html)
- [The Blind Spot: How to Simply Calculate Cyber Attack Likelihood Using the Exploitability Assessment](https://www.cybersecureot.info/post/the-blind-spot-how-to-simply-calculate-cyber-attack-likelihood-using-the-exploitability-assessment)

The risk and vulnerability assessment process is augmented by threat modeling to identify and prioritize potential attack vectors and successful exploitations. The following are a list of methods to help with the threat modeling process:

- [First.org: Threat Modeling](https://www.first.org/global/sigs/cti/curriculum/threat-modelling)
- [The Operational esilience Framework](https://www.grf.org/orf)
- [Microsoft Threat Modeling Tool threats](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) - aka S.T.R.I.D.E.
- [Threat Assessment and Remediation Analysis (TARA)](https://www.mitre.org/news-insights/publication/threat-assessment-and-remediation-analysis-tara)
- [ICS Layered Threat Modeling](https://sansorg.egnyte.com/dl/fztutwiK5J)
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [OWASP Application Threat Modeling](https://owasp.org/www-community/Application_Threat_Modeling)
- [OWASP pytm](https://owasp.org/www-project-pytm/) Pythonic framework for threat modeling
- [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) threat modeling tool

The ISA/IEC 62443 CSMS Detailed Risk Assessment process requires that considerations for the criticality of processes, equipment, and procedures are calculated and documented. The following resources provide some details and insight into the considerations for this process. 

- [Critical infrastructure cybersecurity prioritization: A cross-sector methodology for ranking operational technology cyber scenarios and critical entities](https://www.atlanticcouncil.org/in-depth-research-reports/issue-brief/critical-infrastructure-cybersecurity-prioritization/)
- [Common Vulnerability Scoring System Version 4.0](https://www.first.org/cvss/v4-0/) - CVSS version 4.0 is the next generation of the Common Vulnerability Scoring System standard.

# Approach

The ISA/IEC-62443-2-1 standard outlines that risk is calculated by taking the likelihood that an event will occur and scaling it with the concequences should the event be realized. Hence the equation **Risk = Likelihood * Consequence**. The assignment of the likelihood and consequence variables is the typical debate. 

Most IACS/OT likelihood calculations, sometimes referred to as frequency, take into consideration the commonly understood cases of equipment failure. Industrial and automation equipment have specific usage tollerances that, when calculated with known usage, can provide a measurable likelihood that the equipment will experience a problem. This often results in a likelihood table that uses specific time tables for an event to occur.

- High: will occur in the next year
- Moderate: will occur in the next 10 years
- Low: no history of occurance and therefore unlikely

These typcial likelihood ratings are not applicable when considering cybersecurity and the likelihood or frequency that a threat actor will attempt to exploit a vulnerability. In 2008 the Federal Energy Regulatory Commission (FERC) determined that electric utilities required specific guidance to understand how to address likelihood and frequency when calculating risk. In [FERC Order 706 Mandatory Reliability Standards for Critical Infrastructure Protection](https://www.ferc.gov/sites/default/files/2020-04/E-2_11.pdf) the following guidance was provided:

- "Because there is insufficient data available to determine frequency, it should be assumed that an event will occur." 
- "Risk-based assessment methodology should focus on the consequences of an outage, not the likelihood of an outage.“

In the sections below, the factors that make up "likelihood" and "consequences" for IACS/OT environments are broken down as defined in the 'ISA/IEC-62443-3-2 Zone and Conduit Requirements (ZCR) 5: Perform a detailed cyber security risk assessment' section. The assessment team is shown how to leverage these factors to determine the overall severity for risks identified during a vulnerability assessment.

```
  Step 1: ZCR 5.1: Identify Threats
  Step 2: ZCR 5.2: Identify Vulnerabilities
  Step 3: ZCR 5.3: Factors for Estimating Consequences and Impact
  Step 4: ZCR 5.4: Factors for Estimating Likelihood
  Step 5: ZCR 5.5: Calculate Unmitigated Cybersecurity Risk
  Step 6: Deciding What to Fix
  Step 7: Customizing Your Risk Rating Model
```

## Step 1: Identify Threats (ISA/IEC-62443-3-2 ZCR 5.1)

Following the model of the OWASP risk rating system, there are a few factors that aid in the determination of risk. This effort has modified the OWASP model slightly to fit into the IACS/OT modle. These factors are used when modeling attack scenarios to prioritize assessment efforts. The fartors are also used when calculating the risk rating each vulnerability and will vary according to the specifics of the situation. These factors include: 

- a description of the threat actor group
- the capabilities or skill-level of the threat actors
- the possible motivations for the threat actors
- the opportunities provided to the threat actors by the environment's architecture
- the level of access achieved when successfully exploiting the vulnerability

### Threat Agent Factors

It is important to understand threat actor groups when considering the skills, motivation, opportunities, and population of potential attackers. There are many lists that outline specific threat actor groups that are known to attack IACS/OT environments. These include: [Wikipedia: threat actor](https://en.wikipedia.org/wiki/Threat_actor), [MITRE](https://attack.mitre.org/groups/), [Mandiant](https://www.mandiant.com/resources/insights/apt-groups), [Crowdstrike](https://www.crowdstrike.com/adversaries/), [Dragos](https://www.dragos.com/threat-groups/), and more. To perform vulnerabilitie assessments there needs to be an easier list that allows all stakeholders to agree. Each of these groups are more accurately defined by their skills, likelihood of success, and their primary objectives. The following is one possible breakdown of threat actors associated with IACS/OT environments, each with their own levels of skill, motivation, opportunities, and group size.

- **Malware**: Malicious programs that have a specific affect on vulnerable / compromised systems. This includes general malware, IACS/OT malware, and custom malware.
- **Script Kiddies**: Uses tools, techiques, and malware that are known, common, and easily accessible.
- **Cybercriminal**: An advanced group that have the maturity and financial backing to obtain or develop tools, hire technology experts, and time to conduct research and development to achieve goals.
- **Hacker**: Individuals that are mainly comprised of security researchers and sensationalists. Their activities are typcially limited to conducted vulnerability research on products. Select individuals may progress unauthorized access to understand risk and publically disclose information.
- **Competitor**: Direct competitors with team members that will have access to specific knowledge that will apply in the case of specialized software and equipment.
- **Employee**: Disgruntled and reckless employees that have privileged access to systems and devices as well as the knowledge about the technologies and networks.
- **Vendor**: Rogue vendor, integrator, or consultant that is disgruntled, reckless, or malicious. Have knowledge about technologies and may have privileged access to systems, networks, and devices.
- **Cyberwarrior**: Nation-state threat actors that typically operate in groups to achieve specific goals. Trained to live-off-the-land, steal credentials, and exfiltrate information. Has access to custom tools and malware designed to maintain persistence, propogate, and achieve their goals.

To compute the likelihood that a threat actor groups will be successful the following numerical breakdowns will be assigned to skill level, motivation, opportunity, and size categories. The level of each category can be estimated to calculate the Threat Agent Factor which will be used to computer the overall likelihood that an event will be realized.  

- **Skill Level** - How technically skilled is this group of threat agents? 
  - Limited Information Technology (IT), network, and no Operational Technology (OT) skills (1)
  - Moderate IT, limited network, and no OT technical skills (3)
  - Advanced IT, moderate network, and limited OT technical skills (5)
  - Advanced IT, advanced network, and moderate OT technical skills (6)
  - Advanced OT technical skills (8)
  - Security penetration skills and knowledge of OT technologies (9) 
- **Motive** - How motivated of the threat actors once they obtain access to the control environment? An excellent guide for this is the Impact column of the [MITRE ATT&CK ICS Matrix](https://attack.mitre.org/matrices/ics/).
  - No reward or intention to impact control environment (1)
  - Theft of operational data or equipment (2)
  - Create loss of view and control as a result of target-of-opportunity access to assets (3)
  - Limit access to fileshares and prevent view and control using common malware (5)
  - Prevent view and control using specially designed malware (6)
  - Manipulate view and control using privileged remote access and / or specially designed malware (8)
  - Prevent operation of safety equipment or cause a catastriphic failure (9)
- **Opportunity** - When accessing the control environment, how are the threat actors limited by deployed countermeasures? 
  - Physical access and local authentication is required and response time is less than fifteen minutes (0)
  - Physical access and local authentication is required but response time is more than fifteen minutes (1)
  - Physical and remote access is possible, local authentication required, and active monitoring is enabled (3)
  - Limited logging of physical or remote access but administrative privileges are required to access network devices, systems, and applications (5)
  - Undetected physical or remote access but administrative privileges are required to access network devices, systems, and applications (6)
  - Undetected physical or remote access that provides requires authentication to some network devices, systems, and applications (8)
  - Undetected physical or remote access that provides elevated permissions to network devices, systems, and applications (9)
- **Access** - What is the physical or remote access capabilities achieved by successful exploitation within the process? 
  - Physical owner/operator users (1)
  - Physical vendor / integrator users (2)
  - Physical non-malicious civilian users (4)
  - Remote owner/operator users (5)
  - Remote vendor / integrator users (7)
  - Physical malicious users (8)
  - Remote anonymous internet users (9)

## Step 2: Identify Vulnerabilities (ISA/IEC-62443-3-2 ZCR 5.2)

The identification of vulnerabilities depends on the type of vulnerability assessment being conducted. Every IACS/OT environment will have a list of vulnerabilities that are a combination of known hardware and software vulnerabilities, configuration vulnerabilities, and technology implementation vulnerabilities. Some vulnerabilities can be identified using online research i.e. the [NVD Vulnerabilities search page](https://nvd.nist.gov/vuln/search) and vendor cybersecurity resources pages. Configuration and implementation vulnerabilities are identified using passive and active vulnerability testing methods. The factors that play into rating identified vulnerabilities include:

- the ease of access
- the ease of exploitation
- public awareness of the vulnerability
- detection and response of attempts to exploit the vulnerability

### Vulnerability Factors

The next set of factors are related to understanding the identified vulnerability. The goal here is to estimate the 
likelihood of the particular vulnerability will be exploited and used to gain access to the environment, provide persistence on a system or device, and be used to achieve the threat actor's goals. To understand the vulnerability the factors involving access, exploitation, and public awareness should be considered. Additionally, one of the Foundational Requirements outlined in the ISA/IEC 62443 series of standards includes Timely Response to Events (TRE). This should be added to the factors when understanding the vulnerability within the IACS/OT environment.

- **Ease of Access** - How easy is it for this group of threat agents to access the environment and discover the existence of the vulnerability? 
  - Requires physical access to environment or OT device (1)
  - Requires physical access to environment or IT device (2)
  - Remotely accessible but countermeasures protecting OT technology (3)
  - Remotely accessible but countermeasures protecting IT technology (4)
  - Remotely accessible but no automated tools to discover for OT technology (6)
  - Remotely accessible but no automated tools to discover for IT technology (7)
  - Remotely accessible and automated tools available for IT technology (8)
  - Remotely accessible and automated tools available for OT technology (9)
- **Ease of Exploit** - How easy is it to actually exploit the vulnerability? 
  - No known proof of concept (1)
  - Countermeasures protecting OT technology (2)
  - Denial-of-Service possible but no code execution (3)
  - Custom scripts / tools can be made to exploit IT technology (5)
  - Custom scripts / tools can be made to exploit OT technology (6)
  - Automated tools available for IT technology (8)
  - Automated tools available for OT technology (9)
- **Awareness** - How well known is this vulnerability? 
  - Unknown OT Vulnerability (1)
  - Unknown IT Vulnerability (2)
  - Not publicly known but common [configuration vulnerability](https://cwe.mitre.org/) (3)
  - Publicly identified on vendor website or within [NVD Vulnerabilities database](https://nvd.nist.gov/vuln/search) but no known exploit available (5)
  - Publicly identified on vendor website or within [NVD Vulnerabilities database](https://nvd.nist.gov/vuln/search) no known exploit available but target threat actor group can develop exploit (6)
  - Publicly identified on vendor website, vulnerability databases, and exploit available in public forums, i.e. [Metasploit](https://www.metasploit.com/), [Exploit-DB](https://www.exploit-db.com/) (8)
  - Public identified and in [CISA Known Exploited Vulnerabilityes Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (9)
- **Detection/Response** - How likely is an exploit to be detected? 
  - Centrally logged with alerts and formal review and response plan (1)
  - Centrally logged with alerts and formal review but no response plan (3)
  - Centrally logged with alerts, but no formal review or response plan (6)
  - Centrally logged and without review (7)
  - Locally logged without review (8)
  - Not logged (9)

## Step 3: Estimating Consequences and Impact (ISA/IEC-62443-3-2 ZCR 5.3)

The original OWASP risk rating methodology used a combination of technical and business impact factors to analyze the impact when a vulnerability's exploitation was realized. While useful these are not the best ways to understand the impact of an exploited vulnerability to an IACS/OT enviornment. The Impact column of the [MITRE ATT&CK ICS Matrix](https://attack.mitre.org/matrices/ics/) provides good details about what can happen after successful exploitation. These Impacts are a combination of denial, loss, and manipulation to the process or locations that monitor the process. The FIRST.og [CVSSv4.0](https://www.first.org/cvss/v4-0/) scoring system has been updated to include a new supplemental metric group which includes rating factors that involve safety, automatable, recovery, value density, vulnerability response effort, and provider urgeny. Hence, the IRRM will estimate consequences and impacts using technical factors and safety factors.

### Technical Impact Factors

Technical impact can be broken down into factors aligned with the traditional security areas of concern: confidentiality, integrity, availability, and accountability. The goal is to estimate the magnitude of the impact on the system if the vulnerability were to be exploited.

- **Loss of Confidentiality** - How much data could be disclosed and how sensitive is it? 
  - Minimal architecture configuration data disclosed (2)
  - Minimal network configuration data but no device configuration data disclosed (4)
  - Extensive network configuration data and some device configuration data disclosed (6)
  - Some process network and device configuration data disclosed (7)
  - All process network and device configuration data disclosed (9)
- **Loss of Integrity** - How is the process' data changed and does it impact critical functions? 
  - Modification of historical data not used for control (1)
  - Modification of historical data used for control (2)
  - Local modification of set points used for non-critical functions (4)
  - Remote modification of set points used for non-critical functions (5)
  - Remote modification of device configurations used for non-critical functions (6)
  - Local modification of set points used for critical functions (7)
  - Remote modification of set points used for critical functions (8)
  - Remote modification of device configurations used for critical functions (9)
- **Loss of Availability** - How are production and safety services impacted? 
  - Minimal production interruption and easily recoverable (1)
  - Device or service interrupted but process not impacted (3)
  - Production services temperarily interrupted by easily recoverable (4)
  - Production services interrupted but does not affect other processes (6)
  - Production services interrupted and impacts other processes (7)
  - All production services completely lost (8)
  - Loss of process safety functionality (9)
- **Loss of Accountability** - Are the threat agents' actions traceable to an individual? 
  - Central logging, Multifactor Authentication (MFA), and cameras (1)
  - Central logging, Multifactor Authentication (MFA), but no cameras (2)
  - Local logging, Multifactor Authentication (MFA), and cameras but no central logging (3)
  - Local logging and cameras but no MFA and no central logging (5)
  - Local logging but no MFA, no central logging, and no cameras (7)
  - No local or central logging, no MFA, and no cameras (9)

~~~~~~~~~~~~~~~~~~~~~~~
**BELOW IS ORIGINAL AND REQUIRES UPDATING**
~~~~~~~~~~~~~~~~~~~~~~~

### Business Impact Factors

The business impact stems from the technical impact, but requires a deep understanding of what is 
important to the company running the application. In general, you should be aiming to support your 
risks with business impact, particularly if your audience is executive level. The business risk is 
what justifies investment in fixing security problems.

Many companies have an asset classification guide and/or a business impact reference to help formalize 
what is important to their business. These standards can help you focus on what's truly important for 
security. If these aren't available, then it is necessary to talk with people who understand the 
business to get their take on what's important.

The factors below are common areas for many businesses, but this area is even more unique to a company 
than the factors related to threat agent, vulnerability, and technical impact.

  - **Financial damage** - How much financial damage will result from an exploit? Less than the cost to fix the vulnerability (1), minor effect on annual profit (3), significant effect on annual profit (7), bankruptcy (9)

  - **Reputation damage** - Would an exploit result in reputation damage that would harm the business? Minimal damage (1), Loss of major accounts (4), loss of goodwill (5), brand damage (9)

  - **Non-compliance** - How much exposure does non-compliance introduce? Minor violation (2), clear violation (5), high profile violation (7)

  - **Privacy violation** - How much personally identifiable information could be disclosed? One individual (3), hundreds of people (5), thousands of people (7), millions of people (9)

## Step 4: Determining the Severity of the Risk

In this step, the likelihood estimate and the impact estimate are put together to calculate an overall 
severity for this risk.  This is done by figuring out whether the likelihood is low, medium, or high 
and then do the same for impact. The 0 to 9 scale is split into three parts:

<table width="40%" cellspacing="0" cellpadding="5" border="1" align="center">
<tr>
<th colspan="2" align="center">Likelihood and Impact Levels</th>
</tr>
<tr>
<td width="50%" align="center">0 to &lt;3</td>
<td width="50%" bgcolor="lightgreen" align="center">LOW</td>
</tr>
<tr>
<td align="center">3 to &lt;6</td>
<td bgcolor="yellow" align="center">MEDIUM</td>
</tr>
<tr>
<td align="center">6 to 9</td>
<td bgcolor="red" align="center">HIGH</td>
</tr>
</table>

### Informal Method

In many environments, there is nothing wrong with reviewing the factors and simply capturing the answers. 
The tester should think through the factors and identify the key "driving" factors that are controlling 
the result. The tester may discover that their initial impression was wrong by considering aspects of the 
risk that weren't obvious.

### Repeatable Method

If it is necessary to defend the ratings or make them repeatable, then it is necessary to go through a 
more formal process of rating the factors and calculating the result. Remember that there is quite a 
lot of uncertainty in these estimates and that these factors are intended to help the tester arrive 
at a sensible result. This process can be supported by automated tools to make the calculation easier. 

The first step is to select one of the options associated with each factor and enter the associated 
number in the table. Then simply take the average of the scores to calculate the overall likelihood. 
For example:

<table cellspacing="0" cellpadding="5" border="1" align="center">
<tr>
<td colspan="4" align="center">'''Threat agent factors'''</td>
<td></td>
<td colspan="4" align="center">'''Vulnerability factors'''</td>
</tr>
<tr>
<td width="10%" align="center">Skill level</td>
<td width="10%" align="center">Motive</td>
<td width="10%" align="center">Opportunity</td>
<td width="10%" align="center">Size</td>
<td width="2%" align="center"></td>
<td width="10%" align="center">Ease of discovery</td>
<td width="10%" align="center">Ease of exploit</td>
<td width="10%" align="center">Awareness</td>
<td width="10%" align="center">Intrusion detection</td>
</tr>
<tr>
<td align="center">5</td>
<td align="center">2</td>
<td align="center">7</td>
<td align="center">1</td>
<td align="center"></td>
<td align="center">3</td>
<td align="center">6</td>
<td align="center">9</td>
<td align="center">2</td>
</tr>
<tr>
<td colspan="9" bgcolor="lightblue" align="center">Overall likelihood=4.375 (MEDIUM)</td>
</tr>
</table>
<br/>
Next, the tester needs to figure out the overall impact. The process is similar here. In many cases the 
answer will be obvious, but the tester can make an estimate based on the factors, or they can average 
the scores for each of the factors. Again, less than 3 is low, 3 to less than 6 is medium, and 6 to 9 
is high.  For example:

<table cellspacing="0" cellpadding="5" border="1" align="center">
<tr>
<th colspan="4" align="center">Technical Impact</th>
<td></td>
<th colspan="4" align="center">Business Impact</th>
</tr>
<tr>
<td width="10%" align="center">Loss of confidentiality</td>
<td width="10%" align="center">Loss of integrity</td>
<td width="10%" align="center">Loss of availability</td>
<td width="10%" align="center">Loss of accountability</td>
<td width="2%" align="center"></td>
<td width="10%" align="center">Financial damage</td>
<td width="10%" align="center">Reputation damage</td>
<td width="10%" align="center">Non-compliance</td>
<td width="10%" align="center">Privacy violation</td>
</tr>
<tr>
<td align="center">9</td>
<td align="center">7</td>
<td align="center">5</td>
<td align="center">8</td>
<td align="center"></td>
<td align="center">1</td>
<td align="center">2</td>
<td align="center">1</td>
<td align="center">5</td>
</tr>
<tr>
<td colspan="4" bgcolor="lightblue" align="center">Overall technical impact=7.25 (HIGH)</td>
<td></td>
<td colspan="4" bgcolor="lightblue" align="center">Overall business impact=2.25 (LOW)</td>
</tr>
</table>
<br/>

### Determining Severity

However the tester arrives at the likelihood and impact estimates, they can now combine them to get 
a final severity rating for this risk. Note that if they have good business impact information, they 
should use that instead of the technical impact information.  But if they have no information about 
the business, then technical impact is the next best thing.

<table cellspacing="0" cellpadding="5" border="1" align="center">
<tr>
<th colspan="5" align="center">Overall Risk Severity</th>
</tr>
<tr>
<th rowspan="4" width="15%" align="center">Impact</th>
<td width="15%" align="center">HIGH</td>
<td width="15%" bgcolor="orange" align="center">Medium</td>
<td width="15%" bgcolor="red" align="center">High</td>
<td width="15%" bgcolor="pink" align="center">Critical</td>
</tr>
<tr>
<td align="center">MEDIUM</td>
<td bgcolor="yellow" align="center">Low</td>
<td bgcolor="orange" align="center">Medium</td>
<td bgcolor="red" align="center">High</td>
</tr>
<tr>
<td align="center">LOW</td>
<td bgcolor="lightgreen" align="center">Note</td>
<td bgcolor="yellow" align="center">Low</td>
<td bgcolor="orange" align="center">Medium</td>
</tr>
<tr>
<td align="center">&nbsp;</td>
<td align="center">LOW</td>
<td align="center">MEDIUM</td>
<td align="center">HIGH</td>
</tr>
<tr>
<td align="center">&nbsp;</td>
<th colspan="4" align="center">Likelihood</th>
</tr>
</table>
<br/>
In the example above, the likelihood is medium and the technical impact is high, so from a purely 
technical perspective it appears that the overall severity is high.  However, note that the business 
impact is actually low, so the overall severity is best described as low as well. This is why 
understanding the business context of the vulnerabilities you are evaluating is so critical to making 
good risk decisions. Failure to understand this context can lead to the lack of trust between the 
business and security teams that is present in many organizations.

## Step 5: Deciding What to Fix

After the risks to the application have been classified, there will be a prioritized list of what to 
fix. As a general rule, the most severe risks should be fixed first. It simply doesn't help the overall 
risk profile to fix less important risks, even if they're easy or cheap to fix.

Remember that not all risks are worth fixing, and some loss is not only expected, but justifiable based 
upon the cost of fixing the issue. For example, if it would cost $100,000 to implement controls to stem 
$2,000 of fraud per year, it would take 50 years return on investment to stamp out the loss. But 
remember there may be reputation damage from the fraud that could cost the organization much more.

## Step 6: Customizing the Risk Rating Model

Having a risk ranking framework that is customizable for a business is critical for adoption.  A tailored 
model is much more likely to produce results that match people's perceptions about what is a serious risk. 
A lot of time can be wasted arguing about the risk ratings if they are not supported by a model like this. 
There are several ways to tailor this model for the organization.

### Adding factors

The tester can choose different factors that better represent what's important for the specific organization. 
For example, a military application might add impact factors related to loss of human life or classified 
information. The tester might also add likelihood factors, such as the window of opportunity for an attacker 
or encryption algorithm strength.

### Customizing options

There are some sample options associated with each factor, but the model will be much more effective if the 
tester customizes these options to the business. For example, use the names of the different teams and the 
company names for different classifications of information. The tester can also change the scores associated 
with the options. The best way to identify the right scores is to compare the ratings produced by the model 
with ratings produced by a team of experts. You can tune the model by carefully adjusting the scores to match.

### Weighting factors

The model above assumes that all the factors are equally important. You can weight the factors to emphasize 
the factors that are more significant for the specific business. This makes the model a bit more complex, as 
the tester needs to use a weighted average. But otherwise everything works the same. Again it is possible to 
tune the model by matching it against risk ratings the business agrees are accurate.

# References

* [Managing Information Security Risk: Organization, Mission, and Information System View](https://csrc.nist.gov/publications/detail/sp/800-39/final)
* [Industry standard vulnerability severity and risk rankings (CVSS)](https://www.first.org/cvss/)
* [Threat Modeling Web Applications](https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ff648006(v=pandp.10))
* [Threat Modeling](Threat_Modeling)
* [A Platform for Risk Analysis of Security Critical Systems](https://sourceforge.net/projects/coras/)
* [Model-driven Development and Analysis of Secure Information Systems](http://heim.ifi.uio.no/~ketils/securis/)
* [Value Driven Security Threat Modeling Based on Attack Path Analysis](https://ieeexplore.ieee.org/document/4076949)
* [Risk Rating Template Example in MS Excel](https://wiki.owasp.org/index.php/File:OWASP_Risk_Rating_Template_Example.xlsx)
