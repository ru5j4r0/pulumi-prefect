// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Prefect.Outputs
{

    [OutputType]
    public sealed class GetAccountMembersMemberResult
    {
        /// <summary>
        /// Acount Role ID (UUID)
        /// </summary>
        public readonly string AccountRoleId;
        /// <summary>
        /// Name of Account Role assigned to member
        /// </summary>
        public readonly string AccountRoleName;
        /// <summary>
        /// Actor ID (UUID)
        /// </summary>
        public readonly string ActorId;
        /// <summary>
        /// Member email
        /// </summary>
        public readonly string Email;
        /// <summary>
        /// Member's first name
        /// </summary>
        public readonly string FirstName;
        /// <summary>
        /// Member handle, or a human-readable identifier
        /// </summary>
        public readonly string Handle;
        /// <summary>
        /// Account Member ID (UUID)
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Member's last name
        /// </summary>
        public readonly string LastName;
        /// <summary>
        /// User ID (UUID)
        /// </summary>
        public readonly string UserId;

        [OutputConstructor]
        private GetAccountMembersMemberResult(
            string accountRoleId,

            string accountRoleName,

            string actorId,

            string email,

            string firstName,

            string handle,

            string id,

            string lastName,

            string userId)
        {
            AccountRoleId = accountRoleId;
            AccountRoleName = accountRoleName;
            ActorId = actorId;
            Email = email;
            FirstName = firstName;
            Handle = handle;
            Id = id;
            LastName = lastName;
            UserId = userId;
        }
    }
}
