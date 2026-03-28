# Process
* Persona expanded from initial seed data and interview transcripts
* Social circles generated conditionally upon previous data and expanded focal persona



# Expand Persona Prompt
>Considering the shallow persona object and interview transcript of that persona, expand to a >full Persona object. For persona_id, demographic, psych_traits, and social network you should >be able to directly port the values from the input.
>
>{persona_shallow}
>
>{interview_transcript}

note: shallow persona is nvidia seed

# Create Social Circle Prompt

>Considering the given persona and interview transcript with that persona, generate a list of >4 or 5 close social personas. Close social personas are personas that the persona represented >by the anchor is likely to have regular contact or correspondence with. You may refer to the >interview transcript to infer people likely to be close to this persona, the interviewee is >the persona you are creating. Note that these will be shallow personas.
>
>{persona}
>
>{interview_transcript}



