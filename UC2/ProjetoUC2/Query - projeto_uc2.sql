CREATE TABLE delivery_logistics(
delivery_id INT PRIMARY KEY,
delivery_partner VARCHAR(255),
package_type VARCHAR(255),
vehicle_type VARCHAR(255),
delivery_mode VARCHAR(255),
region VARCHAR(255),
weather_condition VARCHAR(255),
distance_km  DECIMAL(10, 2),
package_weight_kg  DECIMAL(10, 2),
delivery_time_hours DATE,
expected_time_hours DATE,
delayed_product VARCHAR(255),
delivery_status VARCHAR(255),
delivery_rating INT,
delivery_cost DECIMAL(10, 2)

);