# 🐾 나의 가장 따뜻한 기적에게 — Luxury Pet Letter Card

> 사랑스러운 반려견의 사진을 전체 배경으로 담아, 따뜻한 햇살과 오르골 선율 속에서 애틋한 마음을 전하는 럭셔리 인터랙티브 편지 카드 웹 프로젝트입니다.

---

## ✨ 주요 특징 (Features)

* **풀스크린 시네마틱 배경 (Breathing Background)**
  * 강아지 사진(`dog_photo.png`)을 화면 전체에 배치하고, 은은하게 숨 쉬듯 확대·축소되는 애니메이션과 따뜻한 비네팅 오버레이를 적용했습니다.
* **위에서 아래로 내려오는 편지 애니메이션 (Cascading Drop-Reveal)**
  * 편지 제목부터 각 문단, 마지막 서명까지 시간차를 두고 부드럽게 내려오며 나타납니다.
  * 하단의 **`↻ 편지 다시 보기`** 버튼을 통해 언제든 애니메이션을 처음부터 다시 감상할 수 있습니다.
* **은은한 햇살 빛줄기 & 하트 파티클 (Sunbeams & Floating Hearts)**
  * 대각선으로 비추는 따뜻한 빛줄기(CSS)와 아래에서 위로 떠오르는 반투명 하트·금빛 입자(HTML5 Canvas)가 어우러져 감성적인 분위기를 연출합니다.
* **별도 음원 없는 오르골 멜로디 (Web Audio API)**
  * 외부 MP3 파일 없이 브라우저 내장 **Web Audio API**만으로 따뜻하고 잔잔한 피아노·오르골 선율을 실시간으로 연주합니다.
  * 우측 상단 **`음악 켜기`** 버튼으로 재생 및 일시정지가 가능합니다.
* **완벽한 반응형 디자인 (Responsive Layout)**
  * 모바일 세로 화면부터 태블릿, 데스크톱까지 기기 크기에 맞춰 여백과 폰트 크기가 자연스럽게 최적화됩니다.

---

## 📁 폴더 구조 (Directory Structure)

```text
dog-luxury-letter-card/
├── index.html       # 메인 HTML, CSS 스타일 및 인터랙션 스크립트
├── dog_photo.png    # 카드 전체 배경으로 사용되는 강아지 이미지
└── README.md        # 프로젝트 설명 문서
```

---

## 🚀 실행 및 배포 방법 (Getting Started)

별도의 빌드 도구나 패키지 설치 없이 바로 실행할 수 있습니다.

1. **로컬에서 실행하기**
   * 저장소를 클론하거나 ZIP 파일의 압축을 푼 뒤, `index.html` 파일을 웹 브라우저(Chrome, Safari, Edge 등)로 엽니다.
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. **GitHub Pages로 웹에서 공유하기**
   * GitHub 저장소의 **Settings > Pages** 메뉴에서 `Branch`를 `main` (또는 `master`)으로 설정하고 저장하면, 모바일에서도 링크 하나로 편지 카드를 공유할 수 있습니다.

---

## 🎨 커스터마이징 가이드 (Customization)

* **사진 변경하기:** 같은 폴더 내의 `dog_photo.png` 파일을 원하는 사진으로 교체하거나, `index.html`의 `.bg-image` 스타일에서 `background-image: url('파일명');` 경로를 수정하세요.
* **편지 문구 수정하기:** `index.html` 내 `<article class="letter-card">` 영역의 제목(`.letter-title`), 본문(`.drop-line`), 서명(`.letter-sign`) 텍스트를 원하는 내용으로 자유롭게 바꿀 수 있습니다.

---

## 🛠️ 사용 기술 (Tech Stack)

* **HTML5** (Semantic Markup & Canvas API)
* **CSS3** (Glassmorphism, Keyframe Animations, Responsive Clamp Typography)
* **Vanilla JavaScript** (Canvas Particle System & Web Audio API Synthesizer)
* **Google Fonts** (`Gowun Batang`, `Noto Serif KR`, `Cormorant Garamond`)