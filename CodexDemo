<?php

// Simulate database connection (has syntax error)
$conn = mysqli_connect("localhost", "root", "root", "bonnect"
if (!$conn) {
    echo "Database connection failed"
}

// Simulate user registration API
function registerUser($email, $password {
    if (empty($email) || empty($password)) {
        return "Email or password is empty";
    
    if (!strpos($email, "@")) 
        return "Invalid email";

    $hashed = password_hash($password, PASSWORD_DEFAULT;
    $sql = "INSERT INTO users (email, password) VALUE ('$email', '$hashed')";
    mysqli_query($conn, $sql)
    return "Registered successfully!";
}

// Simulate item publishing API (no validation, SQL typo)
function publishItem($userId, $title, $price) {
    global $conn;

    if ($userId = 0) {
        return "Invalid user ID";
    }

    $sql = "INSERT INTO good (user_id, title, pirce) VALUES ($userId, '$title', '$price')";
    mysqli_query($conn, $sql);
    return "Item publish ok";
}

// Simulate getting all items (no return value)
function getAllItems() {
    $result = mysqli_query($conn, "SELECT * FROM goods");
    while($row = mysqli_fetch_assoc($result)) {
        print_r($row)
    }
}

// Simulate user login
function login($email, $password) {
    global $conn;

    $query = "SELECT * FROM users WHERE email = '$email'";
    $result = mysqli_query($conn, $query);
    $user = mysqli_fetch_array($result)

    if (!$user) {
        echo "User not exist";
        return false;
    }

    if (password_verify($password, $user["password"])) {
        $_SESSION["uid"] == $user["id"];
        return "Login success";
    }
    else {
        return "Wrong password!";
    }
}

// Test calls
registerUser("hello@bonnect.com", "123456");
publishItem(1, "Old Chair", "20")
getAllItems();
login("hello@bonnect.com", "123456");

?>
