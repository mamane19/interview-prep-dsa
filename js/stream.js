// # Every month, there are millions of streamers who stream in a variety of different categories. For this challenge,
// # you’ll be working on writing a data structure that will be storing the name of streamers streaming, the number of
// # views they currently have, as well as the category they are streaming in.

// # The initial input of streamer information will come as a list of strings:

// # Example: [Ninja, 100000, Fortnite, Pokimane, 40000, Valorant]

// # This is interpreted as Ninja has 100,000 views and is streaming Fortnite, and Pokimane has 40000 views and is streaming Valorant.
// # The names of the streamers will be unique. You will not be given any negative numbers for view counts.

// # You will also be given a list of commands, that will manipulate the streamer data or require output:

// # (All Examples are based on the original input above)

// # StreamerOnline - Add a new streamer to the data structure. The name will be unique.
// # Example Input: StreamerOnline, AOC, 75000, Just Chatting -> [Ninja, 100000, Fortnite, Pokimane, 40000, Valorant, AOC, 75000, Just Chatting ]

// # UpdateViews - Update the views of a streamer name, who is streaming in the respective category, to the provided number of views.
// # Example Input: UpdateViews, Ninja, 120000, Fortnite -> Update Ninjas viewer count to 120,000 If the streamer is not streaming within that category,
// # this command can be ignored.

// # UpdateCategory - Update the category of a streamer name, who is streaming in the respective category, to the provided category.
// # Example Input: UpdateCategory, Ninja, Fortnite, Warzone -> Update Ninjas category to Warzone If the streamer is not streaming within that category,
// # this command can be ignored.

// # StreamerOffline - Remove the streamer from the data structure, if they are streaming within the given category
// # Example Input: StreamerOffline, Ninja, Fortnite -> [Pokimane, 40000, Valorant] only this data will exist within the data structure.
// # If the streamer is not streaming within that category, this command can be ignored.

// # ViewsInCategory - Returns the amount of viewers watching a certain category. Returns 0 if category does not exist.
// # Example Input: ViewsInCategory, Fortnite -> 100000 as Ninja is the only streamer within the category

// # TopStreamerInCategory - Returns the streamer with the highest view count in a certain category.
// # Returns null if the category does not exist or there is nobody currently streaming in the category.
// # Example Input: TopStreamerInCategory, Valorant -> Pokimane as Pokimane is the only streamer within the category

// # TopStreamer - Returns the streamer with the highest view count currently streaming. Returns null if there is nobody currently streaming.
// # Example Inputs: TopStreamer -> Ninja as Ninja has the highest view count.

// # These commands will be strung together, for example:

// # StreamerOnline, Bugha, 75000, Fortnite, StreamerOnline, Tenzo, 30000, Valorant, ViewsInCategory, Fortnite, TopStreamerInCategory, Valorant

// # Expected Return: [175000, Pokimane]

// # Notes: There will never be a tie in view counts There will never be duplicate category or streamer Names.

// # Test Cases
// # Args: [["Ninja", "100000", "Fortnite", "Pokimane", "40000", "Valorant"], ["TopStreamer"]]
// # Expected result: ["Ninja"]


// # Args: [["Ninja", "100000", "Fortnite", "Pokimane", "40000", "Valorant"], ["StreamerOnline", "AOC", "75000", "Just Chatting", "ViewsInCategory", "Just Chatting"]]
// # Expected result: ["75000"]


// # Args: [["Ninja", "100000", "Fortnite", "Pokimane", "40000", "Valorant"], ["StreamerOnline", "Tfue", "110000", "Fortnite", "ViewsInCategory", "Fortnite", "TopStreamerInCategory", "Fortnite"]]
// # Expected result: ["210000", "Tfue"]


// # Args: [["Ninja", "100000", "Fortnite", "Pokimane", "40000", "Valorant"], ["UpdateViews", "Ninja", "120000", "Fortnite", "ViewsInCategory", "Fortnite"]]
// # Expected result: ["120000"]


// # Args: [["Ninja", "100000", "Fortnite", "Pokimane", "40000", "Valorant"], ["UpdateCategory", "Ninja", "Fortnite", "Warzone", "ViewsInCategory", "Fortnite", "ViewsInCategory", "Warzone"]]
// # Expected result: ["0", "100000"]

// # Args: [["Ninja", "100000", "Fortnite", "Pokimane", "40000", "Valorant"], ["StreamerOffline", "Ninja", "Fortnite", "ViewsInCategory", "Fortnite", "TopStreamer"]]
// # Expected result: ["0", "Pokimane"]

function 