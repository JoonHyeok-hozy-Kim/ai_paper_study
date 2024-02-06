# 논리적 동치성을 이용한 증명 (feat. Bard)

- $A\vee\neg B$는 "A 또는 B의 부정"을 의미합니다.
- $A\leftarrow B$는 "만약 B라면 A"를 의미합니다.

## 1. 
$A\vee\neg B \Rightarrow A\leftarrow B$ 증명:

- $A\vee\neg B$가 참이라고 가정하면 다음 두 가지 경우 중 하나입니다.
   1. A가 참
      - 이 경우, A←B는 "만약 B라면 A"이며, A는 이미 참이므로 B와 상관없이 항상 참입니다.
   2. B의 부정이 참
      - B가 거짓이므로 "만약 B라면 A"는 항상 참입니다.
        - why?)
          - 조건문의 특징:
            - 조건문 "만약 B라면 A"는 다음과 같은 특징을 가집니다.
              - B는 A의 충분 조건이지만, 필수 조건은 아니다.
              - B가 거짓이더라도 A가 참일 수 있는 경우가 존재한다.
        - e.g.)
          - B가 참 (비가 온다)이면 A는 항상 참 (땅이 젖는다)입니다.
          - 하지만 B가 거짓 (비가 안 온다)이더라도 A가 참 (땅이 젖는다)일 수 있습니다. 예를 들어, 사람이 물을 뿌려서 땅이 젖었을 수 있습니다.

- 따라서 두 경우 모두에서 $A\leftarrow B$는 참이므로, $A\vee\neg B \Rightarrow A\leftarrow B$임을 증명했습니다.

<br>

## 2.
$A \leftarrow B \Rightarrow A\vee\neg B$ 증명:

- $A\leftarrow B$가 참이라고 가정하면 "만약 B라면 A"입니다.
  1. B가 참
     - B가 참이므로, "만약 B라면 A"에 의해 A는 참이어야 합니다.
  2. B가 거짓
     - "만약 B라면 A"는 조건문이므로, B가 거짓이면 A의 참 거짓에 영향을 미치지 않습니다.
- 따라서 두 경우 모두에서 $A\vee\neg B$는 참이므로, $A \leftarrow B \Rightarrow A\vee\neg B$임을 증명했습니다.