# Compatibility issues with plans

Working with plans > Compatibility issues with plans
Compatibility issues with plans

In some cases, applying a plan on a workload might cause compatibility issues.

You might observe the following issues:

Conflicting plan – there is a conflict between the plan that you are applying and an already applied plan.

For example, some settings in the plan might conflict with the settings in the already applied plan, or the same workload might already have been protected as part of a device group.

Incompatible operating system – the operating system of the workload is not supported.
Unsupported agent – the version of the protection agent on the workload is outdated and does not support the configured functionality.
Insufficient quota – there is not enough service quota in the tenant to assign to the selected workload.
Incompatible workload type – the selected functionality is not available for this workload type.
Missing advanced pack – the selected functionality is not available because a required advanced pack is not enabled for this customer.

The following table summarizes the possible compatibility issues for different plan types.

Issue/Plan type	Protection plan	Scripting plan	Monitoring plan	Remote management plan	Software deployment plan


Conflicting plan

+*	-	-	+	-


Incompatible operating system

+	+	+	+	+


Unsupported agent

+	+	+	+	+


Insufficient quota

+	+	+	+	-


Incompatible workload type

+	+	+	+	-
Missing advanced pack	+	-	-	-	-

* No conflicts are triggered if different backup settings are configured in multiple protection plans for the same workload.

If the plan is applied to up to 150 individually selected workloads, you will be prompted to resolve the existing conflicts before saving the plan. To resolve a conflict, remove the root cause for it or remove the affected workloads from the plan. For more information, see Resolving compatibility issues. If you do not resolve the conflicts, depending on the type of compatibility issue, the whole plan or some of its modules will be disabled on the incompatible workloads, and alerts will be shown.

If the plan is applied to more than 150 workloads or to device groups, first it will be saved, and then checked for compatibility. Depending on the type of compatibility issue, the whole plan or some of its modules will be disabled on the incompatible workloads, and alerts will be shown.

Resolving compatibility issues

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.