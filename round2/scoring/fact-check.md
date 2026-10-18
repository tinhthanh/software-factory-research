## Fact-check results (fetched 2026-10-18)

**1. Faros "Acceleration Whiplash" (Q2 2026). Verdict: SAI MỘT PHẦN.** Source: https://faros.ai/research/ai-acceleration-whiplash, plus https://www.faros.ai/blog/software-engineering-with-ai and https://www.faros.ai/blog/ai-code-quality-mirage
- (a) The report page says "5X Median Review Time". The figure "441.5%" does not appear on any Faros page I read. It shows up only in a Medium/Plain English post (ai.plainenglish.io "AI made your team slower…"). Cite it as "~5x". 441.5% (about 5.4x) is a third-party reading and should not be attributed to Faros.
- (b) Confirmed. The chart shows "+242.7% incidents per PR", with the headline "3X Incidents per PR".
- (c) Confirmed: "a decrease in deployments per week (-11.7%)". This compares high versus low AI adoption.
- (d) This figure is not on the report page. Faros's own blog confirms it: "unreviewed merges increased 76.3%, up from 31.3% six months earlier" (ai-code-quality-mirage), and "31% more PRs are now merging without any review" (software-engineering-with-ai). So it is correct, with Faros's blogs as the source.
- (e) Confirmed: "Two years of telemetry from 22K developers across 4K teams".

**2. Faros "AI code quality mirage". Verdict: XÁC NHẬN, with one wording fix.** Source: https://www.faros.ai/blog/ai-code-quality-mirage (published 2026-08-06, updated 2026-09-23)
- Quote: "The incident-to-PR ratio increased just 14.5%, compared with 242.7% in the April dataset"
- Quote: "monthly incidents rose 125.4%". The wording is "monthly incidents", not "tổng incident" (total incidents).
- The Q3 report "The Speed Trap" exists. The site banner reads "AI Engineering Report Q3 2026: The Speed Trap is now available". It uses the same sample of 22,000 devs and 4,000 teams.
- Speed Trap figures from Faros blogs: unreviewed merges +76.3%, work restarts +66.7% (April: +13.8%), time in QA +300.6%, MTTR +25.8%, bugs/PR +43.9%.
- Supporting source: https://www.faros.ai/blog/the-most-expensive-number-in-our-new-ai-engineering-report (2026-10-09).

**3. Vercel 58%. Verdict: XÁC NHẬN except 671, which is KHÔNG KIỂM CHỨNG ĐƯỢC from the primary source.**
- The URL https://vercel.com/blog/58-percent-of-prs-in-our-largest-monorepo-merge-without-human-review is the correct slug: the search index still holds it, along with a `.md` version. Right now both WebFetch and curl get HTTP 404, and the post is not in the vercel.com/blog listing, so it looks removed or unpublished. I could not find a new URL.
- Text from the search-engine index of that page: "an agent reviews and merges 58% of those pull requests without a human reviewer, and average merge time has dropped 62%, from 29 hours to 10.9 hours". Also: "The LLM began labeling every PR as LOW or HIGH risk". The post's revert baseline is 1.7%, with a 5.1% kill-switch threshold.
- Date and authors: April 6, 2026, by John Phamous, Kacee Taylor and Eric Dodds.
- "671 auto-approved PRs, zero reverts" appears only in a search summary of the CodeZine article (https://codezine.jp/article/detail/23896, which returned 403 to me). I could not read it in the original.

**4. METR, Feb 2026. Verdict: SAI MỘT PHẦN.** Source: https://metr.org/blog/2026-02-24-uplift-update/
- Confirmed: "We have data from 57 developers, across 143 repos, and 800+ tasks."
- Confirmed: "speedup of -18% with a confidence interval between -38% and +9%" (original developers) and "-4%, with a confidence interval between -15% and +9%" (newly recruited).
- Sign convention: this follows the 2025 convention, where +19% meant 19% longer. Negative therefore means less time, i.e. faster, though the evidence is weak.
- The "30–50%" figure is about developers, not tasks: "30% to 50% of developers told us that they were choosing not to submit some tasks". "30–50% of tasks withheld" is wrong.

**5. ETH Zurich arXiv 2602.11988. Verdict: SAI MỘT PHẦN.** Source: https://arxiv.org/abs/2602.11988
- Title: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
- The abstract says "does not generally improve task success rates" and "increasing inference cost by over 20% on average". So "no improvement" plus ">20% cost" is correct.
- I did not see a "~3%" drop in the abstract. That figure, if it exists, is in the paper body, which I did not read. Writing "giảm ~3%" without a body citation is risky.

**6. Veracode 2026. Verdict: XÁC NHẬN.** Source: https://www.veracode.com/blog/2026-genai-code-security-report
- Quote: "the average security pass rate sits at 56%". SD Times reports the release date as July 28, 2026.

**7. Uber. Verdict: XÁC NHẬN.**
- Four months: Fortune, republished on Yahoo at https://finance.yahoo.com/sectors/technology/articles/uber-burned-entire-2026-ai-180347400.html (2026-05-26/27): "burnt through its entire 2026 AI coding tools budget in just four months".
- The cap: Bloomberg, 2026-06-02, "Uber Caps Employee Spending on AI Tools Like Claude Code to Manage Costs". I read it via https://gigazine.net/gsc_news/en/20260605-uber-caps-ai: "limiting token spending per employee per AI coding tool to $1,500… per month". I did not read Bloomberg directly.

**8. Ona. Verdict: XÁC NHẬN.** Source: https://ona.com/stories/auto-approving-low-risk-prs
- Lead time 4.1h → 1.1h ("↓ 74%"), PRs merged in 4 weeks 1,316 → 4,149 ("↑ 215%").
- The windows are Feb 13–Mar 13 versus Mar 13–Apr 10, 2026, and only human-authored PRs are counted.

**9. Uncountable. Verdict: XÁC NHẬN.** Source: https://engineering.uncountable.com/coding
- Quote: "91% of product changes merge with no human approval".
- Quote: "Pull requests written by an agent, not a person" = 75%. This is the July 2026 figure, up from 0% in July 2025. The page has no publication date.

**10. Google Research. Verdict: XÁC NHẬN.** Source: https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/ (Jan 28, 2026)
- Quote: "every multi-agent variant we tested degraded performance by 39-70%".
- Quote: "centralized coordination improved performance by 80.9%". This is for parallelizable financial-reasoning tasks only.

**11. Merge-conflict papers. Verdict: XÁC NHẬN.**
- https://arxiv.org/abs/2607.04697: "41.7% vs. 19.8%, respectively, with non-overlapping 95% confidence intervals" (cross-agent vs intra-agent).
- https://arxiv.org/abs/2604.03551 (AgenticFlict): "a conflict rate of 27.67%", which is 29K+ of 107K+ simulated agentic PRs.

**12. LinearB. Verdict: XÁC NHẬN, with one wording fix.** Source: https://linearb.io/library/ai-in-software-development
- Quote: "AI pull requests merge within 30 days 32.7% of the time against 84.4% for unassisted pull requests".
- Quote: "Agentic pull requests wait 17.6 hours at the 75th percentile against 3.4 hours". The 17.6h applies to agentic PRs specifically, and the page says "wait", not "pickup".
- Sample: 8.1M PRs from 4,800 teams.

**13. Anthropic RCT. Verdict: XÁC NHẬN.** Source: https://www.anthropic.com/research/AI-assistance-coding-skills (Jan 29, 2026)
- Quote: "We recruited 52 (mostly junior) software engineers".
- Quote: "the AI group averaged 50% on the quiz, compared to 67% in the hand-coding group".

**14. CooperBench. Verdict: SAI MỘT PHẦN.** Source: https://arxiv.org/abs/2601.13295 (Jan 19, 2026)
- The paper exists and the ~30% figure is right: "agents achieve on average 30% lower success rates when working together compared to performing both tasks individually".
- The features are not interdependent. They "can be implemented independently but may conflict without proper coordination".
- The comparison is against doing both tasks individually, not "1 agent" as such.

**15. DORA −1.5% / −7.2%. Verdict: XÁC NHẬN that this is the 2024 report, per 25% increase in AI adoption.** Source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report
- Quote: "an estimated decrease in delivery throughput by 1.5%, and an estimated reduction in delivery stability by 7.2%".
- The same blog post ties it to "A 25% increase in AI adoption". Secondary sources quote the report as "7.2% reduction for every 25% increase in AI adoption".
- Attributing this to 2026 is wrong.

**16. DORA 2026. Verdict: KHÔNG KIỂM CHỨNG ĐƯỢC.** Source: https://dora.dev/research/
- The archive lists reports only up to 2025, the first "State of AI-assisted Software Development". There is no 2026 entry; the only other item is an undated banner for an "ROI of AI-assisted Software Development report".
- Search found no 2026 release. Do not cite DORA 2026 figures.

**17. Cloudflare. Verdict: XÁC NHẬN.** Source: https://blog.cloudflare.com/ai-code-review (datePublished 2026-04-20)
- Quote: "the average review costs $1.19" (median $0.98).
- Quote: "the system completed 131,246 review runs across 48,095 merge requests". The window is "first 30 days", March 10 to April 9, 2026.

**18. Stripe Minions. Verdict: XÁC NHẬN.**
- Part 1, https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents (2026-02-09): "Over a thousand pull requests merged each week", "human-reviewed", "we only have at most two rounds of CI".
- Part 2, https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2 (2026-02-19): "Over 1,300 … (up from 1,000 as of Part 1)".

## Summary table

| # | Claim | Verdict | Note |
|---|---|---|---|
| 1 | Faros Whiplash | SAI MỘT PHẦN | Faros says "5x"; 441.5% is only on Medium. 242.7%, −11.7% and 22K/4K are correct. 31.3% is confirmed by a Faros blog, not the report page |
| 2 | Faros mirage / Speed Trap | XÁC NHẬN | 14.5% correct. 125.4% is "monthly incidents". Speed Trap Q3 2026 exists (unreviewed merges +76.3%) |
| 3 | Vercel 58% | XÁC NHẬN (671 unverified) | Slug is correct but the page is now 404. 58%, 29h→10.9h and the LLM classifier are from the index. 671/0 reverts is secondary only |
| 4 | METR 2026 | SAI MỘT PHẦN | 57 devs and both CIs correct. 30–50% refers to developers, not tasks |
| 5 | AGENTS.md | SAI MỘT PHẦN | "Does not generally improve" and ">20%" cost confirmed. ~3% not in the abstract |
| 6 | Veracode 56% | XÁC NHẬN | Released July 28, 2026 |
| 7 | Uber | XÁC NHẬN | Four months: Fortune. $1,500/month/tool: Bloomberg 2026-06-02 (read via secondary) |
| 8 | Ona | XÁC NHẬN | 4.1→1.1h, 1,316→4,149 |
| 9 | Uncountable | XÁC NHẬN | 91% / 75% (July 2026) |
| 10 | Google scaling agents | XÁC NHẬN | 39–70% / +80.9% |
| 11 | 2607.04697 / AgenticFlict | XÁC NHẬN | 41.7/19.8; 27.67% |
| 12 | LinearB | XÁC NHẬN | 17.6h is agentic PR "wait" at P75 |
| 13 | Anthropic RCT | XÁC NHẬN | 52 people; 50% vs 67% |
| 14 | CooperBench | SAI MỘT PHẦN | ~30% correct, but the features are independent and may conflict, not interdependent |
| 15 | DORA −1.5/−7.2 | XÁC NHẬN (2024) | Per 25% rise in AI adoption; not 2026 |
| 16 | DORA 2026 | KHÔNG KIỂM CHỨNG ĐƯỢC | Not published on dora.dev |
| 17 | Cloudflare | XÁC NHẬN | $1.19; 131,246/48,095; 30 days |
| 18 | Stripe Minions | XÁC NHẬN | >1,000/week (Part 2: >1,300); 2 CI rounds; human review |
