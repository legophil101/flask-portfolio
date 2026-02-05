from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "philip_aron_secret_key"  # Keep this unique

# ---------------------------------------------------------
# DATA: Your Project Portfolio
# ---------------------------------------------------------
projects = [
    {
        "id": 1,
        "title": "Philip's Blog",
        "description": "A personal blog website built from scratch using Flask, Python, Bootstrap, and PostgreSQL (Supabase). Features full CRUD for posts, user authentication, rich text editing with Flask-CKEditor, comment system, Gravatar integration, responsive design, admin-only routes, and a resilient contact form with Formspree API and AJAX for smooth UX.",
        "tech": ["Python", "Flask", "Bootstrap", "PostgreSQL", "SQLAlchemy", "Flask-CKEditor", "AJAX", "Formspree"],
        "cover_image": "project-1.jpg",  # make sure this exists in static/assets/img
        "demo_image": "blog_preview.png",
        "github": "https://github.com/legophil101/blog-website"
    },
    {
        "id": 2,
        "title": "Gym Booking Automation",
        "description": "An automated Python bot using Selenium that logs into a gym scheduling app, books classes, handles waitlists, and verifies bookings. Includes self-healing retry logic, detailed logging, and a clean session summary.",
        "tech": ["Python", "Selenium", "dotenv", "WebDriverWait", "Logging"],
        "cover_image": "project-2.jpg",
        "demo_image": "gym_preview.png",
        "github": "https://github.com/legophil101/gym-booking-automation"
    },
    {
        "id": 3,
        "title": "Music Time Machine",
        "description": "Create a Spotify playlist from the Billboard Hot 100 on any historical date. Select a date, and this Python script finds the closest chart, searches each song on Spotify, and automatically creates a private playlist in your account.",
        "tech": ["Python", "Spotipy", "pandas", "dotenv", "CSV"],
        "cover_image": "project-3.jpg",
        "demo_image": "music_time_machine_preview.gif",
        "github": "https://github.com/legophil101/music-time-machine"
    }
]


# ---------------------------------------------------------
# ROUTES
# ---------------------------------------------------------

@app.route('/')
def home():
    """Renders the main one-page portfolio."""
    return render_template('index.html', projects=projects)


@app.route('/project/<int:project_id>')
def project_details(project_id):
    """Renders the detail page for a specific project."""
    # GENERATOR EXPRESSION
    # project = next((p for p in projects if p['id'] == project_id), None)

    # READABLE LOOP
    # 1. Start by assuming we found nothing
    project = None

    # 2. Look through every project one by one
    for p in projects:
        # 3. If the ID matches what we are looking for...
        if p['id'] == project_id:
            # 4. Save that project and STOP looking (break)
            project = p
            break

    if project:
        return render_template('single.html', project=project)
    return "Project not found", 404


# # NOTE:
# # Contact form intentionally disabled for now.
# # Direct email + GitHub links are used instead to reduce friction.
# @app.route('/contact', methods=['POST'])
# def contact():
#     """Handles the contact form submission."""
#     # 1. Capture Form Data
#     name = request.form.get('name')
#     email = request.form.get('email')
#     subject = request.form.get('subject')
#     message = request.form.get('message')
#
#     # 2. Logic (Print to console for now)
#     # Pro Tip: Later, use 'Flask-Mail' here to send this to your real inbox.
#     print(
#         f"--- NEW INQUIRY ---\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}\n--------------------")
#
#     # 3. User Feedback
#     flash(f"Thank you, {name}! Your message has been sent successfully.")
#
#     # 4. Redirect to home (prevents double-form submission on refresh)
#     return redirect(url_for('home', _anchor='contact-section'))


# ---------------------------------------------------------
# ERROR HANDLING
# ---------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return "This page doesn't exist yet!", 404


if __name__ == '__main__':
    app.run(debug=True)
