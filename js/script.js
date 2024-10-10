// 获取 logo 元素和 logo 图片
const logo = document.querySelector('.logo');
const logoImage = document.querySelector('.logo img');

let hoverTimer; // 用于定时器
let rotationSpeed = 0; // 旋转速度
let isRotating = false; // 是否正在旋转

// 鼠标悬停事件
logo.addEventListener('mouseenter', () => {
    // 设置悬停计时
    hoverTimer = setTimeout(() => {
        isRotating = true; // 开始旋转
        rotationSpeed = 2; // 初始旋转速度
        rotateLogo(); // 启动旋转
    }, 1000); // 1秒后开始旋转
});

// 鼠标离开事件
logo.addEventListener('mouseleave', () => {
    clearTimeout(hoverTimer); // 清除悬停计时器
    isRotating = false; // 停止旋转
    rotationSpeed = 0; // 重置旋转速度
    logoImage.style.transform = 'rotate(0deg)'; // 复位
});

// 旋转 Logo 函数
function rotateLogo() {
    if (isRotating) {
        rotationSpeed += 0.5; // 每次递增旋转速度
        logoImage.style.transform = `rotate(${rotationSpeed * 10}deg)`; // 旋转10度每次
        requestAnimationFrame(rotateLogo); // 请求下一帧
    }
}