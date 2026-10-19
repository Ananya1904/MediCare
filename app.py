
from flask import Flask, render_template_string

app = Flask(__name__)

HOME_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>MediCare | Your Health, Our Priority</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'DM Sans', sans-serif;
            color: #172b3a;
            background: #ffffff;
            line-height: 1.6;
        }

        a {
            text-decoration: none;
            color: inherit;
        }

        .container {
            width: 88%;
            max-width: 1200px;
            margin: auto;
        }

        /* Navigation bar */

        nav {
            height: 82px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #edf1f2;
            background: #ffffff;
        }

        .logo {
            font-family: 'Manrope', sans-serif;
            font-size: 25px;
            font-weight: 800;
            letter-spacing: -1px;
            color: #153a50;
        }

        .logo span {
            color: #269c91;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 30px;
            font-size: 14px;
            color: #647580;
        }

        .nav-links a:hover {
            color: #269c91;
        }

        .nav-button {
            background: #153a50;
            color: white;
            padding: 12px 20px;
            border-radius: 7px;
            font-size: 13px;
            font-weight: 600;
        }

        /* Hero section */

        .hero {
            background: #f5f8f7;
            padding: 75px 0;
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            align-items: center;
            gap: 55px;
        }

        .eyebrow {
            display: inline-block;
            background: #e1f1ed;
            color: #207e74;
            padding: 8px 13px;
            border-radius: 30px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.7px;
            margin-bottom: 22px;
        }

        h1, h2, h3 {
            font-family: 'Manrope', sans-serif;
        }

        h1 {
            font-size: clamp(38px, 4.5vw, 58px);
            line-height: 1.14;
            letter-spacing: -2px;
            color: #153a50;
            margin-bottom: 22px;
        }

        .hero-text {
            max-width: 490px;
            font-size: 16px;
            color: #647580;
            margin-bottom: 30px;
        }

        .primary-button {
            display: inline-block;
            background: #269c91;
            color: white;
            padding: 15px 23px;
            border-radius: 7px;
            font-weight: 700;
            font-size: 14px;
            transition: background 0.2s;
        }

        .primary-button:hover {
            background: #1c7f76;
        }

        .secondary-button {
            display: inline-block;
            padding: 14px 20px;
            color: #153a50;
            font-size: 14px;
            font-weight: 700;
        }

        .hero-image {
            min-height: 365px;
            border-radius: 18px;
            background:
                linear-gradient(
                    180deg,
                    rgba(21, 58, 80, 0.02),
                    rgba(21, 58, 80, 0.12)
                ),
                url("https://images.unsplash.com/photo-1551076805-e1869033e561?auto=format&fit=crop&w=1100&q=85")
                center / cover no-repeat;
            position: relative;
        }

        .floating-card {
            position: absolute;
            left: -22px;
            bottom: 25px;
            background: white;
            padding: 17px 20px;
            border-radius: 12px;
            box-shadow: 0 12px 35px #153a5018;
            max-width: 245px;
        }

        .floating-card strong {
            display: block;
            color: #153a50;
            font-size: 14px;
        }

        .floating-card p {
            font-size: 12px;
            color: #647580;
            margin-top: 4px;
        }

        .status-dot {
            display: inline-block;
            width: 8px;
            height: 8px;
            background: #269c91;
            border-radius: 50%;
            margin-right: 5px;
        }

        /* Statistics */

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            padding: 35px 0;
            border-bottom: 1px solid #edf1f2;
        }

        .stat {
            text-align: center;
        }

        .stat h2 {
            color: #153a50;
            font-size: 28px;
        }

        .stat p {
            color: #71818a;
            font-size: 13px;
        }

        /* General sections */

        .section {
            padding: 75px 0;
        }

        .section-heading {
            text-align: center;
            margin-bottom: 35px;
        }

        .section-heading h2 {
            color: #153a50;
            font-size: 32px;
            letter-spacing: -1px;
            margin-bottom: 10px;
        }

        .section-heading p {
            color: #71818a;
            font-size: 14px;
        }

        /* Specialty cards */

        .specialty-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
        }

        .specialty-card {
            padding: 25px 18px;
            border: 1px solid #e9eff0;
            border-radius: 12px;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .specialty-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 30px #153a500c;
        }

        .specialty-icon {
            width: 48px;
            height: 48px;
            display: grid;
            place-items: center;
            background: #e7f4f1;
            border-radius: 12px;
            font-size: 23px;
            margin-bottom: 17px;
        }

        .specialty-card h3 {
            font-size: 16px;
            color: #153a50;
            margin-bottom: 6px;
        }

        .specialty-card p {
            font-size: 12px;
            color: #71818a;
        }

        /* Doctors */

        .doctors-section {
            background: #f7f9f9;
        }

        .doctor-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 22px;
        }

        .doctor-card {
            background: white;
            border: 1px solid #e9eff0;
            border-radius: 13px;
            overflow: hidden;
        }

        .doctor-photo {
            height: 185px;
            background: #e6efed;
            display: grid;
            place-items: center;
            overflow: hidden;
        }

        .doctor-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .doctor-info {
            padding: 22px;
        }

        .doctor-info h3 {
            color: #153a50;
            font-size: 18px;
            margin-bottom: 4px;
        }

        .doctor-info p {
            font-size: 13px;
            color: #71818a;
        }

        .doctor-bottom {
            margin-top: 18px;
            padding-top: 15px;
            border-top: 1px solid #edf1f2;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
        }

        .fee {
            color: #153a50;
            font-weight: 800;
            font-size: 16px;
        }

        .fee small {
            display: block;
            color: #71818a;
            font-size: 10px;
            font-weight: 400;
        }

        .book-link {
            color: #207e74;
            font-size: 12px;
            font-weight: 700;
        }

        /* Call to action */

        .cta {
            margin: 65px auto;
            background: #153a50;
            color: white;
            border-radius: 16px;
            padding: 48px 30px;
            text-align: center;
        }

        .cta h2 {
            font-size: 30px;
            margin-bottom: 12px;
        }

        .cta p {
            color: #d0dfe4;
            font-size: 14px;
            margin-bottom: 24px;
        }

        /* Footer */

        footer {
            background: #f7f9f9;
            border-top: 1px solid #edf1f2;
            padding: 30px 0;
        }

        .footer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 15px;
        }

        footer p {
            color: #71818a;
            font-size: 12px;
        }

        /* Mobile layout */

        @media (max-width: 800px) {
            .container {
                width: 90%;
            }

            .hero-grid {
                grid-template-columns: 1fr;
                gap: 35px;
            }

            .hero {
                padding: 50px 0;
            }

            .hero-image {
                min-height: 280px;
            }

            .floating-card {
                left: 12px;
            }

            .specialty-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .doctor-grid {
                grid-template-columns: 1fr;
            }

            .nav-links {
                gap: 12px;
            }

            .nav-links .optional-link {
                display: none;
            }
        }

        @media (max-width: 480px) {
            .logo {
                font-size: 21px;
            }

            .nav-button {
                padding: 10px 12px;
                font-size: 12px;
            }

            .stats {
                gap: 8px;
            }

            .stat h2 {
                font-size: 22px;
            }

            .stat p {
                font-size: 11px;
            }

            .section-heading h2 {
                font-size: 27px;
            }

            .footer-content {
                flex-direction: column;
                text-align: center;
            }
        }
    </style>
</head>

<body>

    <nav>
        <div class="container" style="display:flex; align-items:center;
             justify-content:space-between; width:88%;">
            <a href="/" class="logo">Medi<span>Care.</span></a>

            <div class="nav-links">
                <a href="/">Home</a>
                <a href="#specialties" class="optional-link">Specialties</a>
                <a href="#doctors" class="optional-link">Our Doctors</a>
                <a href="#about" class="optional-link">About</a>
                <a href="#doctors" class="nav-button">Find a Doctor</a>
            </div>
        </div>
    </nav>

    <main>
        <section class="hero" id="about">
            <div class="container hero-grid">

                <div>
                    <span class="eyebrow">
                        YOUR WELLNESS, REIMAGINED
                    </span>

                    <h1>Better care.<br>Better health.<br>A better you.</h1>

                    <p class="hero-text">
                        Your health deserves thoughtful attention.
                        Discover trusted healthcare professionals
                        and make your next appointment with ease.
                    </p>

                    <a href="#doctors" class="primary-button">
                        Explore Our Doctors &rarr;
                    </a>

                    <a href="#specialties" class="secondary-button">
                        Our Specialties
                    </a>
                </div>

                <div class="hero-image">
                    <div class="floating-card">
                        <strong>
                            <span class="status-dot"></span>
                            Care that puts you first
                        </strong>
                        <p>A simpler way to manage your appointments.</p>
                    </div>
                </div>

            </div>
        </section>

        <div class="container">
            <section class="stats">
                <div class="stat">
                    <h2>Expert Care</h2>
                    <p>Professional healthcare directory</p>
                </div>

                <div class="stat">
                    <h2>Easy Booking</h2>
                    <p>A simpler appointment experience</p>
                </div>

                <div class="stat">
                    <h2>Patient First</h2>
                    <p>Designed around your convenience</p>
                </div>
            </section>
        </div>

        <section class="section" id="specialties">
            <div class="container">

                <div class="section-heading">
                    <h2>Care for every need</h2>
                    <p>
                        Explore our sample medical specialties.
                    </p>
                </div>

                <div class="specialty-grid">

                  
                   

                       <a href="/specialty/cardiology" class="specialty-card">
                       <div class="specialty-icon">&#9829;</div>
                       <h3>Cardiology</h3>
                       <p>Heart and cardiovascular care</p>
                       </a>

                      <a href="/specialty/general-medicine" class="specialty-card">
                      <div class="specialty-icon">&#10010;</div>
                      <h3>General Medicine</h3>
                      <p>Everyday health consultations</p>
                      </a>

                      <a href="/specialty/dermatology" class="specialty-card">
                      <div class="specialty-icon">&#9786;</div>
                      <h3>Dermatology</h3>
                      <p>Skin and hair consultations</p>
                      </a>

                      <a href="/specialty/pediatrics" class="specialty-card">
                      <div class="specialty-icon">&#10084;</div>
                      <h3>Pediatrics</h3>
                      <p>Healthcare for children</p>
                      </a>

                      <a href="/specialty/gynaecology" class="specialty-card">
                      <div class="specialty-icon">&#10047;</div>
                      <h3>Gynaecology</h3>
                      <p>Women's reproductive healthcare</p>
                      </a>

                      <a href="/specialty/psychiatry" class="specialty-card">
                      <div class="specialty-icon">&#9788;</div>
                      <h3>Psychiatry</h3>
                      <p>Mental health consultations</p>
                      </a>

                      <a href="/specialty/orthopedics" class="specialty-card">
                      <div class="specialty-icon">&#10010;</div>
                      <h3>Orthopedics</h3>
                      <p>Bones, joints and mobility</p>
                      </a>

                      <a href="/specialty/neurology" class="specialty-card">
                      <div class="specialty-icon">&#9733;</div>
                      <h3>Neurology</h3>
                      <p>Brain, nerves and nervous system</p>
                      </a>

                      <a href="/specialty/dentistry" class="specialty-card">
                      <div class="specialty-icon">&#9786;</div>
                      <h3>Dentistry</h3>
                      <p>Teeth and oral healthcare</p>
                      </a>

                                        <a href="/specialty/ophthalmology" class="specialty-card">
                                                <div class="specialty-icon">&#9678;</div>
                                                <h3>Ophthalmology</h3>
                                                <p>Eye health and vision care</p>
                                        </a>

                    <a href="/specialty/ent" class="specialty-card">
                        <div class="specialty-icon">&#9834;</div>
                        <h3>ENT</h3>
                        <p>Ear, nose and throat care</p>
                    </a>

    <a href="/specialty/oncology" class="specialty-card">
        <div class="specialty-icon">&#10010;</div>
        <h3>Oncology</h3>
        <p>Cancer care and consultations</p>
    </a>

    <a href="/specialty/endocrinology" class="specialty-card">
        <div class="specialty-icon">&#10047;</div>
        <h3>Endocrinology</h3>
        <p>Hormones and metabolic health</p>
    </a>

    <a href="/specialty/gastroenterology" class="specialty-card">
        <div class="specialty-icon">&#9829;</div>
        <h3>Gastroenterology</h3>
        <p>Digestive system healthcare</p>
    </a>

    <a href="/specialty/nephrology" class="specialty-card">
        <div class="specialty-icon">&#10010;</div>
        <h3>Nephrology</h3>
        <p>Kidney health and care</p>
    </a>

    <a href="/specialty/urology" class="specialty-card">
        <div class="specialty-icon">&#10047;</div>
        <h3>Urology</h3>
        <p>Urinary tract healthcare</p>
    </a>

    <a href="/specialty/pulmonology" class="specialty-card">
        <div class="specialty-icon">&#9829;</div>
        <h3>Pulmonology</h3>
        <p>Lung and respiratory care</p>
    </a>

    <a href="/specialty/rheumatology" class="specialty-card">
        <div class="specialty-icon">&#10010;</div>
        <h3>Rheumatology</h3>
        <p>Joint and autoimmune conditions</p>
    </a>

                </div>
            </div>
        </section>

        <section class="section doctors-section" id="doctors">
            <div class="container">

                <div class="section-heading">
                    <h2>Meet our specialists</h2>
                    <p>
                        Sample doctor profiles for our capstone prototype.
                    </p>
                </div>

                <div class="doctor-grid">

                    <div class="doctor-card">
                        <div class="doctor-photo">
                            <img
                                src="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=700&q=80"
                                alt="Sample doctor profile"
                                loading="lazy">
                        </div>

                        <div class="doctor-info">
                            <h3>Dr. Arjun Mehta</h3>
                            <p>Cardiologist</p>

                            <div class="doctor-bottom">
                                <div class="fee">
                                    &#8377;800
                                    <small>Consultation fee</small>
                                </div>

                                <a href="#appointment" class="book-link">
                                    Book visit &rarr;
                                </a>
                            </div>
                        </div>
                    </div>

                    <div class="doctor-card">
                        <div class="doctor-photo">
                            <img
                                src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=700&q=80"
                                alt="Sample doctor profile"
                                loading="lazy">
                        </div>

                        <div class="doctor-info">
                            <h3>Dr. Priya Sharma</h3>
                            <p>General Physician</p>

                            <div class="doctor-bottom">
                                <div class="fee">
                                    &#8377;500
                                    <small>Consultation fee</small>
                                </div>

                                <a href="#appointment" class="book-link">
                                    Book visit &rarr;
                                </a>
                            </div>
                        </div>
                    </div>

                    <div class="doctor-card">
                        <div class="doctor-photo">
                            <img
                                src="https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&w=700&q=80"
                                alt="Sample doctor profile"
                                loading="lazy">
                        </div>

                        <div class="doctor-info">
                            <h3>Dr. Neha Kapoor</h3>
                            <p>Dermatologist</p>

                            <div class="doctor-bottom">
                                <div class="fee">
                                    &#8377;600
                                    <small>Consultation fee</small>
                                </div>

                                <a href="#appointment" class="book-link">
                                    Book visit &rarr;
                                </a>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <section class="container" id="appointment">
            <div class="cta">
                <h2>Your health journey starts here.</h2>
                <p>
                    Take the first step towards a simpler healthcare
                    experience.
                </p>
                <a href="#doctors" class="primary-button">
                    Find Your Doctor &rarr;
                </a>
            </div>
        </section>

    </main>

    <footer>
        <div class="container footer-content">
            <a href="/" class="logo">Medi<span>Care.</span></a>
            <p>
                Student capstone prototype using Python and Flask.
            </p>
            <p>&copy; 2026 MediCare</p>
        </div>
    </footer>

</body>
</html>
"""



@app.route("/")
def home():
    return render_template_string(HOME_PAGE)


# All medical specialties supported by MediCare
SPECIALTIES = {
    "cardiology": "Cardiology",
    "general-medicine": "General Medicine",
    "dermatology": "Dermatology",
    "pediatrics": "Pediatrics",
    "gynaecology": "Gynaecology",
    "psychiatry": "Psychiatry",
    "orthopedics": "Orthopedics",
    "neurology": "Neurology",
    "dentistry": "Dentistry",
    "ophthalmology": "Ophthalmology",
    "ent": "ENT",
    "oncology": "Oncology",
    "endocrinology": "Endocrinology",
    "gastroenterology": "Gastroenterology",
    "nephrology": "Nephrology",
    "urology": "Urology",
    "pulmonology": "Pulmonology",
    "rheumatology": "Rheumatology",
}


# One route handles every specialty page
@app.route("/specialty/<slug>")
def specialty_page(slug):
    specialty_name = SPECIALTIES.get(slug)

    # Show a proper error if the specialty does not exist
    if specialty_name is None:
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Specialty Not Found | MediCare</title>
            </head>
            <body style="font-family: Arial; padding: 40px;">
                <h1>Specialty not found</h1>
                <p>Please choose a specialty from MediCare.</p>
                <a href="/">Return to homepage</a>
            </body>
            </html>
        """), 404

    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, initial-scale=1.0">
            <title>{{ specialty_name }} | MediCare</title>

            <style>
                * {
                    box-sizing: border-box;
                }

                body {
                    margin: 0;
                    padding: 30px 20px;
                    font-family: Arial, sans-serif;
                    color: #153a50;
                    background: #f5f8f7;
                    line-height: 1.6;
                }

                main {
                    max-width: 850px;
                    margin: 30px auto;
                    padding: 35px;
                    background: white;
                    border-radius: 14px;
                    box-shadow: 0 8px 30px #153a5010;
                }

                h1 {
                    margin-top: 28px;
                    font-size: 32px;
                }

                p {
                    color: #647580;
                }

                a {
                    color: #207e74;
                    text-decoration: none;
                    font-weight: bold;
                }

                .notice {
                    margin-top: 25px;
                    padding: 18px;
                    border-radius: 10px;
                    background: #e7f4f1;
                }
            </style>
        </head>

        <body>
            <main>
                <a href="/">&#8592; Back to MediCare</a>

                <h1>{{ specialty_name }}</h1>

                <p>
                    Find healthcare professionals specialising in
                    {{ specialty_name }}.
                </p>

                <div class="notice">
                    <strong>Doctor directory</strong>
                    <p>
                        Doctor listings will appear here as doctors
                        enrol and their profiles are approved.
                    </p>
                </div>
            </main>
        </body>
        </html>
    """, specialty_name=specialty_name)


if __name__ == "__main__":
    app.run(debug=True)

