# # from flask import render_template,request,redirect,url_for
# from . import main
# # from ..request import get_movies,get_movie,search_movie
# # from .forms import ReviewForm
# # from ..models import Review
# from flask_login import login_required, current_user
# from flask import render_template,request,redirect,url_for,abort
# from ..models import Blog, Comment, User, Subscriber
# from .forms import PitchForm,UpdateProfile,CommentForm
# # from .. import db
# from .. import db,photos



# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     message = 'Hello World'
#     all_blogs = Blog.get_blogs()
#     return render_template('index.html',message = message, all_pitches = all_pitches)
# # @main.route('/')
# # def index():

# #     '''
# #     View root page function that returns the index page and its data
# #     '''

# #     # Getting popular movie
# #     popular_movies = get_movies('popular')
# #     upcoming_movie = get_movies('upcoming')
# #     now_showing_movie = get_movies('now_playing')

# #     title = 'Home - Welcome to The best Movie Review Website Online'

# #     search_movie = request.args.get('movie_query')

# #     if search_movie:
# #         return redirect(url_for('search',movie_name=search_movie))
# #     else:
# #         return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
# # @main.route('/movies/<int:id>')
# # def movies(movie_id):

# #     '''
# #     View movie page function that returns the movie details page and its data
# #     '''
# #     return render_template('movie.html',id = movie_id)

# # @main.route('/movie/<int:id>')
# # def movie(id):

# #     '''
# #     View movie page function that returns the movie details page and its data
# #     '''
# #     movie = get_movie(id)
# #     title = f'{movie.title}'
# #     pitches = Pitch.get_pitches(movie.id)

# #     return render_template('movie.html',title = title,movie = movie,pitches = pitches)

# # @main.route('/search/<movie_name>')
# # def search(movie_name):
# #     '''
# #     View function to display the search results
# #     '''
# #     movie_name_list = movie_name.split(" ")
# #     movie_name_format = "+".join(movie_name_list)
# #     searched_movies = search_movie(movie_name_format)
# #     title = f'search results for {movie_name}'
# #     return render_template('search.html',movies = searched_movies)

    
# @main.route('/new', methods=['GET', 'POST'])
# @login_required

# def new_pitch():
#     form = PitchForm()
#     if form.validate_on_submit():

#         pitch = form.pitch.data
#         title = form.title.data
#         category = form.category.data
#         author = form.author.data
    
#         new_pitch = Pitch(pitch=pitch, title=title, category=category,author=author, user_id=current_user.id)

       
#         new_pitch.save_pitch()

#         return redirect(url_for('.index', pitch = pitch))

        
#         db.session.add(new_pitch)
#         db.session.commit()

#     return render_template('new_pitch.html', pitch_form=form)


# @main.route('/pitches')
# def display_pitch():
#         all_pitches = Pitch.get_pitches()
#         print(all_pitches)
#         return render_template("new_pitch.html", all_pitches = all_pitches)


# # @main.route('/comment/new/', methods=['GET', 'POST'])
# # @login_required
# # def comment(id):
# #    comment_form = CommentForm()

# #    pitch = Pitch.query.get(id)

# #    if comment_form.validate_on_submit():

# #        comment = comment_form.comment.data

       
# #        comment = Comment(comment=comment,user_id=user_id)
# #        comment.save_comment()

# #        return redirect(url_for('main.index'))

# #    return render_template('comment.html',comment_form=comment_form,pitch=pitch)

# # @main.route('/new/comment/<int:id>', methods = ['GET','POST'])
# # @login_required
# # def add_comment(id):
# #   pitch=Pitch.query.filter_by(id=id).first()
# #   if pitch is None:
# #     abort(404)

# #   form=CommentForm()
# #   if form.validate_on_submit():
# #      comment=form.comment.data
     
# #      new_comment=Comment(content=comment,user_id=current_user.id)
# #      db.session.add(new_comment)  
# #     #  db.session.commit() 

# #      return redirect(url_for('main.index'))
# #   return render_template('comment.html', comment_form=form ,pitch=pitch)


# @main.route('/comment/new/<int:id>', methods=['GET', 'POST'])
# @login_required
# def comment(id):
#     description_form = CommentForm()

#     pitch = Pitch.query.get(id)

#     if description_form.validate_on_submit():
#         description = description_form.description.data
#         new_comment = Comment(description=description,user_id=current_user.id,pitch_id = pitch.id )
#         new_comment.save_comments() 
#         return redirect(url_for('main.index'))

#     return render_template('comment.html',description_form=description_form)

# @main.route('/pitch/<int:id>')
# def single_pitch(id):
#     pitch=Pitch.query.filter_by(id=id).first()
#     comments=Comment.get_comments(id=id)
#     return render_template('pitch.html',pitch=pitch,comments=comments)

# @main.route('/downvotes/<int:id>')
# def upvoting(id):
#     pitch1=Pitch.query.filter_by(id=id).first()
#     pitch1.upvotes=Pitch.upvote(id)
#     return redirect(url_for('main.single_pitch',pitch=pitch1.upvotes))



# @main.route('/user/<uname>')
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()

#     if user is None:
#         abort(404)

#     return render_template("profile/profile.html", user = user)



# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateProfile()

#     if form.validate_on_submit():
#         user.bio = form.bio.data

#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.profile',uname=user.username))

#     return render_template('profile/update.html',form =form)


# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))



from flask import render_template, redirect,url_for,abort,request
from flask_login import login_required, current_user
from . import main
from .forms import BlogForm, CommentForm, SubscriberForm
from ..models import Blog, Comment, User, Subscriber, Quote
from ..email import mail_message
from .. import db
from ..request import get_quotes

# import markdown2

@main.route('/')
def index():
    '''
    function that returns the index page
    '''
    quote = get_quotes()
    blogs = Blog.query.all()
    return render_template('index.html', blogs = blogs, quote=quote)

@main.route('/new_blog', methods = ['GET','POST'])
@login_required
def new_blog():
   form  =BlogForm()

   if form.validate_on_submit():
       blog = form.blog.data

       new_blog = Blog(blog = blog, user_id = current_user.id)

       new_blog.save_blog()

       return redirect(url_for('main.index'))

   title = 'New Blog'
   return render_template('new_blog.html',title = title, blog_form = form)

@main.route('/comment/<id>')
def comment(id):
    '''
    function to return the comment
    '''
    comment = Comment.get_comment(id)
    print(comment)
    title = 'comments'
    return render_template('comment.html',title = title, comment = comment)

@main.route('/new_comment/<int:id>', methods = ['GET', 'POST'])
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        writer = form.author.data
        comm = form.comment.data

        new_comment = Comment(comment = comm, blog_id = id, author= writer)
        new_comment.save_comment()

        return redirect(url_for('main.index'))

    title = 'New Comment'
    return render_template('new_comment.html', title = title, comment_form = form, pitch_id = id)

@main.route('/bloger/<uname>')
@login_required

def profile(uname):
    user = User.query.filter_by(username = uname).first()
    # abort(404)

    post = Blog.query.filter_by(user_id = current_user.id).all()
    print(post)


    title = uname

    return render_template('profile.html', user = user, blogs = post,title=title)

@main.route('/blog/<id>')
@login_required
def blog(id):

    post = Blog.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    print(post)

    title = 'Delete blog'

    return render_template('delete.html', title = title, blogs = post)

@main.route('/pro-comment/<id>')
@login_required
def viewcomment(id):
    '''
    function to return the comments
    '''
    comment = Comment.get_comment(id)
    print(comment)
    title = 'comments'
    return render_template('pro-comment.html',title = title, comment = comment)

@main.route('/del-comment/<id>')
@login_required
def delcomment(id):
    '''
    function to delete comments
    '''
    comment = Comment.query.filter_by(id = id).first()
    db.session.delete(comment)
    db.session.commit()
    print(comment)
    title = 'delete comments'
    return render_template('delete.html',title = title, comment = comment)


@main.route('/subscribe',methods=["GET","POST"])
def subscriber():
    form=SubscriberForm()

    if form.validate_on_submit():
        subscriber = Subscriber(name=form.name.data,email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()

        mail_message("Welcome to my blog","email/welcome_user",subscriber.email,subscriber=subscriber)
        # flash('A confirmation by email has been sent to you by email')
        return redirect(url_for('main.index'))
        title = 'Subscribe'
    return render_template('subscription.html',form=form)


@main.route('/blog/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_blog(id):
    """
    Edit a blogpost in the database
    """
    new_blog=False

    blog = Blog.query.get(id)
    form = BlogForm()

    if form.validate_on_submit():

        blog.blog = form.blog.data

        db.session.commit()

        print('edited comment ')


        return redirect(url_for('main.index'))

    form.blog.data = blog.blog


    return render_template('new_blog.html',action = 'Edit',
                           new_blog = new_blog,
                           blog_form = form,
                           legend='Update Post')