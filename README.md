# CardGames
A collection of card games written in Python

## Games
TBD

## Development Plan
### Phase 0
#### Objectives
* Library representing a card or a deck of cards.
  * Initialize with default 52 deck of cards
  * Allow for selecting contents of deck when initialized
    * Numerical cards only.
    * Face cards only.
    * Limit cards by color
    * Add N number of Jokers
  * Shuffle and order cards
  * Manipulate card attributes
  * Add / remove, sort, shuffle, and group methods to modify the collection of card objects (a.k.a. deck) 
  * Attributes
    | Name | Data Type | Description |
    |--|--|--|
    | rank | STR | The position of the card within a suit (0-10, Jack, Queen, King, Ace). |
    | suit | STR | Suit of the card (heart, diamond, spade, club). |
    | color | STR | Card Color (red or black). |
    | value | INT | A numerical value of the card to assign heirarchy. |
    | wild | BOOL | If the card should be treated as a wild. |
    | name | STR | What the card is called. Should hold some variations. |
    | face | TBD | A visual representation of the card. Image, ASCII, UNICode, etc |
  * Methods
    | Summary | Description |
    |--|--|
    | add to deck| Insert a Card Object to the deck. Should allow for interting at a random spot in the deck. |
    | remove from deck | Removes a Card Object from the deck |
    | sort deck | Variety of methods for organzing and shuffling the deck (e.g. New Deck order, by rank, etc)  |
    | group deck | Form collections of card objects (e.g. By Suit) |
    | shuffle deck | Rearange the deck in ways the mimic shuffle patterns (e.g. Bridge, Over-Hand, Washing, etc) |
* Framework for single point of contact for user interaction.
  * Create debug log. Loggig requirements (e.g. log rotation policy, set verbosity)
  * Read user arguments to initilize on launch
  * Initialize deck using optional command line arguments to define the configuration of the deck.
  * User interface
    * Display Deck
    * Add/Remove cards from deck
    * Sort/Shuffle deck
### Phase 1
Add simple games.
#### Objectives
TBD
