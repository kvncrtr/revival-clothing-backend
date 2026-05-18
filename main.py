from fastapi import FastAPI
from app.controllers.drop import router as drop_router

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Revival Clothing API is running"} 

app.include_router(drop_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)

'''
CREATE TABLE users(
    id BIGSERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number INTEGER,
    sex CHAR(2),
    create_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE orders(
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id), 
    order_number TEXT NOT NULL,
    drop_id BIGINT NOT NULL REFERENCES drops(id),
    amount INTEGER NOT NULL,
    eta TIMESTAMPTZ DEFAULT NOW() + INTERVAL '7 days',
    address TEXT NOT NULL,
    tracking TEXT NOT NULL,
    shipping_provider TEXT NOT NULL
);

ALTER TABLE drops 
RENAME COLUMN price TO price_cents;

ALTER TABLE drops 
ALTER COLUMN price_cents TYPE INTEGER;

ALTER TABLE drops
ADD COLUMN inventory_count INTEGER NOT NULL;

CREATE TYPE clothing_size AS ENUM ('XS', 'S', 'M', 'L', 'XL', 'XXL');
CREATE TYPE status_type AS ENUM ('coming', 'available', 'archive', 'discontinued', 'vintage');

/* Drops Table
	id              | integer                  |           | not null | nextval('drops_id_seq'::regclass)
	name            | text                     |           | not null | 
	price           | numeric(10,2)            |           |          | 0
	units_count     | integer                  |           |          | 0
	status          | status_type              |           |          | 'archive'::status_type
	team            | text                     |           |          | 
	created_at      | timestamp with time zone |           |          | now()
	updated_at      | timestamp with time zone |           |          | now()
	owner           | text                     |           |          | 
	collection_type | text                     |           |          | 'streetware'::text
*/

INSERT INTO drops(name, price_cents, inventory_count, status, team, owner, collection_type)
VALUES ('He Has Risen', 9999, 1000, 'available', 'founding', 'Kevin', 'Fashion'),
			 ('The Blood', 89701, 100, 'coming', 'founding', 'Kevin', 'Fashion'),
			 ('Rip The Vail', 120099, 10, 'coming', 'founding', 'Kevin', 'Fashion');

CREATE TABLE users(
    id BIGSERIAL PRIMARY KEY,
    first_name TEXT NOT NULL UNIQUE,
    last_name TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number INTEGER,
    sex CHAR(2),
    create_at TIMESTAMPTZ DEFAULT NOW(),
);

ALTER TABLE users
ADD COLUMN first_name TEXT NOT NULL UNIQUE;

ALTER TABLE users
ADD COLUMN last_name TEXT NOT NULL UNIQUE;

ALTER TABLE users
ALTER COLUMN phone_number TYPE BIGINT;

/* Users Table
    id           | bigint                   |           | not null | nextval('users_id_seq'::regclass)
    username     | text                     |           | not null | 
    email        | text                     |           | not null | 
    phone_number | bigint                   |           |          | 
    sex          | character(2)             |           |          | 
    create_at    | timestamp with time zone |           |          | now()
    first_name   | text                     |           | not null | 
    last_name    | text                     |           | not null | 
Indexes:
    "users_pkey" PRIMARY KEY, btree (id)
    "users_first_name_key" UNIQUE CONSTRAINT, btree (first_name)
    "users_last_name_key" UNIQUE CONSTRAINT, btree (last_name)
Referenced by:
    TABLE "orders" CONSTRAINT "orders_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id)
*/

INSERT INTO users(username, email, phone_number, sex, first_name, last_name)
VALUES (
    'repayjesus', 
    'kevin@gorpstudios.com', 
    4049983276,
    'M', 
    'Kevin', 
    'Carter'
),
(
    'jordan_reed',
    'jordan.reed@example.com',
    4045551201,
    'M',
    'Jordan',
    'Reed'
),
(
    'maya_thompson',
    'maya.thompson@example.com',
    4045558732,
    'F',
    'Maya',
    'Thompson'
),
(
    'caleb_wright',
    'caleb.wright@example.com',
    4045554429,
    'M',
    'Caleb',
    'Wright'
);

/* Orders Table
    id                | bigint                   |           | not null | nextval('orders_id_seq'::regclass)
    user_id           | bigint                   |           | not null | 
    order_number      | text                     |           | not null | 
    drop_id           | bigint                   |           | not null | 
    amount_cents      | integer                  |           | not null | 
    eta               | timestamp with time zone |           |          | now() + '7 days'::interval
    address           | text                     |           | not null | 
    tracking          | text                     |           |          | 
    shipping_provider | text                     |           | not null | 
    line_items        | text[]                   |           | not null | 
    qty               | integer                  |           | not null | 1
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "orders_drop_id_fkey" FOREIGN KEY (drop_id) REFERENCES drops(id)
    "orders_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id)
*/

ALTER TABLE orders
ALTER COLUMN tracking DROP NOT NULL;

ALTER TABLE orders
ADD COLUMN line_items TEXT[] NOT NULL;

ALTER TABLE orders
ADD COLUMN qty INTEGER NOT NULL DEFAULT 1;

INSERT INTO orders(user_id, order_number, drop_id, amount_cents, address, tracking, shipping_provider, line_items, qty)
VALUES (1, 'S9999C01D01', 1, 29997, '1335 west pace ferry way, Atlanta, GA, 30327', '819740732389rt4h2845t890g548h9', 'UPS', ARRAY['L', 'S', 'L'], 3),
       (2, 'S9999C02D01', 1, 9999, 'Gainsborough Rd, West Ham, London, E15 3AF, LN', 'bhdjsvbke58493584fjkaw', 'DHL', ARRAY['S'], 1),
       (3, 'S9999C03D01', 1, 49995, '2 Rue Auguste Gache, Grenoble, Isère, 38000, FR', '4572vjdskv35748kdsjfl93275843', 'UPS', ARRAY['S', 'S', 'M', 'M', 'M'], 5);

INSERT INTO orders (
    user_id,
    order_number,
    drop_id,
    amount_cents,
    address,
    tracking,
    shipping_provider,
    line_items,
    qty
)
VALUES
(
    4,
    'S9999C04D01',
    1,
    19998,
    '742 Evergreen Terrace, Springfield, IL, 62704',
    '1Z999AA10123456784',
    'UPS',
    ARRAY['M', 'M'],
    2
),
(
    1,
    'S9999C01D02',
    1,
    9999,
    '1335 West Paces Ferry Way, Atlanta, GA, 30327',
    '9400111899223857364721',
    'USPS',
    ARRAY['L'],
    1
),
(
    2,
    'S9999C02D02',
    1,
    39996,
    'Gainsborough Rd, West Ham, London, E15 3AF, LN',
    'JD014600006421344573',
    'DHL',
    ARRAY['S', 'M', 'L', 'XL'],
    4
),
(
    3,
    'S9999C03D02',
    1,
    29997,
    '2 Rue Auguste Gache, Grenoble, Isère, 38000, FR',
    '1Z888BB20234567895',
    'UPS',
    ARRAY['M', 'M', 'L'],
    3
),
(
    4,
    'S9999C04D02',
    1,
    49995,
    '742 Evergreen Terrace, Springfield, IL, 62704',
    NULL,
    'FedEx',
    ARRAY['S', 'S', 'M', 'L', 'XL'],
    5
),
(
    1,
    'S9999C01D03',
    1,
    19998,
    '1335 West Paces Ferry Way, Atlanta, GA, 30327',
    '78123456789012345678',
    'DHL',
    ARRAY['XL', 'XL'],
    2
),
(
    2,
    'S9999C02D03',
    1,
    59994,
    'Gainsborough Rd, West Ham, London, E15 3AF, LN',
    NULL,
    'UPS',
    ARRAY['S', 'S', 'M', 'M', 'L', 'L'],
    6
),
(
    3,
    'S9999C03D03',
    1,
    9999,
    '2 Rue Auguste Gache, Grenoble, Isère, 38000, FR',
    '9400550200881234567890',
    'USPS',
    ARRAY['S'],
    1
),
(
    4,
    'S9999C04D03',
    1,
    29997,
    '742 Evergreen Terrace, Springfield, IL, 62704',
    'FDX998877665544332211',
    'FedEx',
    ARRAY['M', 'L', 'XL'],
    3
),
(
    1,
    'S9999C01D04',
    1,
    69993,
    '1335 West Paces Ferry Way, Atlanta, GA, 30327',
    NULL,
    'UPS',
    ARRAY['S', 'S', 'M', 'M', 'L', 'XL', 'XL'],
    7
);

COPY orders TO '/Users/repayjesus/Dev/personal/study/revival-clothing-backend/join_study_data.txt'
WITH (FORMAT CSV, HEADER, DELIMITER '|');

SELECT
    orders.id AS order_id,
    orders.shipping_provider,
    orders.tracking,
    users.id AS user_id,
    users.first_name,
    users.last_name,
    users.email,
    users.phone_number
FROM orders
INNER JOIN users
ON 
    orders.user_id = users.id
WHERE orders.tracking != ''
ORDER BY 
    orders.id;

SELECT
    users.id AS user_id,
    users.first_name,
    users.last_name,
    users.email,
    users.phone_number,
    orders.id AS order_id,
    orders.amount_cents,
    orders.line_items, 
    orders.qty 
FROM users
LEFT JOIN orders
ON
    orders.user_id = users.id;

SELECT
    u.id AS user_id,
    u.first_name,
    d.id AS drop_id,
    o.id AS order_id,
    o.order_number,
    o.line_items,
    o.qty
FROM orders AS o
LEFT JOIN users AS u
ON
    u.id = o.user_id 
LEFT JOIN drops AS d
ON
    o.drop_id = d.id
ORDER BY user_id;

SELECT
    u.id AS user_id,
    u.username,
    u.create_at
FROM
    users AS u
LEFT JOIN
    orders AS o
ON
    u.id = o.user_id
WHERE
    o.id IS NULL;

SELECT
    u.id AS user_id,
    u.first_name,
    u.last_name
FROM users AS u
LEFT JOIN orders AS o
    ON o.user_id = u.id
GROUP BY
    u.id,
    u.first_name,
    u.last_name;
    
'''
