import ollama

MODEL = "llama3.2"

def agent(name, instruction):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": instruction
            },
            {
                "role": "user",
                "content": name
            }
        ]
    )
    return response["message"]["content"]

def main():
    incident = input("Enter cybersecurity incident: ")

    print("\n[1] Supervisor Agent")
    plan = agent(
        incident,
        """
        You are a cybersecurity supervisor agent.
        Analyze the incident and create a safe defensive investigation plan.
        Do not provide instructions for attacking systems.
        """
    )
    print(plan)

    print("\n[2] IOC Analysis Agent")
    ioc = agent(
        incident,
        """
        You are a defensive cybersecurity IOC analysis agent.
        Identify possible indicators such as IP addresses, domains,
        usernames, suspicious files and unusual activities.
        """
    )
    print(ioc)

    print("\n[3] Risk Analysis Agent")
    risk = agent(
        incident,
        """
        You are a cybersecurity risk assessment agent.
        Classify the incident as LOW, MEDIUM, HIGH or CRITICAL.
        Explain the defensive reasoning.
        """
    )
    print(risk)

    print("\n[4] MITRE Analysis Agent")
    mitre = agent(
        incident,
        """
        You are a defensive cybersecurity analyst.
        Identify relevant MITRE ATT&CK tactics or techniques if
        they can be reasonably inferred from the incident.
        Do not provide attack instructions.
        """
    )
    print(mitre)

    print("\n[5] Response Agent")
    response = agent(
        incident,
        """
        You are a SOC incident response agent.
        Provide safe defensive recommendations such as:
        investigation, containment, monitoring, password reset,
        log analysis and recovery.
        Do not provide offensive instructions.
        """
    )
    print(response)

    print("\n[6] Executive Report Agent")

    final_prompt = f"""
Create an executive cybersecurity incident report.

INCIDENT:
{incident}

IOC ANALYSIS:
{ioc}

RISK ANALYSIS:
{risk}

MITRE ANALYSIS:
{mitre}

RESPONSE RECOMMENDATIONS:
{response}

Include:
1. Incident summary
2. Indicators
3. Risk level
4. Possible techniques
5. Immediate defensive actions
6. Recovery actions
7. Monitoring recommendations
"""

    final = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    print("\nFINAL INCIDENT REPORT")
    print("=" * 60)
    print(final["message"]["content"])

if __name__ == "__main__":
    main()