#! /usr/bin python

# autor : spkang
# create at : 2013-10-12
# email : spkangirhit@gmail.com

import os
import codecs
import math
import re


stopwords = """a_able_about_above_abst_accordance_according_accordingly_across_act_actually_added_adj_affected_affecting_affects_after_afterwards_again_against_ah_all_almost_alone_along_already_also_although_always_am_among_amongst_an_and_announce_another_any_anybody_anyhow_anymore_anyone_anything_anyway_anyways_anywhere_apparently_approximately_are_aren_arent_arise_around_as_aside_ask_asking_at_auth_available_away_awfully_b_back_be_became_because_become_becomes_becoming_been_before_beforehand_begin_beginning_beginnings_begins_behind_being_believe_below_beside_besides_between_beyond_biol_both_brief_briefly_but_by_c_ca_came_can_cannot_can't_cause_causes_certain_certainly_co_com_come_comes_contain_containing_contains_could_couldnt_d_date_did_didn't_different_do_does_doesn't_doing_done_don't_down_downwards_due_during_e_each_ed_edu_effect_eg_eight_eighty_either_else_elsewhere_end_ending_enough_especially_et_et-al_etc_even_ever_every_everybody_everyone_everything_everywhere_ex_except_f_far_few_ff_fifth_first_five_fix_followed_following_follows_for_former_formerly_forth_found_four_from_further_furthermore_g_gave_get_gets_getting_give_given_gives_giving_go_goes_gone_got_gotten_h_had_happens_hardly_has_hasn't_have_haven't_having_he_hed_hence_her_here_hereafter_hereby_herein_heres_hereupon_hers_herself_hes_hi_hid_him_himself_his_hither_home_how_howbeit_however_hundred_i_id_ie_if_i'll_im_immediate_immediately_importance_important_in_indeed_index_information_instead_into_invention_inward_is_isn't_it_itd_it'll_its_itself_i've_j_just_k_keep_keeps_kept_kg_km_know_known_knows_l_largely_last_lately_later_latter_latterly_least_less_lest_let_lets_like_liked_likely_line_little_'ll_look_looking_looks_ltd_m_made_mainly_make_makes_many_may_maybe_me_mean_means_meantime_meanwhile_merely_mg_might_million_miss_ml_more_moreover_most_mostly_mr_mrs_much_mug_must_my_myself_n_na_name_namely_nay_nd_near_nearly_necessarily_necessary_need_needs_neither_never_nevertheless_new_next_nine_ninety_no_nobody_non_none_nonetheless_noone_nor_normally_nos_not_noted_nothing_now_nowhere_o_obtain_obtained_obviously_of_off_often_oh_ok_okay_old_omitted_on_once_one_ones_only_onto_or_ord_other_others_otherwise_ought_our_ours_ourselves_out_outside_over_overall_owing_own_p_page_pages_part_particular_particularly_past_per_perhaps_placed_please_plus_poorly_possible_possibly_potentially_pp_predominantly_present_previously_primarily_probably_promptly_proud_provides_put_q_que_quickly_quite_qv_r_ran_rather_rd_re_readily_really_recent_recently_ref_refs_regarding_regardless_regards_related_relatively_research_respectively_resulted_resulting_results_right_run_s_said_same_saw_say_saying_says_sec_section_see_seeing_seem_seemed_seeming_seems_seen_self_selves_sent_seven_several_shall_she_shed_she'll_shes_should_shouldn't_show_showed_shown_showns_shows_significant_significantly_similar_similarly_since_six_slightly_so_some_somebody_somehow_someone_somethan_something_sometime_sometimes_somewhat_somewhere_soon_sorry_specifically_specified_specify_specifying_still_stop_strongly_sub_substantially_successfully_such_sufficiently_suggest_sup_sure_t_take_taken_taking_tell_tends_th_than_thank_thanks_thanx_that_that'll_thats_that've_the_their_theirs_them_themselves_then_thence_there_thereafter_thereby_thered_therefore_therein_there'll_thereof_therere_theres_thereto_thereupon_there've_these_they_theyd_they'll_theyre_they've_think_this_those_thou_though_thoughh_thousand_throug_through_throughout_thru_thus_til_tip_to_together_too_took_toward_towards_tried_tries_truly_try_trying_ts_twice_two_u_un_under_unfortunately_unless_unlike_unlikely_until_unto_up_upon_ups_us_use_used_useful_usefully_usefulness_uses_using_usually_v_value_various_'ve_very_via_viz_vol_vols_vs_w_want_wants_was_wasn't_way_we_wed_welcome_we'll_went_were_weren't_we've_what_whatever_what'll_whats_when_whence_whenever_where_whereafter_whereas_whereby_wherein_wheres_whereupon_wherever_whether_which_while_whim_whither_who_whod_whoever_whole_who'll_whom_whomever_whos_whose_why_widely_willing_wish_with_within_without_won't_words_world_would_wouldn't_www_x_y_yes_yet_you_youd_you'll_your_youre_yours_yourself_yourselves_you've_z_zero"""


def generate_docs ( file_name ) :
	docs = []
	if os.path.isfile (file_name) :
		with codecs.open (file_name, 'r', 'utf-8') as cin :
			while True :
				line = cin.readline ()
				if not line :
					break
				line = line.strip()
				if len (line ) == 0 :
					continue
				docs.append(line);
	return docs


def load_stopwords () :
	stop_dict = {}
	t = stopwords.split('_')
	for w in t :
		try :
			stop_dict[w] += 0
		except  :
			stop_dict[w] = 1
	return stop_dict

def segment ( content) :
	pattern = re.compile ('\w+')
	words = []
	if content == None :
		return words
	words = pattern.findall(content)
	return words

def remove_stopwords (words, stopwords) :
	if words == None or words ==[] :
		return []
	res_wds = []
	for w in words :
		if w in stopwords :
			continue
		res_wds.append(w.lower())
	return res_wds


def generate_count_dict (docs, stop_words) :
	if docs == None :
		return None
	res_dict = {}
	doc_num_reduce = 0
	for doc in docs :
		tw = segment (doc)
		#print "tw : ", tw
		words = remove_stopwords (tw, stop_words)
		if words == None or words == [] :
			doc_num_reduce += 1
			continue 
		for wd in words :
			#print "wd : ", wd
			try : 
				res_dict[wd] += 1
			except :
				res_dict[wd] = 1
	
	return res_dict, doc_num_reduce

def add_one_normalize_dict ( dict , factor) :
	if dict is None :
		return None
	if factor < 1 :
		factor = 1
	for key in dict :
		dict [key] = (dict[ key ] + 1)* 1.0 / factor 
	return dict

def bayis_classifiaction (pos_file_name, neg_file_name):
	
	# load the stop words dict to swd
	stopwds = load_stopwords()
	
	#generate positive docs, namely apple is inc
	#pos_file_name = './../data/train/appleinc'
	pos_docs = generate_docs (pos_file_name)

	#genertate negative docs, namely apple is fruit
	#neg_file_name = './../data/train/applefruit'
	neg_docs = generate_docs (neg_file_name)
	
	# positive docs content words count after removing stop words
	pos_dict, pos_doc_reduce_num = generate_count_dict( pos_docs, stopwds )
	
	# positive docs content words count after removing stop words
	neg_dict, neg_doc_reduce_num = generate_count_dict( neg_docs, stopwds )
	
	print "pos_reduce : ", pos_doc_reduce_num
	print "neg_reduce : ", neg_doc_reduce_num

	# positive document num
	pos_doc_num = len ( pos_docs ) - pos_doc_reduce_num

	# negative document num
	neg_doc_num = len ( neg_docs ) - neg_doc_reduce_num

	# all train docs numnber
	N = pos_doc_num + neg_doc_num
	
	# positive doc proir property
	P_pos = pos_doc_num * 1.0 / N
	#P_pos = 0.6
	# negative doc proir property
	P_neg = neg_doc_num * 1.0 / N
	#P_neg = 0.40
	# the constant B is the vocabulary of positive documents and negative documents
	B = 0
	for key in pos_dict.keys() : # get the common element number both in pos and neg documents
		if key in neg_dict.keys():
			B += 1
	B = len ( pos_dict.keys() ) + len ( neg_dict.keys() ) - B
	
	# get the normalize dict , namely proir posibility
	pos_dict_size = len ( pos_dict )
	pos_dict = add_one_normalize_dict ( pos_dict, (pos_dict_size + B ) )
	
	neg_dict_size = len ( neg_dict )
	neg_dict = add_one_normalize_dict ( neg_dict, (neg_dict_size + B ) )
	
	return P_pos, P_neg, pos_dict, neg_dict, stopwds

def predict  (sentence,  pr, p_dict, stop_words) :
	tmp = []
	tmp.append(sentence)
	wd_dict, timtad = generate_count_dict (tmp, stop_words) 
	print "wd_dict ", wd_dict.keys()
	score = 0.0
	score += math.log(pr)
	for wd in wd_dict.keys() :
		if wd in p_dict.keys() :
			#t = math.pow(p_dict[wd], wd_dict[wd])
			print "(wd : %s, cnt : %s )" %(wd,  wd_dict[wd])
			score += wd_dict[wd] * 1.0 * math.log(p_dict[wd])
	return score
if __name__ == "__main__" :
	#print stopwords
	#load_stopwords()
	
	#p = re.compile ("\w+")
	#sent = "This article is about the fruit. For the technology company, see Apple Inc.. For other uses, see Apple (disambiguation)."
	#print segment (sent, p )
	
	pos_file_name = './../data/train/pos'
	neg_file_name = './../data/train/neg'
	
	
	#pos_file_name = './../data/train/appleinc'
	#neg_file_name = './../data/train/applefruit'

	P_pos , P_neg, pos_dict, neg_dict, stop_words = bayis_classifiaction (pos_file_name, neg_file_name)
	print "p_pos : ", P_pos
	print "p_neg : ", P_neg
	print "pos_dict : ", len (pos_dict)
	print "neg_dict : ", len (neg_dict)
	
	n = input ()
	i = 0
	while i < n :
		line = raw_input().strip()
		print "line : ", line
		#print "line segment : ", segment (line)
		pos_score = predict (line, P_pos, pos_dict, stop_words)
		neg_score = predict (line, P_neg, neg_dict, stop_words)
		print "pos_score : ", pos_score
		print "neg_score : ", neg_score
		if pos_score > neg_score :
			print "computer-company"
		else :
			print "fruit"
		i += 1



