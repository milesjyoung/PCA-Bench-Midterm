# Process
* Use persona and close circle and transcripts to create tasks


# Prompt
> You are generating benchmark test cases for evaluating an AI assistant's ability to retrieve and verify information from personal app logs.  
>
> ## Context  
> You are given:  
> 1. A PERSONA (used only to make the requests realistic)  
> 2. A list of CLOSE SOCIAL CONNECTIONS  
> 3. APP LOGS (messages, calendar events, etc.)  
>
> IMPORTANT:  
> - The APP LOGS are the ONLY source of truth.  
> - The PERSONA is ONLY for realism, tone, and plausibility.  
> - The assistant being evaluated will ONLY have access to the APP LOGS at test time.  
> - Do NOT rely on persona facts unless they are explicitly reflected in the logs.  
>
> ## Critical Framing Rule  
> - Every test case task must be written as a NATURAL FIRST-PERSON request from the focal persona to an AI assistant.  
> - The task must sound like something the focal persona would genuinely ask.  
> - Do NOT write evaluator-style questions.  
> - Do NOT mention logs, retrieval, evidence, benchmark, memory systems, or reasoning type in the task.  
> - The retrieval challenge must be implicit.  
> - The task should feel like a realistic help request about the persona's own life, plans, relationships, or commitments.  
>
> ## Your Task  
> Generate EXACTLY 5 test cases for this persona.  
>
> Each test case must include:  
> - type  
> - task  
> - successful_response  
> - evidence  
>
> ## Case Type Requirements  
> ### 1. Simple Fact-Check (1 case)  
> - Internally solvable using ONLY ONE app log.  
> - Task must still be a natural first-person request.  
>
> ### 2. Cross-Log Fact-Check (3 cases)  
> - Internally must require combining information across multiple conversations or multiple apps.  
> - Task must still be a natural first-person request.  
> - The need for multi-log retrieval should be implicit, not stated.  
>
> ### 3. Dynamic Preference Tracking (1 case)  
> - Internally must involve a change over time.  
> - The correct answer must rely on the MOST RECENT logged information.  
> - Task must still be a natural first-person request about a current preference, plan, or intention.  
>
> ## Successful Response Requirements  
> - Must answer the user's request directly and naturally.  
> - Must be grounded only in app logs.  
> - Must explicitly cite the relevant logs.  
> - Must explain why the cited evidence supports the answer.  
>
> ## Evidence Requirements  
> - Include the exact logs or log snippets needed to justify the answer.  
> - Include enough evidence to prove the answer and rule out weaker alternatives.  
>
> ## Style Requirements for task  
> - Phrase tasks like: "Can you remind me...", "Did I ever say...", "What did I end up deciding about...", "Am I free...", "Who did I tell...", "When was I planning to..."  
> - Avoid sounding formal, synthetic, or evaluator-written.  
> - Make each task feel personally motivated and socially realistic.  
>
> Return structured output matching the schema.  
>
> **[persona]**  
>
> **[close_circle]**  
>
> **[messenger_logs]**  
>
> **[calendar_logs]**