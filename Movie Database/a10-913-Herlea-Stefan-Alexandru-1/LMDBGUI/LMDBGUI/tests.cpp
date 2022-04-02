#include "tests.h"
#include <assert.h>
#include "movie.h"
#include "admin_service.h"
#include "user_service.h"

void Tests::repo_init(MovieRepo& repo)
{
	repo.add(Movie("Terminator", "Action", 1984, 3251, "https://www.youtube.com/watch?v=k64P4l2Wmeg&ab_channel=MovieclipsClassicTrailers"));
	repo.add(Movie("Terminator 2", "Action", 1991, 4251, "https://www.youtube.com/watch?v=lwSysg9o7wE&ab_channel=STUDIOCANALFrance"));
	repo.add(Movie("Harry Potter and the Gobblet of Fire", "Adventure", 2000, 451, "https://www.youtube.com/watch?v=PFWAOnvMd1Q&ab_channel=WarnerMoviesOnDemand"));
	repo.add(Movie("Divergent", "Action", 1991, 4251, "https://www.youtube.com/watch?v=lwSysg9o7wE&ab_channel=STUDIOCANALFrance"));
	repo.add(Movie("Saw", "Horror", 2004, 2311, "https://www.google.com"));
	repo.add(Movie("Saw 2", "Horror", 2005, 1355, "https://www.google.com"));
	repo.add(Movie("Terminator 3", "Action", 2003, 1456, "https://www.youtube.com/watch?v=5UgPJhyJmlM&ab_channel=MovieclipsClassicTrailers"));
	repo.add(Movie("Bad Boys", "Action", 1995, 917, "https://www.youtube.com/watch?v=jKCj3XuPG8M&ab_channel=SonyPicturesEntertainment"));
	repo.add(Movie("Bad Boys 2", "Action", 2003, 2341, "https://www.youtube.com/watch?v=AURhd5TCG6U&ab_channel=thecultbox"));
	repo.add(Movie("M.I.B.", "S.F.", 1997, 3125, "https://www.youtube.com/watch?v=HYUd7AOw_lk&ab_channel=SonyPicturesHomeEntertainment"));
}

void Tests::test_movie()
{
	Movie mv("Terminator", "Action", 1984, 3251, "https://www.youtube.com/watch?v=k64P4l2Wmeg&ab_channel=MovieclipsClassicTrailers");
	
	assert(mv.getTitle() == "Terminator");
	assert(mv.getGenre() == "Action");
	assert(mv.getYear() == 1984);
	assert(mv.getLikes() == 3251);
	assert(mv.getLink() == "https://www.youtube.com/watch?v=k64P4l2Wmeg&ab_channel=MovieclipsClassicTrailers");

	mv.setTitle("Saw");
	mv.setGenre("Horror");
	mv.setYear(2004);
	mv.setLikes(1355);
	mv.setLink("https://www.youtube.com");

	assert(mv.getTitle() == "Saw");
	assert(mv.getGenre() == "Horror");
	assert(mv.getYear() == 2004);
	assert(mv.getLikes() == 1355);
	assert(mv.getLink() == "https://www.youtube.com");

	mv.runLink();
}

void Tests::test_repo()
{
	MovieRepo repo;
	this->repo_init(repo);

	assert(repo.length() == 10);

	assert(repo.add(Movie("Saw 2", "Horror", 2005, 1355, "")) == 1);

	assert(repo.remove("M.I.B.") == 0);
	assert(repo.remove("M.I.B.") == 1);

	assert(repo.remove("Saw") == 0);
	assert(repo.remove("Saw 2") == 0);
	assert(repo.remove("Bad Boys") == 0);
	assert(repo.remove("Bad Boys 2") == 0);
	assert(repo.remove("Harry Potter and the Gobblet of Fire") == 0);

	assert(repo.length() == 4);

	Movie mv = repo.getObj("Terminator");

	assert(mv.getTitle() != "");

	mv = repo.getObj("eqwg");

	assert(mv.getTitle() == "");

	repo.write_list();
}

void Tests::test_service()
{
	MovieRepo repo;
	this->repo_init(repo);

	AdminService service(repo);

	assert(service.add_movie("Terminator", "Action", "1984", "3251", "https://www.youtube.com/watch?v=k64P4l2Wmeg&ab_channel=MovieclipsClassicTrailers") == 1);

	assert(service.add_movie("wef", "ewfwef", "141", "315135", "dsfwef") == 5);

	assert(service.add_movie("wef", "ewfwef", "141", "315135", "") == 5);

	assert(service.add_movie("wef", "ewfwef", "eqg", "315135", "dsfwef") == 2);

	assert(service.add_movie("", "ewfwef", "141", "315135", "dsfwef") == 3);

	assert(service.add_movie("wef", "", "141", "315135", "dsfwef") == 4);

	assert(service.remove_movie("Saw") == 0);

	assert(service.remove_movie("") == 3);

	assert(service.remove_movie("Saw") == 1);

	assert(service.update_movie("Saw", "", "", "", "", "") == 1);
	assert(service.update_movie("Terminator", "", "refeg", "436", "23667", "https:") == 0);
	assert(service.update_movie("Terminator", "", "refeg", "qfeqfe", "23667", "https:") == 2);
	assert(service.update_movie("Terminator", "", "refeg", "436", "egwgh", "https:") == 2);
	assert(service.update_movie("Terminator", "", "refeg", "436", "23667", "eqgqg:") == 5);
	assert(service.update_movie("Terminator", "qfq", "refeg", "436", "23667", "https:") == 0);

	service.write_list();
}

void Tests::test_user_service()
{
	MovieRepo domain;
	this->repo_init(domain);
	MovieRepo watch;
	MovieRepo filter;

	UserService service(domain, watch, filter);

	service.getGenre("Action");
	assert(filter.length() == 6);

	Movie mv = service.getCurrent();
	assert(mv.getTitle() == "Terminator");

	service.addCurrent();

	service.cont();
	mv = service.getCurrent();
	assert(mv.getTitle() == "Terminator 2");

	service.addCurrent();
	assert(watch.length() == 2);

	for (int i = 0; i < 6; i++)
		service.cont();

	service.startOver();
	assert(filter.length() == 0);

	service.remove("Terminator", "y");
	assert(watch.length() == 1);

	service.writeWatchList();

	assert(service.getGenre("wewfe") == false);

	assert(service.remove("Terminator 2", "") == 2);
	assert(service.remove("", "y") == 1);
}

void Tests::run_all()
{
	this->test_movie();
	this->test_repo();
	this->test_service();
	this->test_user_service();
}
