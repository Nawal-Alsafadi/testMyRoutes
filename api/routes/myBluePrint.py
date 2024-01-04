from flask import Blueprint

from api.models.myModels import getString


first_page_bp = Blueprint('first_page_bp', __name__)
first_page_bp.route('fisr-page-route', methods=['GET'])(getString)
