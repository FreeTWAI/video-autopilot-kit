# 共創任務入口

[查看／認領 GitHub Issues](https://github.com/FreeTWAI/video-autopilot-kit/issues) · [建立有完成條件的新任務](https://github.com/FreeTWAI/video-autopilot-kit/issues/new/choose) · [平台找夥伴](https://freetwai.com/#cocreation)

`collaboration/tasks.json` 提供 Agent 可讀的入口索引；進度、認領、留言與驗收以 GitHub Issue／PR 為準，這裡不另存第二份狀態。

```sh
gh issue list --repo FreeTWAI/video-autopilot-kit --state open --json number,title,labels,assignees,url
gh issue view 1 --repo FreeTWAI/video-autopilot-kit --json title,body,comments,assignees
```

第一輪有測試素材、檢查工具、字幕／配樂擴充、共同推廣與 Pillow 依賴修復五個方向。每張 Issue 已列範圍、完成條件、驗證方式與需要的角色。先留言協調，再用自己的分支提 PR；這些任務還在待認領，不是完成成果。
