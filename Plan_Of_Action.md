# Group 5 takeover plan.

## Contributing Policy updates:
Looking at the contributing.md we plan to update the policy on how the contributors will use branching.
The Contributing.md does not detail any specifics about branching policies per developer or features. The only standard the policy details is to ensure Travis check are passing. 
The Group will primarily use the master branch, since the Development team is not too large. For critical experiments which threaten the sanity of codebase, the team will have independent feature branches. 
We plan to assign a Testing Czar.
The testing czar will be responsible for merging the pull requests from Feature branches and will make sure that the test suite of each implemented feature exists and passes before getting merged back in.

## Testing updates:
The project is lacking a automated testing suite, style checkers, formatting guide, code coverage. 
We plan to have a policy where, each new developed feature/Function needs to have a Test case associated with it unless deemed unnecessary by Testing Czar.

## Organizational Updates: 
We will be using a project board to better keep track of tasks. 
The previous Team also used Project board. However, a lack of coherency between finished tasks and issues being closed is apparent. Also Duplicate issues only lead to more complexity.
We have already setup Templates for Issues related to Bug-Reports and Feature requests to ensure a common layout.

## Coding tasks:
As mentioned earlier, a general lack of coherency in issues prompted us to inherit the issues directly.
Instead, we decided to write our own issues by taking from their wiki to obtain a general idea and previous issues.
We quickly discovered that the back-end for the project simply does not exist and currently requires us to manually run a python file for assignment. 
The database used is AWS RDS, which might be hindrance to the Zero-boundary policy.

### List of Actions Based on Priority
    1.  Setup Flask Environment.
    2.  Integrate Front-End[React] with Back-End[Flask].
    3.  Setup Local Database using SQL rather than Aws. [Cost-Effective and Zero-boundary]
    4.  Implement the Signup Functionality. [Backend Implementation and Database connections]
    5.  Implement Validation checks on Signup/Project Details Form.
    6.  Implement the assignment algorithm, so as to allocate people to teams in Real time.
    7.  Convert Current Assignment Algorithm [Greedy Approach] to Clustering approach.
    8.  Implement project pipeline including deployment steps.
    9.  Add Unit tests to the testing suite.
    10. Tests are not executed in the Travis.
    11. Publish the Codebase to a downloadable package manager.

### Current Plan of Work [Task Allocations]:
All Group members will be involved for Tasks 1-3. [Due to this tasks forming the core of the project and might result in confusions if not handled properly]

Tasks 4-5 will be handled by Sameer, Sreemoyee and Poorvaja, who have some experience with Front-end from Project 1.

Tasks 6-7 will be handled by Neeraj, who is well versed with Algorithms and their optimizations.

Tasks 8 will be handled by Sameer.

Task 9 will be handled in phases: Since any new code implementation will already have test cases. The test cases for pre-existing code will be handled by all group members.

Tasks 10-11 will be handled by Dhruvil.