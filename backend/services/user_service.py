from database.db_connection import get_connection

# Get all users
def get_all_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users


# Create new user
def create_user(
    full_name,
    phone_number,
    email,
    state,
    district,
    land_acres,
    land_type,
    password
):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO users
    (
        full_name,
        phone_number,
        email,
        state,
        district,
        land_acres,
        land_type,
        password
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        full_name,
        phone_number,
        email,
        state,
        district,
        land_acres,
        land_type,
        password
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()


# Get user using email
def get_user_by_email(email):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """SELECT * FROM users WHERE email = %s"""

    cursor.execute(query, (email,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


# Get user using user_id
def get_user_by_id(user_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM users
    WHERE user_id = %s
    """

    cursor.execute(query, (user_id,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user