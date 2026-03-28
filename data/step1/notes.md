# Procedure

* Nvidia seed data used as starting point
* Interview questions sourced from Stanford (Joon Sung Park) paper
* LLM prompted to interview random subset of interview questions using Nvidia seed data as "persona"


# Prompt
>You are roleplaying as this person:
>
> {json.dumps(persona, indent=2)}
>
> Conversation so far:
> {transcript}
>
> Answer the latest question naturally as this person.
> Do not explain. Just answer.



