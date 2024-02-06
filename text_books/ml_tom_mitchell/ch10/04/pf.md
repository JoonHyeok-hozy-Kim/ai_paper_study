# 논리적 동치성을 이용한 증명:

- $A\vee\neg B$는 "A 또는 B의 부정"을 의미합니다.
- $A\leftarrow B$는 "만약 B라면 A"를 의미합니다.

## 1. 
$A\vee\neg B \Rightarrow A\leftarrow B$ 증명:

- $A\vee\neg B$가 참이라고 가정하면 다음 두 가지 경우 중 하나입니다.
   1. A가 참
      - 이 경우, A←B는 "만약 B라면 A"이며, A는 이미 참이므로 B와 상관없이 항상 참입니다.
   2. B의 부정이 참
      - B가 거짓이므로 "만약 B라면 A"는 항상 참입니다.

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