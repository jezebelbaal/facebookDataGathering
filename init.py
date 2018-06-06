from source.controllers.facebook_controller import FacebookController
from source.modules.facebook_facade import FacebookFacade
import source.modules.comments_analysis

def main():	
	facebook_facade = FacebookFacade()
	controller = FacebookController(facebook_facade, comments_analysis)

	#print("Saving all posts for post pile.")
	#controller.save_all_posts_from_a_page_in_a_pile()
	#print("Saving all comments from a page.")
	#controller.saves_all_comments_from_unsaved_posts_pile()
	#controller.append_comments_in_single_corpus()
	controller.generate_word_cloud()

if __name__ == "__main__":
	main()

