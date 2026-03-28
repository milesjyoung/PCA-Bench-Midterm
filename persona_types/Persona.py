from __future__ import annotations

from typing import List, Literal
from pydantic import BaseModel, Field

IncomeCategory = Literal["Under $35k", "$35k-$75k", "$75k-$150k", "Over $150k"]
class Demographics(BaseModel):
  name: str = Field(description="Name of the persona.")
  age: int = Field(description="Age of the persona.")
  gender: str = Field(description="Gender of the persona.")
  education: str = Field(description="Education of the persona.")
  occupation: str = Field(description="Occupation of the persona.")
  income_bracket: IncomeCategory = Field(
      description="Income bracket of the persona. Must be one of: "
      "'Under $35k', '$35k-$75k', '$75k-$150k', or 'Over $150k'."
    )
  location: str = Field(description="Location of the persona.")
  marital_status: str = Field(description="Marital status of the persona.")

class PsychTraits(BaseModel):
  openness: float = Field(description="Openness trait score.")
  conscientiousness: float = Field(description="Conscientiousness trait score.")
  extraversion: float = Field(description="Extraversion trait score.")
  agreeableness: float = Field(description="Agreeableness trait score.")
  neuroticism: float = Field(description="Neuroticism trait score.")


StaticFactCategory = Literal["personal", "interest", "preference", "taboo"]
class StaticFact(BaseModel):
  id: str = Field(description="Unique identifier for the fact.")
  category: StaticFactCategory = Field(
        description=(
            "Category of the fact. Must be one of: "
            "'personal', 'interest', 'preference', or 'taboo'."
        )
    )
  text: str = Field(description="Text representation of the fact.")
  source: List[str] = Field(
        description="List of app_log_blueprints.item_id values supporting this fact."
    )

class PastActivity(BaseModel):
  id: str = Field(description="Unique identifier for the activity.")
  category: str = Field(description="Categorical representation of the activity.")
  text: str = Field(description="Text representation of the activity.")
  location: str = Field(description="Location of the activity.")
  timestamp: str = Field(description="Timestamp of the activity in ISO 8601 format.")
  involved_entities: List[str] = Field(
        description="IDs of users, groups, or entities involved in the activity."
    )
  source: List[str] = Field(
        description="List of app_log_blueprints.item_id or static_fact.id values supporting this fact."
    )


class HiddenContextGroundTruth(BaseModel):
    """Ground-truth hidden context for the persona."""

    static_facts: List[StaticFact] = Field(
        description="Collection of stable or semi-stable persona facts."
    )
    past_activities: List[PastActivity] = Field(
        description="Collection of historical persona activities."
    )

class AppLogBlueprint(BaseModel):
    """A blueprint connecting evidence items to app-level behavioral traces."""

    item_id: str = Field(description="Unique identifier for this app log.")
    app_source: str = Field(description="Application or platform source.")
    intent: str = Field(description="Behavioral interpretation of the app activity (user goal).")

class SocialLayer(BaseModel):
    """One layer of the persona's social graph."""

    description: str = Field(description="Meaning of this social layer.")
    base_layer: int = Field(description="Nominal Dunbar-style layer size.")
    scaled_size: int = Field(description="Scaled size for this persona.")


class SocialNetwork(BaseModel):
    """Structured social network for the persona."""

    intimate_circle: SocialLayer = Field(
        description="Closest family or best-friend circle."
    )
    close_friends: SocialLayer = Field(
        description="High-trust, high-frequency friend circle."
    )
    social_network: SocialLayer = Field(
        description="Casual acquaintances, colleagues, or neighbors."
    )
    active_network: SocialLayer = Field(
        description="Broader network with lower-frequency interaction."
    )
    dunbar_formula: str = Field(
        description="Formula used to scale social-layer sizes."
    )

class RelationshipToPrimary(BaseModel):
    relationship_type: Literal[
        "spouse", "partner", "parent", "child", "sibling",
        "best_friend", "close_friend", "coworker", "manager",
        "neighbor", "classmate", "mentor", "other"
    ]
    social_layer: Literal[
        "intimate_circle", "close_friends", "social_network", "active_network"
    ]

class RelatedPersona(BaseModel):
    relationship_id: str = Field(description="Unique ID for this relationship entry.")
    persona_reference: str = Field(description="persona_id of close-contact persona.")
    relationship_to_primary: RelationshipToPrimary

class PersonaShallow(BaseModel):
  persona_id: str = Field(description="Unique identifier for the persona.")
  demographics: Demographics = Field(description="Demographics of the persona.")
  psych_traits: PsychTraits = Field(
        description="OCEAN personality profile for the persona."
    )
  social_network: SocialNetwork = Field(
        description="Multi-layer social network structure for the persona."
    )

class PersonaShallowList(BaseModel):
    personas: List[PersonaShallow] = Field(
        description="List of 3 or 4 close social personas."
    )

class PreferencesAndInterests(BaseModel):
   health_and_wellness: str = Field("Health and wellness preferences, interests, and practices for the persona.")
   food: str = Field("Food preferences, interests, and practices for the persona.")
   travel: str = Field("Travel practices, preferences, and interests for the persona.")
   home_and_lifestyle: str = Field("Home and lifestyle practices, preferences, and interests for the persona.")
   entertainment: str = Field("Entertainment practices, preferences, and interests for the persona.")
   hobbies: str = Field("Hobby practices, preferences, and interests for the persona.")
   work_and_career: str = Field("Work and career practices, preferences, and interests for the persona.")
   arts_and_culture: str = Field("arts and culture practices, preferences, and interests for the persona.")
   sports: str = Field("sports practices, preferences, and interests for the persona.")
   nature_and_outdoors: str = Field("Nature and outdoors practices, preferences, and interests for the persona.")
   technology: str = Field("technology practices, preferences, and interests for the persona.")
   music: str = Field("music practices, preferences, and interests for the persona.")
   fashion: str = Field("fashion and dressing practices, preferences, and interests for the persona.")

class Persona(BaseModel):
  persona_id: str = Field(description="Unique identifier for the persona.")
  demographics: Demographics = Field(description="Demographics of the persona.")
  psych_traits: PsychTraits = Field(
        description="OCEAN personality profile for the persona."
    )
  preferences_and_interests: PreferencesAndInterests = Field(
     description="Preferences and interests related to the persona."
  )
  social_network: SocialNetwork = Field(
        description="Multi-layer social network structure for the persona."
    )
  close_social_personas: List[RelatedPersona] | None = Field(
        default_factory=list,
        description="Small set of explicitly generated personas in the primary user's immediate social world."
    )
