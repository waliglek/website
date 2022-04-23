from crypt import methods
from flask import Flask, render_template,flash, request, Blueprint, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .classes.Utilisateur import Utilisateur

views = Blueprint('views',__name__)


@views.route('/', methods=["GET","POST"])
def home():
    return render_template("home.html", user=current_user)

@views.route('/deconnexion')
@login_required
def deconnexion():
    logout_user()
    return redirect(url_for("views.connexion"))

@views.route('/connexion',methods=["GET","POST"])
def connexion():
    if request.method == 'POST':
            email = request.form.get('email')
            motdepasse = request.form.get('motdepasse')

            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.motdepasse, motdepasse):
                    flash('Tu es connecté', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash('Mot de passe incorrecte', category='error')
            else:
                flash("Ton email n'existe pas", category='error')


    return render_template('connexion.html', user=current_user)

@views.route('/inscritpion',methods=["GET","POST"])
def inscription():
    if request.method == 'POST':
        email = request.form.get('email')
        nom = request.form.get('nom')
        motdepasse1 = request.form.get('motdepasse1')
        motdepasse2 = request.form.get('motdepasse2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email déjà utilisé")
        elif len(email) < 4:
            flash('Email doit faire plus de 4 caractères')
        elif len(nom) <= 2:
            flash('Le nom doit faire plus de 2 caractères', category='error')
        elif motdepasse1 != motdepasse2:
            flash('Les mots de passe ne sont pas identiques', category='error')
        elif len(motdepasse1) < 6:
            flash('Le mot de passe doit faire plus de 6 caractères', category='error')
        else :
            #Création d'un user dans la base de donnée
            new_user=User(email=email,nom=nom,motdepasse=generate_password_hash(motdepasse1,method="sha256"))
            #création d'un utilisateur dans la base de donnée (voir pour faire les 2 en 1)
            utilisateur1=Utilisateur(email,nom,motdepasse1)
            flash(utilisateur1.getNomUtilisateur())
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Compte créé ! ', category='success')
            return redirect(url_for('views.home'))

        
    return render_template('inscription.html', user=current_user)


if __name__ == "__main__":
    views.run()