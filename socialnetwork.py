##made by: Samhira Babiker
##My Social Network

class User:
    
    def __init__(self, userName):
        self.userName = userName
        self.firstName = ""
        self.lastName = ""
        self.bio = ""
        self.friends = []
        self.posts = []

    def viewFriends(self, friends):
        for people in friends:
            print(people.userName)

    def addfirstName(self, firstName):
        self.firstName = firstName

    def addlastName(self, lastName):
        self.lastName = lastName

    def addbio(self, bio):
        self.bio = bio

    def addFriend(self, something):
        self.friends.append(something)

    def addposts(self, post):
        self.posts.append(post)

    def unFriend(self, yoda):
        for friend in self.friends:
            if friend.userName == yoda.userName:
                self.friends.remove(yoda)



    def viewNewsFeed(self, friends):
        for friend in self.friends:
            print(friend.posts)



if __name__ == "__main__":
    userName = "ThunderousChocolate"



    Samhira = User(userName)
    Billy = User("SecretlyTheGrimReaper")
    DoodleBob = User("MihoyMinoy")

    Samhira.addFriend(Billy)
    Samhira.addFriend(DoodleBob)

    Samhira.addposts("skibidi")
    Billy.addposts("Pah Pah!")
    DoodleBob.addposts("And a Poom Poom Prrrrrrh Poom! Skiyah!")

    Samhira.viewFriends(Samhira.friends)
    Samhira.viewNewsFeed(Samhira.friends)
    Samhira.unFriend(Billy)
    Samhira.viewFriends(Samhira.friends)
        

    friendsList = []
    posts = []

    def createPost(self, content):
        myPost = Post(content)
        self.posts.append(myPost)
        myPost.createPostID(len(posts))

    def createuserID(self, num):
        self.userID = num

class Post:
    def __init__(self, userName):
        self.content = ""
        self.postID = ""
        self.comments = []

    def createcomment(self, comment):
        self.comment.append(comment)

    def createpostID(self, num):
        self.postID = num

class Network:
    def __init__(samhira):
        self.users = []

    def createUser (self, userName):
        myUser = User(userName)
        self.Users.append(myUser)
        myUser.createUserID(len(Users))
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
    
    userName = "ThunderousChocolate"
   
    User(userName)

    samhira = User(userName)
    lucy = User("lucygoosey")
    print(samhira.firstName)
    print(lucy.firstName)

    post1 ="I'm expanding my horizons.' *says in a snobby voice*"

    samhira.addFriend("lucygoosey")
    print(samhira.friends)
    samhira.posts.append(post1)
    print(samhira.posts)

    selena = User("selena_gonz")
    print(selena.firstName)

    post2 ="yeet"

    samhira.addFriend(selena)
    print(samhira.friends)
    samhira.posts.append(post2)
    print(samhira.posts)

    post3 ="got a new sister goose... might eat her idk yet."

    lucy.posts.append(post3)
    print(lucy.posts)

    post4 ="shE doEs'Nt evEn gO heRe."
    

    selena.posts.append(post4)
    print(selena.posts)

    daisy = User("daisythenerd")
    print(daisy.firstName)

    post5 ="she's a weirdo."

    samhira.addFriend(daisy)
    print(samhira.friends)
    samhira.posts.append(post5)
    print(samhira.posts)

    post6 ="I take pictures of cacti for a living."

    daisy.posts.append(post6)
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
        
##    samhira.viewNewsFeed(userName)
    

