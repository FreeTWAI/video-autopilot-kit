# 一起把底層疊起來

我們以 Hao 的公開剪輯框架為起點，讓開發、測試、影音、音樂、文件、行銷與銷售夥伴都能找到明確的貢獻入口。這是工坊 Fork；上游作者仍保有自己的原始 repo，回送上游的 PR 另外協調。

## 一次完成一張任務

1. 從 [GitHub Issues](https://github.com/FreeTWAI/video-autopilot-kit/issues) 選一張，閱讀完成條件與討論。
2. 留言說明「我能做什麼／這次範圍／需要誰協助」。維護者確認後再認領，沒有人被平台自動派單。
3. 用自己的 GitHub 身分 Fork，或使用已有 Fork 加上工坊 remote；從工坊的最新 main 開工作分支。不要把密碼或 token 貼到 Issue。
4. 讓 Agent 讀 AGENTS.md 和 Issue；小幅實作、自己看差異，執行相關檢查。
5. 提交到 **FreeTWAI/video-autopilot-kit** 的 PR，描述 `Closes #任務編號`、測試與限制；請維護者 review。

## 可使用的既有檢查

先閱讀相關檔案與環境要求，再選與修改有關的命令；以下是上游既有入口，不代表本次協作文件已替你跑過：

```sh
python src/system_health.py --quick
python examples/02_caption_broll_match.py
python examples/04_shorts_gate.py
```

影音與字型依賴以 README／SETUP 為準。缺工具就記 `not_run` 與原因，不自動安裝、不補造 render。當前工坊 Fork 的 Actions 尚未啟用；本階段由作者附本機測試，維護者審查。

## 貢獻與機會

GitHub 的作者、review、PR 和合併 SHA 是可追溯紀錄；協作者依實際參與列出。文件、測試、設計、需求回饋與推廣也可提交成果。平台先顯示已合併 PR 的 GitHub 作者，不把自填帳號變成已驗證會員資歷。

自願開源貢獻不保證報酬；若形成客戶案，當事人另定範圍、分工、報酬及收款方式。平台不壟斷分配機會、不代收錢。受助者可以透過修文件、補測試、回覆問題、分享可公開成果回饋社群，並非強制勞務或換取基本存取的條件。

<!-- freedom-repository-guide:start -->
## 自由工坊：從一個成果到一個 PR

媒體自動化公會的剪輯框架與第一個公開共創試點。 保留 Hao 的 Editkin v4 流程、素材／QA 工具、範例，以及工坊 Issue／PR 任務入口。

先看[本倉 Issues](https://github.com/FreeTWAI/video-autopilot-kit/issues)與[現有 PR](https://github.com/FreeTWAI/video-autopilot-kit/pulls)。提出問題、這一輪範圍、完成條件與可投入時間，在 Issue 認領並協調重疊工作；維護者已直接派工時不必重複等待，將約定連回交接即可。使用自己的 fork／分支，PR 送到 **FreeTWAI/video-autopilot-kit:main**。

交給 Agent 前先讓它讀 [AGENTS.md](AGENTS.md)。PR 寫明變更用途、使用者可見結果、驗證命令、限制與原 Issue；附上可公開的合成案例或重現方式。Issue／PR 是程式協作的記錄，平台名片與公會身分不取代 repo 維護者的審查。

保留 Editkin v4 runtime 與上游署名。私人 profiles、config.py、原始媒體與後台數據留在使用者本機。中央只索引公開 repo／Issue／merged PR，不接收影片工作資料。

### 這個模組怎麼驗證

選擇與修改範圍相符的既有入口：

```sh
python3 src/system_health.py --quick
python3 examples/02_caption_broll_match.py
python3 examples/04_shorts_gate.py
```

命令列在這裡不表示本輪已執行。先核對依賴與環境，再記錄實際結果；缺工具、桌面、媒體或授權時寫 `not_run` 與原因，不能補造成功。純文件修改以連結／路徑核對與 `git diff --check` 為主。

### 署名與上游

工坊 Fork：上游產品／授權來源為 [Hao0321/video-autopilot-kit](https://github.com/Hao0321/video-autopilot-kit)；本次協作的 Issue／PR 送到 **FreeTWAI/video-autopilot-kit**，不是自動送往上游。 保留原作者與授權檔，另列真正完成文件、測試、設計、程式或協作的人。使用 AI 時如實交代協作範圍；只有實際 GitHub PR／review／合併紀錄可以作為對應貢獻證據，不能靠自填帳號推定。

自願貢獻不保證案源、XP、收益或雇用。若產生付費合作，由當事人另定條款與 Seller 外部收款；平台不代收。秘密、客戶資料、真實交易單據與未授權素材不進公開 Issue／PR。
<!-- freedom-repository-guide:end -->
