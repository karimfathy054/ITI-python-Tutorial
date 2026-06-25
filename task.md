~~1- install & setup django rest_framework~~
~~2- create your rest api structure (with or without sub-version “No Restriction”)~~
~~3- create movie & series model which both will share a common informations~~
~~a. title~~
~~b. description~~
~~c. release_date~~
~~d. categories (M2m relation with model category)~~
~~e. casts (Many2many relation with model cast)~~
~~f. poster_image~~
~~4- create the serializers for all previous models~~
5- create the full CRUD operation using function based views (only on movie will be
enough)
a. Don’t forget to implement both update scenarios (FULL & PARTIAL)
Bonus:
1- Display the categories & casts with their str representation while retrieving a movie