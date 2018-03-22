# Locations module

import bodyparts

from random import *
from enum import * 
from util import *

class Location():
	Name = ""
	NamePrep = ""
	Loc = LocInOutType.Indoors
	BeginDesc = ""
	EndDesc = ""
	BentOver = ""
	KneelingOn = ""
	SittingOn = ""
	Ground = "ground"
	Despite = ""
	MaleTopClothing = "tshirt"
	MaleBottomClothing = "jeans"
	FemaleTopClothing = "dress"
	FemaleBottomClothing = "panties"
	
	def RemoveMaleClothing(self):
		Penis = bodyparts.Penis()
		sTakeItOff = ""
		
		if not self.MaleTopClothing == "":
			sTakeItOff = "stripped off his " + self.MaleTopClothing + " and pulled down his " + self.MaleBottomClothing  + " exposing his " + bodyparts.Penis.RandomDescription(bAllowLongDesc = False)
		elif not self.MaleBottomClothing == "":
			sTakeItOff = "pulled down his " + self.MaleBottomClothing + " exposing his " + bodyparts.Penis.RandomDescription(bAllowLongDesc = False)
		else: 
			sTakeItOff = "was naked, his " + bodyparts.Penis.RandomDescription(bAllowLongDesc = False) + " on full display"

		sTakeItOff += bodyparts.Penis.RandomDescription(bAllowLongDesc = False)	
		
		return sTakeItOff
			
	def RemoveFemaleClothing(self):
		Vagina = bodyparts.Vagina()
		sTakeItOff = ""
		
		if not FemaleTopClothing == "":
			sTakeItOff = "slipped out of her " + self.FemaleTopClothing + " and pulled down her " + self.FemaleBottomClothing + " revealing her " + bodyparts.Vagina.RandomDescription(bAllowLongDesc = False)
		elif not FemaleBottomClothing == "":
			sTakeItOff = "pulled down her " + self.FemaleBottomClothing + " revealing her " + bodyparts.Vagina.RandomDescription(bAllowLongDesc = False)
		else:
			"was naked, her " + bodyparts.Breasts.RandomDescription(bAllowLongDesc = False) + " on full display"
			
		return sTakeItOff
			
	def PutOnMaleClothing(self, bBottomOnly = False):
		sPutItOn = ""
		
		if not self.MaleTopClothing == "":
			if bBottomOnly:
				sPutItOn = "pulled his " + self.MaleBottomClothing + " up"
			else:
				sPutItOn = "pulled his " + self.MaleBottomClothing + " up and put on his " + self.MaleTopClothing
		else:
			sPutItOn = "pulled up his " + self.MaleBottomClothing
			
		return sPutItOn
		
	def PutOnFemaleClothing(self, bBottomOnly = False):
		sPutItOn = ""
		
		if not self.FemaleTopClothing == "":
			if bBottomOnly:
				sPutItOn = "wiggled into her " + self.FemaleBottomClothing
			else:
				sPutItOn = "wiggled into her " + self.FemaleBottomClothing + " and then he helped her into her " + self.FemaleTopClothing
		else:
			sPutItOn = "wiggled into her " + self.FemaleBottomClothing
			
		return sPutItOn
		
class PublicLocation(Location):
	HurryReason = ""
	Caught = ""
	Excuse = ""
	Consequence = ""
	
class PrivateLocation(Location):
	pass

class Balcony(PublicLocation):
	Name = "the hotel balcony"
	NamePrep = "on the hotel balcony"
	Loc = LocInOutType.Outdoors
	BeginDesc = "The city spread out below them and the horizon was blue ocean."
	Despite = "the fact that they were exposed to anyone who looked up"
	BentOver = "the balcony rail"
	KneelingOn = "on a patio chair"
	SittingOn = "the broad ledge of the balcony"
	HurryReason = "What if someone is watching?"
	Caught = "'I think those people down there are videoing us with their iPhones!"
	Excuse = "'Let's give them a show, baby!' he replied."
	Consequence = "as a small crowd gathered to watch them"
	Ground = "ground"
	MaleTopClothing = ""
	MaleBottomClothing = "boxer briefs"
	FemaleTopClothing = "bra"
	FemaleBottomClothing = "panties"

class Beach(PublicLocation):
	Name = "the beach"
	NamePrep = "at the beach"
	Loc = LocInOutType.Outdoors
	BeginDesc = "A hot sun shone down as blue waves lapped at the sand."
	Despite = "the sand that got into every crack"
	BentOver = "the sand dune"
	KneelingOn = "on the beach towel"
	SittingOn = "on the beach towel"
	HurryReason = "The lifeguard will be here any minute"
	Caught = "'What are you doing?' shouted the lifeguard."
	Excuse = "'We're just putting on lotion!' he replied."
	Consequence = "right in front of the lifeguard"
	Ground = "tiled floor"
	MaleTopClothing = ""
	MaleBottomClothing = "swim trunks"
	FemaleTopClothing = "skimpy bikini top"
	FemaleBottomClothing = "bikini bottoms"
	
class Boat(PrivateLocation):
	Name = "the boat"
	NamePrep = "on a boat"
	BeginDesc = "The boat rocked gently in the open water. It was a perfect day."
	Despite = "the sun beating down on them"
	BentOver = "the side rail"
	KneelingOn = "on the stern of the boat"
	SittingOn = "on the stern of the boat"
	Ground = "deck"
	
class Bedroom(PublicLocation):
	Name = "the bedroom"
	NamePrep = "in the bedroom"
	BeginDesc = "The four-poster bed was bathed in warm sunlight as he shut the door behind them."
	Despite = "the open window"
	BentOver = "the king-sized bed"
	KneelingOn = "on the king-sized bed"
	SittingOn = "on the king-sized bed"
	HurryReason = "the neighbors will see us"
	Caught = "'I think the neighbors are watching us!' she said."
	Excuse = "'Let them,' he replied."
	Consequence = "as the people next door looked on"
	Ground = "thick carpet"
	
class CarBackseat(PublicLocation):
	Name = "the backseat of the car"
	NamePrep = "in the backseat of the car"
	BeginDesc = "The couple scrambled into the backseat of the car."
	Despite = "the extremely tight space"
	BentOver = "the back seat"
	KneelingOn = "on the back seat"
	SittingOn = "on the back seat"
	HurryReason = "I hear someone pulling up"
	Caught = "'There was a knock on the steamed-up window. 'Everything OK in there?' asked a cop."
	Excuse = "'Just a little engine trouble,' he replied."
	Consequence = "as the cop shone his flashlight through the window"
	Ground = "leather upholstery"
	
class Church(PublicLocation):
	Name = "the church"
	NamePrep = "in the church"
	BeginDesc = "Colored light flooded through a stained glass window."
	Despite = "the sacred atmosphere"
	BentOver = "the pulpit"
	KneelingOn = "on the altar steps"
	SittingOn = "on a pew"
	HurryReason = "someone will catch us in our sin"
	Caught = "'Whis is the meaning of this?' shouted the minister."
	Excuse = "'We were just praying!' he replied."
	Consequence = "as the minister looked on in horror"
	Ground = "soft carpet"
	
class Classroom(PublicLocation):
	Name = "the classroom"
	NamePrep = "in the classroom"
	BeginDesc = "The blackboard was covered in notes and the rows of student desks were straight and orderly."
	Despite = "the threat of being caught"
	BentOver = "the teacher's desk"
	KneelingOn = "on a student desk"
	SittingOn = "the teacher's desk"
	HurryReason = "someone will catch us"
	Caught = "Suddenly the door opened. A male student carrying a textbook walked in."
	Excuse = "'This isn't what it looks like!' he said."
	Consequence = "as the student tugged feverishly at his crotch"
	Ground = "the floor"
	
class Den(PrivateLocation):
	Name = "the den"
	NamePrep = "in the den"
	Loc = LocInOutType.Indoors
	Despite = "a little shyness"
	BeginDesc = "A fire was crackling in the fireplace of the cozy den."
	BentOver = "the arm of the couch"
	KneelingOn = "the sofa"
	SittingOn = "a thick cushion"
	Ground = "the thick fur rug"
	FemaleBottomClothing = "lacy silk panties"
	
class Hottub(PrivateLocation):
	Name = "the hot tub"
	NamePrep = "in the hot tub"
	Loc = LocInOutType.Outdoors
	Despite = "the heat"
	BeginDesc = "They slipped into the warm water of the hot tub."
	BentOver = "the side of the tub"
	KneelingOn = "the seat in the tub"
	SittingOn = "a seat in the tub"
	Ground = "the steaming water"
	FemaleTopClothing = "bikini"
	FemaleBottomClothing = "bikini bottoms"
	MaleTopClothing = ""
	MaleBottomClothing = "swimming trunks"
	
class Gym(PublicLocation):
	Name = "the gym"
	NamePrep = "at the gym"
	BeginDesc = "The mirrors on the wall of the gym reflected their bodies back at them."
	Despite = "the sweat which covered their bodies"
	BentOver = "a weight bench"
	KneelingOn = "on an exercise machine"
	SittingOn = "a weight bench"
	HurryReason = "someone will catch us"
	Caught = "A girl wearing a leotard walked in. 'Holy fuck!' the girl said."
	Excuse = "'We are just stretching!' he yelled."
	Consequence = "the girl with the leotard watched open-mouthed"
	Ground = "rubber mat"
	
class Kitchen(PublicLocation):
	Name = "the kitchen"
	NamePrep = "in the kitchen"
	BeginDesc = "A pan of bacon was frying on the kitchen stove."
	Despite = "the crackling of cooking bacon"
	BentOver = "the counter"
	KneelingOn = "on a kitchen chair"
	SittingOn = "on the kitchen table"
	HurryReason = "the bacon will burn"
	Caught = "The pan of bacon began to smoke."
	Excuse = "'We'll just make some more!', he said."
	Consequence = "as the fire alarm blared"
	Ground = "black and white tiled floor"
	MaleTopClothing = ""
	MaleBottomClothing = "briefs"
	FemaleTopClothing = "oversized tshirt"
	FemaleBottomClothing = "panties"
	
class Library(PublicLocation):
	Name = "the library"
	NamePrep = "in the library"
	BeginDesc = "It was quiet and stuffy amongst the stacks."
	Despite = "the need for silence"
	BentOver = "a stack of books"
	KneelingOn = "on a table strewn with books"
	SittingOn = "on a study desk"
	HurryReason = "someone will hear us"
	Caught = "'Please, you must be quiet!' called out a librarian."
	Consequence = "as the librarian listened"
	Excuse = "'We are just about to check out!' he called back."
	Ground = "soft carpet"
	FemaleBottomClothing = "thong"
	
class MassageRoom(PrivateLocation):
	Name = "a massage room"
	NamePrep = "in a massage room"
	BeginDesc = "Ambient ocean sounds and the smell of incense filled the massage room."
	Despite = "the danger of being caught"
	BentOver = "the massage table"
	KneelingOn = "on the massage table"
	SittingOn = "on the massage table"
	Ground = "soft carpet"
	FemaleTopClothing = ""
	FemaleBottomClothing = "towel"
	MaleTopClothing = ""
	MaleBottomClothing = "towel"
	
class MensRoom(PublicLocation):
	Name = "men's restroom"
	NamePrep = "in the men's restroom"
	BeginDesc = "Crude graffiti was scrawled on the walls of the cramped stall."
	Despite = "the extremely cramped quarters"
	BentOver = "the toilet"
	KneelingOn = "on the toilet seat"
	SittingOn = "on the toilet"
	HurryReason = "Someone might hear us!"
	Caught = "Someone pounded on the door and shouted 'Hurry up!'"
	Consequence = "as someone called out 'Fuck her good, man'"
	Excuse = "'Busy!' he shouted back."
	Ground = "tiled floor"
	FemaleBottomClothing = "thong"

class Office(PublicLocation):
	Name = "the office"
	NamePrep = "in the office"
	BeginDesc = "A large oak desk stood in the center of the corner office."
	Despite = "the danger of being caught"
	BentOver = "the massive desk"
	KneelingOn = "on the boss's desk"
	SittingOn = "on the surface of the desk"
	HurryReason = "Someone will catch us!"
	Caught = "The door opened and a tall man walked in. 'Fuck, its my boss!' she said."
	Consequence = "as her boss watched, open-mouthed"
	Excuse = "'This isn't what it looks like!' he shouted."
	Ground = "carpet"
	FemaleTopClothing = "gray pencil dress"
	FemaleBottomClothing = "thong panties"
	MaleTopClothing = "dress shirt"
	MaleBottomClothing = "slacks"

class ParentsBedroom(PrivateLocation):
	Name = "his parents bedroom"
	NamePrep = "in the bedroom of his parents"
	Loc = LocInOutType.Indoors
	Despite = "some fumbling awkwardness"
	BeginDesc = "Candles were lit all around his parents king-sized bed."
	BentOver = "the end of the bed"
	KneelingOn = "the bed"
	SittingOn = "a stack of cushions"
	Ground = "the thick comforter"
	FemaleBottomClothing = "sheer panties"
	
class PrivateBeach(PrivateLocation):
	Name = "a private beach"
	NamePrep = "on a private beach"
	Loc = LocInOutType.Outdoors
	BeginDesc = "The beach was lovely, and so private that she felt free to go topless."
	Despite = "the sand that got into every crack"
	BentOver = "a sand dune"
	KneelingOn = "on the beach towel"
	SittingOn = "a beach chair"
	Ground = "sand"
	MaleTopClothing = ""
	MaleBottomClothing = "speedo"
	FemaleTopClothing = ""
	FemaleBottomClothing = "g-string"
	
class Shower(PrivateLocation):
	Name = "the shower"
	NamePrep = "in the shower"
	Loc = LocInOutType.Indoors
	Despite = "the slippery floor"
	BeginDesc = "The hot shower water rained down on them."
	BentOver = "against the wall"
	KneelingOn = "the floor of the shower stall"
	SittingOn = "a seat in the shower stall"
	Ground = "wet floor"
	FemaleTopClothing = ""
	FemaleBottomClothing = ""
	MaleTopClothing = ""
	MaleBottomClothing = ""
	
class StarbucksBathroom(PublicLocation):
	Name = "Starbucks bathroom"
	NamePrep = "in the bathroom at Starbucks"
	BeginDesc = "The bathroom at Starbucks was small and smelled of coffee."
	Despite = "the extremely cramped quarters"
	BentOver = "the toilet"
	KneelingOn = "on the toilet seat"
	SittingOn = "on the toilet"
	HurryReason = "Someone might hear us!"
	Caught = "Someone pounded on the door and shouted 'Hurry up!'"
	Excuse = "'Busy!' he shouted back."
	Consequence = "as someone called, 'I think they're having sex in the Starbucks bathroom'"
	Ground = "tiled floor"
	
class Surf(PublicLocation):
	Name = "the surf"
	NamePrep = "in the water at the beach"
	Loc = LocInOutType.Outdoors
	BeginDesc = "A hot sun shone down as the waves crested against their bodies."
	Despite = "the breaking waves"
	BentOver = "in the water"
	KneelingOn = "in the shallow water"
	SittingOn = "in the shallow water"
	HurryReason = "People will notice us!"
	Caught = "'That lifeguard is coming towards us!' she said."
	Excuse = "'Let them enjoy it, baby,' he said."
	Consequence = "as the lifeguard watched"
	Ground = "the dark green water"
	MaleTopClothing = ""
	MaleBottomClothing = "speedos"
	FemaleTopClothing = "skimpy bikini top"
	FemaleBottomClothing = "g-string"
	
class Woods(PublicLocation):
	Name = "the woods"
	NamePrep = "out in the woods"
	Loc = LocInOutType.Outdoors
	BeginDesc = "The leafy trees were thick in every direction."
	Despite = "the dirt and mosquitos"
	BentOver = "a mossy log"
	KneelingOn = "on a large smooth rock"
	SittingOn = "on a tree stump"
	HurryReason = "someone might see us"
	Caught = "'Oh my god, there is a homeless guy watching us,' she whispered."
	Excuse = "'Fuck off!' he yelled at the man."
	Consequence = "as the homeless man watched them"
	Ground = "thick carpet of leaves"
	FemaleBottomClothing = "thong"
	
class YogaStudio(PrivateLocation):
	Name = "a yoga studio"
	NamePrep = "in a yoga studio"
	Loc = LocInOutType.Indoors
	BeginDesc = "The relaxing drone of zen meditation music filled the warm studio."
	Despite = "not having stretched properly"
	BentOver = "a large yoga ball"
	KneelingOn = "a yoga mat"
	SittingOn = "a balance ball"
	Ground = "the purple yoga mat"
	FemaleBottomClothing = "tight yoga pants"

	
class LocationSelector():
	Locations = []
	
	def __init__(self):
		for sub in PublicLocation.__subclasses__():
			self.Locations.append(sub())
			
		for sub in PrivateLocation.__subclasses__():
			self.Locations.append(sub())
	
	def Location(self, InOut = LocInOutType.Either, PubPrivType = LocPubPrivType.Either):
		ThisLoc = Location()
		MatchingLocations = []
		
		if InOut == None:
			InOut = LocInOutType.Either
		if PubPrivType == None:
			PubPrivType = LocPubPrivType.Either
		
		#print("Getting a " + str(PubPrivType) + "location and .")
		#print("Length of self.Locations[] is " + str(len(self.Locations)))
		
		if not self.Locations is None and len(self.Locations) > 0:
			for loc in self.Locations:
				#print("Loc [" + loc.Name + "] is " + str(loc.Loc) + " and " + loc.__class__.__name__)
				if InOut == LocInOutType.Either or loc.Loc == InOut:
					if PubPrivType == LocPubPrivType.Public and isinstance(loc, PublicLocation):
						MatchingLocations.append(loc)
						#print("Public location added to list.")
					elif PubPrivType == LocPubPrivType.Private and isinstance(loc, PrivateLocation):
						MatchingLocations.append(loc)
						#print("Private location added to list.")
					elif PubPrivType == LocPubPrivType.Either:
						MatchingLocations.append(loc)
						#print("Any type location added to list.")
			
			#print("Length of MatchingLocations[] is " + str(len(MatchingLocations)))
			if len(MatchingLocations) > 0:
				iRand = randint(0, len(MatchingLocations) - 1)
				ThisLoc = MatchingLocations[iRand]
		
		return ThisLoc
		
	
	