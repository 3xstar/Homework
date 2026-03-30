<?php

// Разрешаем запросы с любого источника (для разработки)
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Обрабатываем preflight-запрос от браузера
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

header('Content-Type: application/json; charset=utf-8');
$conn = new mysqli("localhost", "root", "", "flutter_db");
$conn->set_charset("utf8");

$action = $_POST['action'] ?? '';
$sort = $_POST['sort'] ?? 'name';  // Параметр сортировки


if ($action === 'read') {
    // Сортировка: name, average_score (по убыванию)
    if ($sort === 'score') {
        $sql = "SELECT * FROM students ORDER BY average_score DESC";
    } else {
        $sql = "SELECT * FROM students ORDER BY name ASC";
    }
    $result = $conn->query($sql);
    
    $students = [];
    while($row = $result->fetch_assoc()){
        $students[] = $row;
    }

    echo json_encode(["success" => true, "data" => $students], JSON_UNESCAPED_UNICODE);
}

// СОЗДАНИЕ (POST)
if($action === 'create'){
    $name = $_POST['name'] ?? '';
    $group_num = $_POST['group_num'] ?? '';
    $average_score = $_POST['average_score'] ?? '';

    $comand = $conn->prepare("INSERT INTO students (name, group_num, average_score) VALUES (?,?,?)");
    $comand->bind_param("ssd", $name, $group_num, $average_score);
    $comand->execute();
    $comand->close();

    echo json_encode(["success" => true], JSON_UNESCAPED_UNICODE);
}

// ОБНОВЛЕНИЕ (POST)
if($action === 'update'){
    $id = $_POST['id'] ?? 0;
    $name = $_POST['name'] ?? '';
    $group_num = $_POST['group_num'] ?? '';
    $average_score = $_POST['average_score'] ?? '';

    $comand = $conn->prepare("UPDATE students SET name = ?, group_num = ?, average_score = ? WHERE id = ?");
    $comand->bind_param("ssdi", $name, $group_num, $average_score, $id);
    $comand->execute();
    $comand->close();

    echo json_encode(["success" => true], JSON_UNESCAPED_UNICODE);
}

// УДАЛЕНИЕ (POST)
if($action === 'delete'){
    $id = $_POST['id'] ?? 0;

    $comand = $conn->prepare("DELETE FROM students WHERE id = ?");
    $comand->bind_param("i", $id);
    $comand->execute();
    $comand->close();

    echo json_encode(["success" => true], JSON_UNESCAPED_UNICODE);
}

$conn->close();
?>