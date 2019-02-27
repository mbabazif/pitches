from flask import render_template, request, redirect, url_for, abort
from . import main

from .forms import ReviewForm, UpdateProfile
from .. import db, photos
from ..models import User, Review, Role, Pitch, Comment
from flask_login import login_required, current_user
import markdown2


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The one minute pi'

    return render_template('index.html', title=title)


@main.route('/review/<int:id>')
def single_review(id):
    review = Review.query.get(id)
    if review is None:
        abort(404)
    format_review = markdown2.markdown(
        review.movie_review, extras=["code-friendly", "fenced-code-blocks"])
    return render_template(
        'review.html', review=review, format_review=format_review)


@main.route('/movie/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    # movie = get_movie(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # Updated review instance
        new_review = Review(
            # movie_id=movie.id,
            # movie_title=title,
            # image_path=movie.poster,
            # movie_review=review,
            user=current_user)

        # save review method
        new_review.save_review()
    #     return redirect(url_for('.movie', id=movie.id))

    # title = f'{movie.title} review'
    # return render_template(
    #     'new_review.html', title=title, review_form=form, movie=movie)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))
