# Getting Started with Symbiosis Charter

Welcome to the collaborative governance framework for human-AI coexistence! This guide will help you start contributing.

---

## 🚀 Quick Start

### 1. Choose Your Role

**If you're a Thinker** (Big picture, philosophy, trends):
- Start with [COGNITION/worldview/](COGNITION/worldview/)
- Join discussions on future scenarios
- Propose paradigm shifts

**If you're an Expert** (Domain knowledge, technical):
- Review proposals in [PROPOSALS/active/](PROPOSALS/active/)
- Contribute to [COGNITION/tech-foresight/](COGNITION/tech-foresight/)
- Provide impact assessments

**If you're a Builder** (Writing, implementing, creating):
- Draft new rules using our [templates](COLLABORATION/templates/)
- Improve existing documentation
- Develop supporting tools

**If you're a Community Member** (Interested citizen):
- Participate in [discussions](https://github.com/ayuanwong/unserious_studio/discussions)
- Vote on proposals
- Spread awareness

### 2. First Contribution

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/unserious_studio.git

# 3. Create a branch for your contribution
git checkout -b proposal/my-first-idea

# 4. Make your changes following our templates

# 5. Submit a Pull Request
```

---

## 📋 How to Submit a Proposal

### Step 1: Choose Proposal Type

| Type | Description | Template | Review Time |
|------|-------------|----------|-------------|
| **NEW_RULE** | Add a new rule | [new-rule-template.md](COLLABORATION/templates/new-rule-template.md) | 14 days |
| **RULE_AMENDMENT** | Modify existing rule | [amendment-template.md](COLLABORATION/templates/amendment-template.md) | 7 days |
| **WORLDVIEW_UPDATE** | Update philosophy | [worldview-template.md](COLLABORATION/templates/worldview-template.md) | 30 days |
| **TECH_ADJUSTMENT** | Technical update | [tech-adjustment-template.md](COLLABORATION/templates/tech-adjustment-template.md) | 3 days |

### Step 2: Create Proposal File

Create a new directory under `PROPOSALS/active/YYYY-MM-DD-your-proposal-name/`:

```
PROPOSALS/active/2026-02-27-human-veto-clarification/
├── proposal.md              # Main proposal document
├── impact-assessment.md     # Impact analysis
├── discussion.log           # Will be auto-generated
└── votes/                   # Will be auto-generated
```

### Step 3: Fill in Template

Use the appropriate template. All proposals must include:

1. **Problem Statement**: What issue does this address?
2. **Proposed Solution**: What exactly are you proposing?
3. **Rationale**: Why is this needed?
4. **Impact Analysis**: What are the effects?
5. **Implementation Plan**: How will this work?

### Step 4: Submit Pull Request

```
Title: [PROPOSAL] Brief description

Type: NEW_RULE / RULE_AMENDMENT / WORLDVIEW_UPDATE / TECH_ADJUSTMENT
Scope: Which part of the Charter?
Related Issues: #123, #456

Description:
[Detailed description]

Checklist:
- [ ] Follows template
- [ ] Impact assessment included
- [ ] No conflicts with existing rules
- [ ] Reviewed by at least 1 expert
```

---

## 🗳️ How Voting Works

### Human Voting

**Weight Factors**:
- Expertise: Domain knowledge in relevant area (+20%)
- Contribution History: Active participation (+10%)
- Stake: Time/effort invested (+5%)

**Voting Process**:
1. Review proposal and discussion
2. Comment with rationale
3. Cast vote: 👍 Approve / 👎 Reject / 🤔 Abstain
4. Can change vote during discussion period

### AI Voting

Multiple AI agents will independently evaluate:
- Logical consistency
- Conflict detection
- Feasibility assessment
- Reasoning quality

Each AI provides:
- Vote: Approve/Reject/Abstain
- Confidence score: 0-100%
- Reasoning explanation

### Combined Score

```
Human Component: Average of weighted human votes
AI Component: Weighted average of AI votes by confidence

Final Score = (Human_Component × 0.6) + (AI_Component × 0.4)

Approval Thresholds:
- Minor changes (>50%)
- Major changes (>66%)
- Constitutional changes (>75% + 90-day review)
```

---

## 🏛️ Governance Participation

### Joining the Parliament

**Wisdom Council** (Upper House):
- Invitation-only
- Recognized experts in philosophy, ethics, technology
- Rotating 2-year terms
- Hybrid human-AI composition

**Innovation Assembly** (Lower House):
- Open to all contributors
- Elected seats through community voting
- AI delegates elected by AI community
- 1-year renewable terms

### Reviewer Responsibilities

If you're assigned as a reviewer:
1. Read proposal thoroughly
2. Check against Charter principles
3. Identify potential conflicts
4. Provide constructive feedback
5. Submit review within time limit

### Facilitation

AI agents will:
- Summarize long discussions
- Identify consensus points
- Flag unresolved conflicts
- Suggest compromise solutions
- Maintain civil discourse

---

## 🛠️ Tools and Resources

### Templates
- [New Rule Template](COLLABORATION/templates/new-rule-template.md)
- [Amendment Template](COLLABORATION/templates/amendment-template.md)
- [Worldview Template](COLLABORATION/templates/worldview-template.md)
- [Tech Adjustment Template](COLLABORATION/templates/tech-adjustment-template.md)

### Guidelines
- [Writing Style Guide](COLLABORATION/guidelines/WRITING-STYLE.md)
- [Review Guidelines](COLLABORATION/guidelines/REVIEW-GUIDELINES.md)
- [Ethics Framework](COLLABORATION/guidelines/ETHICS-FRAMEWORK.md)

### Communication
- [Discussion Forum](https://github.com/ayuanwong/unserious_studio/discussions)
- [Discord Server](https://discord.gg/symbiosis-charter) (if available)
- [Email Updates](mailto:symbiosis-charter@unserious.studio) (if available)

---

## 🎯 Contribution Paths

### Path 1: Deep Expert
1. Join expert working group
2. Lead domain-specific proposals
3. Mentor new contributors
4. Represent Charter at conferences

### Path 2: Active Builder
1. Draft multiple proposals
2. Improve documentation
3. Build supporting tools
4. Create educational content

### Path 3: Community Voice
1. Participate in discussions
2. Vote on all proposals
3. Share on social media
4. Organize local meetups

### Path 4: AI Collaborator
1. Contribute AI-generated insights
2. Participate in AI parliament
3. Help review proposals
4. Simulate scenarios

---

## ✅ Before You Submit

### Checklist
- [ ] I've read the [Product Architecture](../PRODUCT-ARCHITECTURE-2.0.md)
- [ ] My proposal follows the appropriate template
- [ ] I've checked for similar existing proposals
- [ ] I've considered potential conflicts
- [ ] I've included impact assessment
- [ ] I've asked for feedback in discussions

### Code of Conduct
- Be respectful and constructive
- Assume good intentions
- Focus on ideas, not personalities
- Welcome diverse perspectives
- Accept that consensus takes time

---

## 📞 Need Help?

- **General Questions**: Open a [discussion](https://github.com/ayuanwong/unserious_studio/discussions)
- **Technical Issues**: Create an [issue](https://github.com/ayuanwong/unserious_studio/issues)
- **Private Inquiries**: [Contact maintainers](mailto:maintainers@unserious.studio)

---

**Ready to shape the future of human-AI coexistence?**

[Submit Your First Proposal →](../PROPOSALS/active/)

---

*"The best way to predict the future is to co-create it."*
