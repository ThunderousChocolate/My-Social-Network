##made by: Samhira Babiker
##My Social Network

class User:
    def __init__(self, firstName, lastName, userName, bio, userID):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.bio = bio
        self.userID = userID
        self.friends = []
        self.posts = []

    def addFriend(self, userName):
        self.friends.append(userName)


##  def unFriend():
##
    def viewNewsFeed(self, friends):
        for friends in self.friends:
            print (friends.posts)


if __name__ == "__main__":
    firstName = "Samhira"
    lastName = "Babiker"
    userName = "ThunderousChocolate"
    bio = "I'm not gay I swear."
    userID = "88888888"

    User(firstName, lastName, userName, bio, userID)

    samhira = User(firstName, lastName, userName, bio, userID)
    lucy = User("Lucy", "Lucille", "lucygoosey", "Big Shaq", "0000")
    print(samhira.firstName)
    print(lucy.firstName)

    samhira.addFriend("lucygoosey")
    print(samhira.friends)
    samhira.posts.append("'I'm expanding my horizons.' *says in a snobby voice*")
    print(samhira.posts)

    selena = User("Selena", "Gonzales", "selena_gonz", "Selena?", "69")
    print(selena.firstName)

    samhira.addFriend("selena_gonz")
    print(samhira.friends)
    samhira.posts.append("yeet")
    print(samhira.posts)

    lucy.posts.append("got a new sister goose... might eat her idk yet.")
    print(lucy.posts)
    

    selena.posts.append("shE doEs'Nt evEn gO heRe.")
    print(selena.posts)

    daisy = User("Daisy", "Rivera", "daisythenerd", "kms", "420")
    print(daisy.firstName)

    samhira.addFriend("daisythenerd")
    print(samhira.friends)
    samhira.posts.append("she's a weirdo.")
    print(samhira.posts)

    daisy.posts.append("I take pictures of cacti for a living.")
    print(daisy.posts)

    
##    masaran = ("Masaran", "Keita", "friendly_neighborhood_potato", "I have a perfect plan for a whore house. I'll tell you later.", "666")
##    print(masaran.firstName)
##
##    samhira.addFriend("friendly_neighborhood_potato")
##    print(samhira.friends)
##    samhira.posts.append("I regret this descision...")
##    print(samhira.posts)
##
##    msaran.posts.append("Platypi produce Platytittiejuice.")
##    print(masaran.posts)
##        
        
    samhira.viewNewsFeed(userName)

class User:
    def __init__(self, userName):
        self.userName = userName

        friendsList = []
        posts = []

    def createPost(samhira, content):
        myPost = Post(content)
        self.posts.append(myPost)
        myPost.createPostID(len(posts))

    def createuserID(self, num):
        self.userID = num

class Post:
    def __init__(samhira, ThunderousChocolate):
        self.content = content
        self.postID = ""
        self.comments = []

    def createpostID(self, num):
        self.postID = num

class Network:
    def __init__(samhira):
        self.users = []

    def createUser (self, userName):
        myUser = User(userName)
        self.Users.append(myUser)
        myUser.createUserID(len(Users))
        

    
