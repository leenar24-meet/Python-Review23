def create_youtube_video(title,descreption):
	comments={}
	youtube={"title": title, "descreption": descreption, "likes":0, "dislikes":0, "comments":{}} 
	return youtube
def like(youtube_video):
	if "likes" in youtube_video:
			youtube_video["likes"]+=1
	return youtube_video 
def dislike(youtube_video):
	if "dislikes" in youtube_video:
			youtube_video["dislikes"]+=1
	return youtube_video 
def add_comments(youtubevideo, username,comments_text):
	youtubevideo["comments"][username]=comments_text
	return youtubevideo
dictionary=create_youtube_video("leensvid","hello")
dictionary=like(dictionary)
dictionary=dislike(dictionary)
dictionary=add_comments(dictionary,"Ali","fyffyfy")
#i would add likes by doing this :
for i in range(495):
	like(dictionary)
print(dictionary)








	


